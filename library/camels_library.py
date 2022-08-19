# This script contains different routines to analyze the output of the CAMEL simulations
import numpy as np
import sys,os,h5py,time
import readgadget
import MAS_library as MASL
import units_library as UL
import sorting_library as SL
import Pk_library as PKL
import HI_library as HIL
import scipy.spatial as SS

# define constants here
rho_crit   = UL.units().rho_crit #h^2 Msun/Mpc^3
BOLTZMANN  = 1.38065e-16         #erg/K - NIST 2010
PROTONMASS = 1.67262178e-24      #gram  - NIST 2010

########################################################################################
# This function computes the distance of each gas particle to its Nneigh nearest 
# neighbourgs
# pos1 -------> positions of the particles
# pos2 -------> positions of the tracers (can be the same as pos1)
# k ----------> compute distance to Nneigh closest neighbourghs
# BoxSize ----> for non-periodic boundary conditions set this to None
# treads -----> number of openmp threads
# verbose ----> whether to print some information on the progress
def KDTree_distance(pos1, pos2, k, BoxSize=None, threads=1, verbose=True):

    # construct kdtree of the particles
    start  = time.time()
    kdtree = SS.cKDTree(pos1, leafsize=16, boxsize=BoxSize)
    if verbose:  print('Time to build KDTree = %.3f seconds'%(time.time()-start))

    # find nearest neighbors of the tracer particles
    start = time.time()
    dist, indexes = kdtree.query(pos2, k, n_jobs=threads)
    if verbose:  print('Time to find k-neighbors = %.3f seconds'%(time.time()-start))

    # return the distance of each particle to its farthest neighborgh
    return dist[:,-1]
########################################################################################

########################################################################################
# This routine returns the suffix of the considered ptype
def Pk_suffix(ptype):
    if   ptype==[0]:        return 'g'
    elif ptype==[1]:        return 'c'
    elif ptype==[4]:        return 's'
    elif ptype==[5]:        return 'bh'
    elif ptype==[0,1,4,5]:  return 'm'
    else:  raise Exception('no label found for ptype')
########################################################################################

########################################################################################
# This routine computes the power spectrum of a snapshot
# snapshot -----> snapshot name
# grid ---------> size of the grid to compute Pk
# MAS ----------> Mass Assignment Scheme (typically 'CIC')
# threads ------> number of OPENMP threads used to compute Pk
# ptype --------> particle type: [0]-gas, [1]-DM, [4]-stars, [5]-black holes
# root_out -----> folder where to save the power spectrum
def compute_Pk(snapshot, grid, MAS, threads, ptype, root_out):

    # read header
    if not(os.path.exists(snapshot)):  return 0
    head     = readgadget.header(snapshot)
    BoxSize  = head.boxsize/1e3  #Mpc/h  
    Nall     = head.nall         #Total number of particles
    Masses   = head.massarr*1e10 #Masses of the particles in Msun/h                    
    Omega_m  = head.omega_m
    Omega_l  = head.omega_l
    redshift = head.redshift
    Hubble   = 100.0*np.sqrt(Omega_m*(1.0+redshift)**3+Omega_l)#km/s/(Mpc/h)
    h        = head.hubble
    Ntot     = np.sum(Nall[ptype], dtype=np.int64)

    # get the name of the output file
    fout = '%s/Pk_%s_z=%.2f.txt'%(root_out, Pk_suffix(ptype), redshift)
    if os.path.exists(fout):  return 0

    # define the arrays containing the number positions and masses of the particles
    pos  = np.zeros((Ntot,3), dtype=np.float32)
    mass = np.zeros(Ntot,     dtype=np.float32)

    # read data for the different particle types
    f = h5py.File(snapshot, 'r');  offset = 0
    for pt in ptype:
        # sometimes there are not black-holes or stars...
        if 'PartType%d'%pt not in f.keys():  continue

        # read positions
        pos_pt  = f['PartType%d/Coordinates'%pt][:]/1e3  #Mpc/h
        if pos_pt.dtype==np.float64:  pos_pt = pos_pt.astype(np.float32)

        # read masses
        if 'PartType%d/Masses'%pt in f:
            mass_pt = f['PartType%d/Masses'%pt][:]*1e10                    #Msun/h
        else:
            mass_pt = np.ones(pos_pt.shape[0], dtype=np.float32)*Masses[1] #Msun/h

        # fill pos and mass arrays
        length  = len(pos_pt)
        pos[offset:offset+length]  = pos_pt
        mass[offset:offset+length] = mass_pt
        offset += length
    f.close()
    if offset!=Ntot:  raise Exception('Not all particles counted')

    # calculate density field
    delta = np.zeros((grid,grid,grid), dtype=np.float32)
    MASL.MA(pos, delta, BoxSize, MAS, W=mass)
    delta /= np.mean(delta, dtype=np.float64);  delta -= 1.0 

    # compute Pk and save results to file
    axis = 0
    Pk = PKL.Pk(delta, BoxSize, axis, MAS, threads)
    np.savetxt(fout, np.transpose([Pk.k3D, Pk.Pk[:,0]]), delimiter='\t')
########################################################################################

########################################################################################
# This routine computes the Pk of the ICs
# snapshot -----> snapshot name
# grid ---------> size of the grid to compute Pk
# MAS ----------> Mass Assignment Scheme (typically 'CIC')
# threads ------> number of OPENMP threads used to compute Pk
# ptype --------> particle type: [0]-gas, [1]-DM, [4]-stars, [5]-black holes
# root_out -----> folder where to save the power spectrum
def compute_Pk_ICs(snapshot, grid, MAS, threads, ptype, root_out):

    if not(os.path.exists(snapshot)) and not(os.path.exists(snapshot+'.0')):  return 0

    # read header
    head     = readgadget.header(snapshot)
    BoxSize  = head.boxsize/1e3  #Mpc/h  
    redshift = head.redshift

    # get the name of the file
    fout = '%s/Pk_%s_z=%.2f.txt'%(root_out, Pk_suffix(ptype), redshift)
    if os.path.exists(fout):  return 0
    
    # compute overdensity field
    do_RSD, axis = False, 0
    delta = MASL.density_field_gadget(snapshot, ptype, grid, MAS, do_RSD, axis)
    delta /= np.mean(delta, dtype=np.float64);  delta -= 1.0

    # compute Pk and save results to file
    Pk = PKL.Pk(delta, BoxSize, axis, MAS, threads)
    np.savetxt(fout, np.transpose([Pk.k3D, Pk.Pk[:,0]]), delimiter='\t')
########################################################################################

########################################################################################
# This routine computes Pk_hydro / Pk_Nbody
# root --------> main CAMEL folder
# sim ---------> simulation type 'IllustrisTNG' or 'SIMBA'
# i -----------> realization number
# snapnum -----> snapnum of the snapshot. Needed to get the redshift
# root_out ----> output folder
def compute_Pk_ratio(root, sim, i, snapnum, root_out):

    # find the number of N-body counterpart
    #if   i in map(str,np.arange(1522,1566)):                       j = 1505
    #elif i in ['1505_0', '1505_1', '1505_2', '1505_3', '1505_4']:  j = 1505
    #elif i in ['0_test', '0_clean0', '0_clean1']:                  j = 0
    #else:                                                          j = i

    #if i in ['1505_0', '1505_1', '1505_2', '1505_3', '1505_4', '1505_5', '1505_6',
    #         '1505_7', '1505_8', '1505_9', '1505_10', '1505_11', '1505_12', '1505_13',
    #         '1505_14', '1505_15', '1505_16', '1505_17', '1505_18', '1505_19', 
    #         '1505_20', '1505_21', '1505_22', '1505_23', '1505_24', '1505_25', 
    #         '1505_26'] and sim=='IllustrisTNG':
    #    sim2='SIMBA'
    #else:  sim2=sim

    # get the names of the snapshots
    #snapshot1 = '%s/Sims/%s/%s/snap_%03d.hdf5'%(root,sim,i,snapnum)
    #snapshot2 = '%s/Sims/%s_DM/%s/snap_%03d.hdf5'%(root,sim2,j,snapnum)
    snapshot1 = '%s/Sims/%s/%s/snap_%03d.hdf5'%(root,sim,i,snapnum)
    snapshot2 = '%s/Sims/%s_DM/%s/snap_%03d.hdf5'%(root,sim,i,snapnum)
    if not(os.path.exists(snapshot1)) or not(os.path.exists(snapshot2)): return 0

    # read the redshifts of the snapshots
    redshift1 = (readgadget.header(snapshot1)).redshift
    redshift2 = (readgadget.header(snapshot2)).redshift

    # get the name of the output file
    fout = '%s/Pk_ratio_m_z=%.2f.txt'%(root_out, redshift2)
    if os.path.exists(fout):  return 0

    # get the name of the power spectra
    f_hydro = '%s/Results/Pk/%s/%s/Pk_m_z=%.2f.txt'%(root,sim,i,redshift1)
    f_nbody = '%s/Results/Pk/%s_DM/%s/Pk_m_z=%.2f.txt'%(root,sim,i,redshift2)
    #f_nbody = '%s/Results/Pk/%s_DM/%s/Pk_m_z=%.2f.txt'%(root,sim,j,redshift2)
    if not(os.path.exists(f_hydro)) or not(os.path.exists(f_nbody)):  return 0

    # read power spectra and save results to file
    k1, Pk_hydro = np.loadtxt(f_hydro, unpack=True)
    k2, Pk_nbody = np.loadtxt(f_nbody, unpack=True)
    if np.any(k1!=k2):  raise Exception('k-values differ!')
    np.savetxt(fout, np.transpose([k1,Pk_hydro/Pk_nbody]))
########################################################################################

########################################################################################
# This routine computes the baryon fraction in FoF halos
# RMmin -------> minimum reduced mass (mass/Omega_m) in the halo
# RMmax -------> maximum reduced mass (mass/Omega_m) in the halo
# bins --------> baryon fraction is computed in log from Nmin to Nmax using # bins
# f_subfind ---> name of the subfind file
# snapshot ----> snapshot name (to read CDM particle masses)
# root_out ----> folder where to write the results
def baryon_fraction_FoF(RMmin, RMmax, bins, f_subfind, snapshot, root_out):

    # check if subfind file exists
    if not(os.path.exists(f_subfind)):  return 0

    # read header and get masses of CDM particles
    head     = readgadget.header(snapshot)
    BoxSize  = head.boxsize/1e3  #Mpc/h  
    Masses   = head.massarr*1e10 #Masses of the particles in Msun/h       
    Nall     = head.nall         #Total number of particles
    Om       = head.omega_m
    redshift = head.redshift
    Mc       = (Om - 0.049)*BoxSize**3*rho_crit/Nall[1] #mass of a CDM particle

    # get the name of the output file
    fout = '%s/bf_%.2e_%.2e_%d_z=%.2f.txt'%(root_out,RMmin, RMmax, bins, redshift)
    if os.path.exists(fout):  return 0

    # read halo masses
    f              = h5py.File(f_subfind, 'r')
    halo_mass      = f['Group/GroupMass'][:]*1e10
    halo_mass_type = f['Group/GroupMassType'][:]*1e10
    halo_part_type = f['Group/GroupLenType'][:]   #number of particles in each halo
    f.close()

    # take only halos with more than 50 CDM particles
    indexes = np.where(halo_part_type[:,1]>50)[0]
    halo_mass = halo_mass[indexes]
    halo_mass_type = halo_mass_type[indexes]

    # define the bins with the number of CDM particles and the intervals mean
    RM_bins = np.logspace(np.log10(RMmin), np.log10(RMmax), bins+1)
    RM_mean = 10**(0.5*(np.log10(RM_bins[1:]) + np.log10(RM_bins[:-1])))

    # compute baryon fraction in units of cosmic fraction
    fraction = ((halo_mass_type[:,0] + halo_mass_type[:,4] + halo_mass_type[:,5])/halo_mass) / (0.049/Om)

    # take bins in halo mass / Omega_m. Compute average baryon fraction
    mean_fraction = np.histogram(halo_mass/Om, RM_bins, weights=fraction)[0]
    Number        = np.histogram(halo_mass/Om, RM_bins)[0]
    Number[np.where(Number==0)] = 1.0
    mean_fraction = mean_fraction/Number

    # save results to file
    np.savetxt(fout, np.transpose([RM_mean, mean_fraction]))
########################################################################################

########################################################################################
# This routine computes the baryon fraction in FoF halos
# RMmin -------> minimum reduced mass (mass/Omega_m) in the halo
# RMmax -------> maximum reduced mass (mass/Omega_m) in the halo
# bins --------> baryon fraction is computed in log from Nmin to Nmax using # bins
# f_SO --------> name of the SO file
# snapshot ----> snapshot name (to read CDM particle masses)
# root_out ----> folder where to write the results
def baryon_fraction_SO(RMmin, RMmax, bins, f_SO, snapshot, root_out):

    # check if SO file exists
    if not(os.path.exists(f_SO)):  return 0

    # read header and get masses of CDM particles
    head     = readgadget.header(snapshot)
    BoxSize  = head.boxsize/1e3  #Mpc/h  
    Om       = head.omega_m
    redshift = head.redshift

    # get the name of the output file
    fout1 = '%s/bf_SO_%.2e_%.2e_%d_z=%.2f.txt'%(root_out, RMmin, RMmax, bins, redshift)
    fout2 = '%s/gf_SO_%.2e_%.2e_%d_z=%.2f.txt'%(root_out, RMmin, RMmax, bins, redshift)
    if os.path.exists(fout1) and os.path.exists(fout2):  return 0

    # read halo masses
    data = np.loadtxt(f_SO, unpack=False)
    halo_mass = data[:,0]
    Mg        = data[:,5]
    Mc        = data[:,6]
    Ms        = data[:,7]
    Mbh       = data[:,8]
    Nc        = data[:,11]

    # take only halos with more than 50 CDM particles
    indexes   = np.where(Nc>50)[0]
    halo_mass = halo_mass[indexes]
    Mg        = Mg[indexes]
    Mc        = Mc[indexes]
    Ms        = Ms[indexes]
    Mbh       = Mbh[indexes]

    # define the bins with the number of CDM particles and the intervals mean
    RM_bins = np.logspace(np.log10(RMmin), np.log10(RMmax), bins+1)
    RM_mean = 10**(0.5*(np.log10(RM_bins[1:]) + np.log10(RM_bins[:-1])))

    # compute baryon fraction in units of cosmic fraction
    fraction1 = ((Mg + Ms + Mbh)/halo_mass) / (0.049/Om)
    fraction2 = (Mg/halo_mass) / (0.049/Om)

    # take bins in halo mass / Omega_m. Compute average baryon fraction
    mean_fraction1 = np.histogram(halo_mass/Om, RM_bins, weights=fraction1)[0]
    mean_fraction2 = np.histogram(halo_mass/Om, RM_bins, weights=fraction2)[0]
    Number         = np.histogram(halo_mass/Om, RM_bins)[0]
    Number[np.where(Number==0)] = 1.0
    mean_fraction1 = mean_fraction1/Number
    mean_fraction2 = mean_fraction2/Number

    # save results to file
    np.savetxt(fout1, np.transpose([RM_mean, mean_fraction1]))
    np.savetxt(fout2, np.transpose([RM_mean, mean_fraction2]))
########################################################################################

########################################################################################
# This routine computes the mean and std of the halo mass function
# We use reduced mass instead of traditional mass because Omega_m changes a lot in the
# CAMEL simulations. Results are less sensitive to Omega_m using the reduced mass
# RMmin -------> minimum reduced mass (mass/Omega_m) in the halo
# RMmax -------> maximum reduced mass (mass/Omega_m) in the halo
# bins --------> baryon fraction is computed in log from Nmin to Nmax using # bins
# f_subfind ---> name of the subfind file
# snapshot ----> snapshot name (to read CDM particle masses)
# root_out ----> folder where to write the results
def halo_mass_function(RMmin, RMmax, bins, f_subfind, snapshot, root_out):

    # check if subfind file exists
    if not(os.path.exists(f_subfind)):  return 0

    # read header and get masses of CDM particles
    head     = readgadget.header(snapshot)
    BoxSize  = head.boxsize/1e3  #Mpc/h  
    Masses   = head.massarr*1e10 #Masses of the particles in Msun/h                    
    Nall     = head.nall         #Total number of particles
    Om       = head.omega_m
    redshift = head.redshift

    # get the name of the output file
    fout = '%s/mass_function_%.2e_%.2e_%d_z=%.2f.txt'%(root_out,RMmin,RMmax,bins,redshift)
    if os.path.exists(fout):  return 0

    # read halo masses
    f              = h5py.File(f_subfind, 'r')
    halo_mass      = f['Group/GroupMass'][:]*1e10 #Msun/h
    halo_part_type = f['Group/GroupLenType'][:]   #number of particles in each halo
    f.close()

    # take only halos with more than 50 CDM particles
    indexes   = np.where(halo_part_type[:,1]>50)[0]
    halo_mass = halo_mass[indexes]

    # define the arrays with the reduced mass (mass/Omega_m) bins, mean and width
    RM_bins = np.logspace(np.log10(RMmin), np.log10(RMmax), bins+1)
    RM_mean = 10**(0.5*(np.log10(RM_bins[1:]) + np.log10(RM_bins[:-1])))
    dRM     = RM_bins[1:] - RM_bins[:-1]

    # compute halo mass function and save results to file
    HMF = np.histogram(halo_mass/Om, RM_bins)[0]
    HMF = HMF/(BoxSize**3*dRM*Om)
    np.savetxt(fout, np.transpose([RM_mean*Om, RM_mean, HMF]))
########################################################################################

########################################################################################
# This routine reads the SFRH from the sims and produce a lighter file with the SFRH
# from z_min to z_max
# f_sfr ------> file with the star-formation rate history
# z_min ------> minimum redshift
# z_max ------> maximum redshift
# bins -------> number of bins to use
# BoxSize ----> Size of the simulation box
# root_out ---> output folder
def star_formation_rate_history(f_sfrh, z_min, z_max, bins, BoxSize, root_out):

    h = 0.6711

    # check if files exists
    fout = '%s/SFRH_%.2f_%.2f_%d.txt'%(root_out, z_min, z_max, bins)
    if os.path.exists(fout):  return 0
    if not(os.path.exists(f_sfrh)):  return 0

    # define the z-bins
    bins_z = np.linspace(z_min, z_max, bins)

    # read SFRH and interpolate and save results to file
    data = np.loadtxt(f_sfrh);  z, SFR = 1.0/data[:,0]-1.0, data[:,2]/(BoxSize/h)**3
    indexes = np.argsort(z);  z = z[indexes];  SFR = SFR[indexes]
    SFRH = np.interp(bins_z, z, SFR)
    #SFRH = np.interp(bins_z, z[::-1], SFR[::-1])
    np.savetxt(fout, np.transpose([bins_z, SFRH]))

# This routine computes the mean and std of the considered realizations
# sim ------------> simulation considered: 'SIMBA' or 'IllustrisTNG'
# z_min ----------> minimum redshift
# z_max ----------> maximum redshift
# bins -----------> number of bins
# root -----------> folder where data is
# realizations ---> array with the realizations to use for the mean and std
# fout -----------> name of output file
def mean_SFRH(sim, z_min, z_max, bins, root, realizations, fout, verbose=False):
    
    # define the array hosting all data
    SFRH = np.zeros((len(realizations),bins), dtype=np.float64)

    # read all SFRH and fill the array
    count = 0
    for i in realizations:
        fin = '%s/%s/%d/SFRH_%.2f_%.2f_%d.txt'%(root,sim,i,z_min,z_max,bins)
        if not(os.path.exists(fin)):  continue
        z, SFRH[count] = np.loadtxt(fin, unpack=True)
        count += 1
    if verbose:  print('Found %d realizations for %s'%(count,sim))
    SFRH = SFRH[:count]
    
    # save mean and std to file
    np.savetxt(fout, np.transpose([z, np.mean(SFRH, axis=0), np.std(SFRH, axis=0),
                                   np.percentile(SFRH,84,axis=0), 
                                   np.percentile(SFRH,16,axis=0)]))
########################################################################################

########################################################################################
# This routine computes the stellar mass function of a subfind catalogue
# SMmin -------> minimum value of the stellar mass; Msun/h
# SMmax -------> maximum value of the stellar mass; Msun/h
# bins --------> number of bins to compute the stellar mass function
# f_subfind ---> subfind catalogue
# root_out ----> output folder
def stellar_mass_function(SMmin, SMmax, bins, f_subfind, root_out):

    if not(os.path.exists(f_subfind)):  return 0

    # read stellar masses
    f = h5py.File(f_subfind, 'r')
    BoxSize  = f['Header'].attrs[u'BoxSize']/1e3 #Mpc/h
    redshift = f['Header'].attrs[u'Redshift']
    SM       = f['Subhalo/SubhaloMassType'][:]*1e10 #Msun/h
    SM       = SM[:,4]
    f.close()

    # get the name of the output file
    fout = '%s/SMF_%.2e_%2.e_%d_z=%.2f.txt'%(root_out, SMmin, SMmax, bins, redshift)
    if os.path.exists(fout):  return 0

    # define bins, mean and width of the stellar mass function
    bins_SM = np.logspace(np.log10(SMmin), np.log10(SMmax), bins+1)
    mean_SM = 0.5*(bins_SM[1:] + bins_SM[:-1])
    dSM     = bins_SM[1:] - bins_SM[:-1]

    # compute stellar mass function and save results to file
    SMF = np.histogram(SM, bins_SM)[0]
    SMF = SMF/(BoxSize**3*dSM)
    np.savetxt(fout, np.transpose([mean_SM, SMF]))
########################################################################################

########################################################################################
# This routine computes the average of different galaxy properties vs stellar mass
# SMmin -------> minimum value of the stellar mass; Msun/h
# SMmax -------> maximum value of the stellar mass; Msun/h
# bins --------> number of bins to compute the stellar mass function
# f_subfind ---> subfind catalogue
# root_out ----> output folder
# sim ---------> sim type 'SIMBA', 'IllustrisTNG'
# i -----------> name of the realization: e.g. '0' or '1505_0'
def properties_vs_SM(SMmin, SMmax, bins, f_subfind, root_out, sim, i):

    if not(os.path.exists(f_subfind)):  return 0

    # read stellar masses, 
    f = h5py.File(f_subfind, 'r')
    BoxSize  = f['Header'].attrs[u'BoxSize']/1e3 #Mpc/h
    redshift = f['Header'].attrs[u'Redshift']
    SM   = f['Subhalo/SubhaloMassType'][:][:,4]*1e10   #Msun/h
    Rp   = f['Subhalo/SubhaloHalfmassRadType'][:][:,4] #kpc/h
    BHp  = f['Subhalo/SubhaloBHMass'][:]*1e10          #Msun/h
    Vp   = f['Subhalo/SubhaloVmax'][:]                 #km/s
    SFRp = f['Subhalo/SubhaloSFR'][:]                  #Msun/yr
    f.close()

    # define bins, mean and width of the stellar mass function
    bins_SM = np.logspace(np.log10(SMmin), np.log10(SMmax), bins+1)
    mean_SM = 0.5*(bins_SM[1:] + bins_SM[:-1])
    dSM     = bins_SM[1:] - bins_SM[:-1]

    # number of galaxies in each stellar bin
    N = np.histogram(SM, bins_SM)[0]

    ##### Radii #####
    R = np.histogram(SM, bins_SM, weights=Rp)[0];  
    indexes = np.where(R!=0.0)[0];  R[indexes] = R[indexes]/N[indexes]
    root_out2 = '%s/Radii/%s/%s'%(root_out, sim, i)
    if not(os.path.exists(root_out2)):  os.makedirs(root_out2)
    fout = '%s/R_vs_SM_%.2e_%2.e_%d_z=%.2f.txt'%(root_out2,SMmin,SMmax,bins,redshift)
    np.savetxt(fout, np.transpose([mean_SM, R, N]))

    ##### BH mass #####
    BH = np.histogram(SM, bins_SM, weights=BHp)[0]
    indexes = np.where(BH!=0.0)[0];   BH[indexes] = BH[indexes]/N[indexes]
    root_out2 = '%s/BH/%s/%s'%(root_out, sim, i)
    if not(os.path.exists(root_out2)):  os.makedirs(root_out2)
    fout = '%s/BH_vs_SM_%.2e_%2.e_%d_z=%.2f.txt'%(root_out2,SMmin,SMmax,bins,redshift)
    np.savetxt(fout, np.transpose([mean_SM, BH, N]))

    ##### SFR #####
    SFR = np.histogram(SM, bins_SM, weights=SFRp)[0]
    indexes = np.where(SFR!=0.0)[0];   SFR[indexes] = SFR[indexes]/N[indexes]
    root_out2 = '%s/SFR/%s/%s'%(root_out, sim, i)
    if not(os.path.exists(root_out2)):  os.makedirs(root_out2)
    fout = '%s/SFR_vs_SM_%.2e_%2.e_%d_z=%.2f.txt'%(root_out2,SMmin,SMmax,bins,redshift)
    np.savetxt(fout, np.transpose([mean_SM, SFR, N]))

    ##### Vmax #####
    indexes = np.where(Vp!=np.inf)[0]
    V = np.histogram(SM[indexes], bins_SM, weights=Vp[indexes])[0]
    indexes = np.where(V!=0.0)[0];  V[indexes] = V[indexes]/N[indexes]
    root_out2 = '%s/Vmax/%s/%s'%(root_out, sim, i)
    if not(os.path.exists(root_out2)):  os.makedirs(root_out2)
    fout = '%s/Vmax_vs_SM_%.2e_%2.e_%d_z=%.2f.txt'%(root_out2,SMmin,SMmax,bins,redshift)
    np.savetxt(fout, np.transpose([mean_SM, V, N]))
########################################################################################

########################################################################################
# This function computes the temperature of the gas particles of a given snapshot
def temperature(snapshot):

    # read internal energy, electron abundance  and star-formation rate
    f      = h5py.File(snapshot, 'r')
    ne     = f['/PartType0/ElectronAbundance'][:]
    energy = f['/PartType0/InternalEnergy'][:] #(km/s)^2
    f.close()

    # compute the temperature
    yhelium = 0.0789
    T = energy*(1.0 + 4.0*yhelium)/(1.0 + yhelium + ne)*1e10*(2.0/3.0)
    T *= (PROTONMASS/BOLTZMANN)
    return T
########################################################################################

########################################################################################
# This function computes the HI mass of the gas particles of a given snapshot
def HI_mass(snapshot, TREECOOL_file, sim='IllustrisTNG'):

    # read redshift and h
    f = h5py.File(snapshot, 'r')
    redshift = f['Header'].attrs[u'Redshift']
    h        = f['Header'].attrs[u'HubbleParam']

    # read pos, radii, densities, HI/H and masses of gas particles 
    MHI  = f['PartType0/NeutralHydrogenAbundance'][:]
    mass = f['PartType0/Masses'][:]*1e10  #Msun/h
    rho  = f['PartType0/Density'][:]*1e19 #(Msun/h)/(Mpc/h)^3
    SFR  = f['PartType0/StarFormationRate'][:]
    indexes = np.where(SFR>0.0)[0];  del SFR
            
    # find the metallicity of star-forming particles
    if sim in ['IllustrisTNG', 'Astrid']:
        metals = f['PartType0/GFM_Metallicity'][:]
    elif sim=='SIMBA':
        metals = f['PartType0/Metallicity'][:,0] #metallicity
    else:
        raise Exception('Wrong simulation type!!!')
    metals = metals[indexes]/0.0127
    f.close()

    # find densities of star-forming particles: units of h^2 Msun/Mpc^3
    Volume = mass/rho                            #(Mpc/h)^3
    radii  = (Volume/(4.0*np.pi/3.0))**(1.0/3.0) #Mpc/h 
    rho    = rho[indexes]                        #h^2 Msun/Mpc^3
    Volume = Volume[indexes]                     #(Mpc/h)^3

    # find volume and radius of star-forming particles
    radii_SFR  = (Volume/(4.0*np.pi/3.0))**(1.0/3.0) #Mpc/h 
        
    # find HI/H fraction for star-forming particles
    MHI[indexes] = HIL.Rahmati_HI_Illustris(rho, radii_SFR, metals, redshift, h, 
                                            TREECOOL_file, Gamma=None, fac=1, 
                                            correct_H2=True) #HI/H
    MHI *= (0.76*mass)
    return MHI

########################################################################################

########################################################################################
# This function computes the pressure of the gas particles of a given snapshot
def pressure(snapshot):

    gamma = 5.0/3.0

    # read internal energy, electron abundance  and star-formation rate
    f   = h5py.File(snapshot, 'r')
    rho = f['/PartType0/Density'][:]*1e10   #(Msun/h)/(kpc/h)^3
    U   = f['/PartType0/InternalEnergy'][:] #(km/s)^2
    f.close()

    P = (gamma-1.0)*U*rho

    return P  #units are (Msun/h)*(km/s)^2/(kpc/h)^3
########################################################################################

########################################################################################
# This function computes the pressure of the gas particles of a given snapshot
def electron_density(snapshot):

    m_proton = 1.6726e-27    #kg
    Msun     = 1.99e30       #kg
    kpc      = 3.0857e21     #cm

    # read internal energy, electron abundance  and star-formation rate
    f    = h5py.File(snapshot, 'r')
    rho  = f['/PartType0/Density'][:]   #(1e10 Msun/h)/(kpc/h)^3
    ne   = f['/PartType0/ElectronAbundance'][:] 
    SFR  = f['PartType0/StarFormationRate'][:]
    f.close()

    # formula is 0.76*ne*rho/m_proton
    # rho units are (Msun/h)/(kpc/h)^3;  1e19*2e30/(3.1e24)^3/3e-55
    factor = 1e10*Msun/kpc**3/m_proton

    indexes = np.where(SFR>0.0)
    n_e = factor * 0.76 * ne * rho #electrons*h^2/cm^3
    n_e[indexes] = 0.0 #put electron density to 0 for star-forming particles

    return n_e
########################################################################################

# This routine computes different properties of SO halos such as mass in each component
# the temperature of the halo, number of particles...etc.
# snapshot --------> snapshot
# f_subfind -------> SUBFIND catalague
# cell_size -------> particles/halos will be places in a grid. This is to speed up the
#                    calculation. The voxel size should be larger than the radius of the
#                    largest halo in the snapshot
# root_out --------> output folder
def SO_properties(snapshot, f_subfind, cell_size, root_out):

    # check if subfind catalogue exists
    if not(os.path.exists(f_subfind)):  return 0

    # read the header and get BoxSize, redshift and masses
    f        = h5py.File(snapshot, 'r')
    BoxSize  = f['Header'].attrs[u'BoxSize']/1e3    #Mpc/h
    redshift = f['Header'].attrs[u'Redshift']
    Masses   = f['Header'].attrs[u'MassTable']*1e10 #Msun/h
    f.close()

    # get the name of the output file
    fout = '%s/SO_z=%.2f.txt'%(root_out, redshift)
    if os.path.exists(fout):  return 0

    ############################## HALOS ###############################
    # read the halo catalogue
    f = h5py.File(f_subfind, 'r')
    halo_pos  = f['Group/GroupPos'][:]/1e3           #Mpc/h
    halo_mass = f['Group/Group_M_TopHat200'][:]*1e10 #Msun/h
    halo_R    = f['Group/Group_R_TopHat200'][:]/1e3  #Mpc/h
    f.close()
    
    # keep only halos with radii larger than 0
    indexes   = np.where(halo_R>0)[0]
    halo_pos  = halo_pos[indexes]
    halo_mass = halo_mass[indexes]
    halo_R    = halo_R[indexes]

    # sort halo positions (not really neccesary, but positions will be closer in memory)
    data = SL.sort_3D_pos(halo_pos, BoxSize, cell_size, return_indexes=True, 
                          return_offset=False)
    halo_pos  = data.pos_sorted
    halo_R    = halo_R[data.indexes]
    halo_mass = halo_mass[data.indexes]
    ######################################################################

    ############################# PARTICLES ##############################
    # open the snapshot
    f = h5py.File(snapshot, 'r')

    ##### black-holes #####
    pos_bh  = f['/PartType5/Coordinates'][:].astype(np.float32)/1e3 #Mpc/h
    mass_bh = f['/PartType5/Masses'][:]*1e10                        #Msun/h
    Nbh     = np.ones(pos_bh.shape[0], dtype=np.float32)

    # sort the positions
    data = SL.sort_3D_pos(pos_bh, BoxSize, cell_size, return_indexes=True, 
                          return_offset=True)
    pos_bh    = data.pos_sorted
    mass_bh   = mass_bh[data.indexes]
    offset_bh = data.offset;  del data

    # compute the gas mass and number of gas particles
    halo_Mbh = np.zeros(halo_R.shape[0], dtype=np.float64)
    halo_Nbh = np.zeros(halo_R.shape[0], dtype=np.float64)
    HIL.HI_mass_SO(halo_pos, halo_R, pos_bh, mass_bh, offset_bh, halo_Mbh, BoxSize)
    HIL.HI_mass_SO(halo_pos, halo_R, pos_bh, Nbh,     offset_bh, halo_Nbh, BoxSize)
    del pos_bh, mass_bh, Nbh, offset_bh
    ######################

    ##### stars #####
    pos_s  = f['/PartType4/Coordinates'][:].astype(np.float32)/1e3 #Mpc/h
    mass_s = f['/PartType4/Masses'][:]*1e10                        #Msun/h
    Ns     = np.ones(pos_s.shape[0], dtype=np.float32)

    # sort the positions
    data = SL.sort_3D_pos(pos_s, BoxSize, cell_size, return_indexes=True, 
                          return_offset=True)
    pos_s    = data.pos_sorted
    mass_s   = mass_s[data.indexes]
    offset_s = data.offset;  del data

    # compute the gas mass and number of gas particles
    halo_Ms = np.zeros(halo_R.shape[0], dtype=np.float64)
    halo_Ns = np.zeros(halo_R.shape[0], dtype=np.float64)
    HIL.HI_mass_SO(halo_pos, halo_R, pos_s, mass_s, offset_s, halo_Ms, BoxSize)
    HIL.HI_mass_SO(halo_pos, halo_R, pos_s, Ns,     offset_s, halo_Ns, BoxSize)
    del pos_s, mass_s, Ns, offset_s
    ###################

    ##### CDM #####
    pos_c  = f['/PartType1/Coordinates'][:].astype(np.float32)/1e3   #Mpc/h
    if '/PartType1/Masses' in f:  
        mass_c = f['/PartType1/Masses'][:]*1e10                      #Msun/h
    else: 
        mass_c = np.ones(pos_c.shape[0], dtype=np.float32)*Masses[1] #Msunh
    Nc     = np.ones(pos_c.shape[0], dtype=np.float32)

    # sort the positions
    data = SL.sort_3D_pos(pos_c, BoxSize, cell_size, return_indexes=True, 
                          return_offset=True)
    pos_c    = data.pos_sorted
    mass_c   = mass_c[data.indexes]
    offset_c = data.offset;  del data

    # compute the gas mass and number of gas particles
    halo_Mc = np.zeros(halo_R.shape[0], dtype=np.float64)
    halo_Nc = np.zeros(halo_R.shape[0], dtype=np.float64)
    HIL.HI_mass_SO(halo_pos, halo_R, pos_c, mass_c, offset_c, halo_Mc, BoxSize)
    HIL.HI_mass_SO(halo_pos, halo_R, pos_c, Nc,     offset_c, halo_Nc, BoxSize)
    del pos_c, mass_c, Nc, offset_c
    ###################

    ##### gas #####
    pos_g  = f['/PartType0/Coordinates'][:].astype(np.float32)/1e3 #Mpc/h
    mass_g = f['/PartType0/Masses'][:]*1e10                        #Msun/h
    SFR    = f['/PartType0/StarFormationRate'][:]
    T      = temperature(snapshot)
    Ng     = np.ones(pos_g.shape[0], dtype=np.float32)

    # sort the positions
    data = SL.sort_3D_pos(pos_g, BoxSize, cell_size, return_indexes=True, 
                          return_offset=True)
    pos_g    = data.pos_sorted
    mass_g   = mass_g[data.indexes]
    SFR      = SFR[data.indexes]
    T        = T[data.indexes]
    offset_g = data.offset;  del data

    # compute the gas mass and number of gas particles
    halo_Mg = np.zeros(halo_R.shape[0], dtype=np.float64)
    halo_Ng = np.zeros(halo_R.shape[0], dtype=np.float64)
    HIL.HI_mass_SO(halo_pos, halo_R, pos_g, mass_g, offset_g, halo_Mg, BoxSize)
    HIL.HI_mass_SO(halo_pos, halo_R, pos_g, Ng,     offset_g, halo_Ng, BoxSize)
    del offset_g, Ng
    ###############

    ##### non-star forming gas #####
    indexes   = np.where(SFR<=0.0)[0];  del SFR
    pos_nsfg  = pos_g[indexes];         del pos_g
    mass_nsfg = mass_g[indexes];        del mass_g
    T_nsfg    = T[indexes];             del T
    Nnsfg     = np.ones(pos_nsfg.shape[0], dtype=np.float32)

    # sort the positions
    data = SL.sort_3D_pos(pos_nsfg, BoxSize, cell_size, return_indexes=True, 
                          return_offset=True)
    pos_nsfg    = data.pos_sorted
    mass_nsfg   = mass_nsfg[data.indexes]
    T_nsfg      = T_nsfg[data.indexes]
    offset_nsfg = data.offset;  del data

    # compute the gas mass and number of gas particles
    halo_Mnsfg  = np.zeros(halo_R.shape[0], dtype=np.float64)
    halo_TMnsfg = np.zeros(halo_R.shape[0], dtype=np.float64)
    halo_Nnsfg  = np.zeros(halo_R.shape[0], dtype=np.float64)
    HIL.HI_mass_SO(halo_pos, halo_R, pos_nsfg, mass_nsfg,        offset_nsfg, 
                   halo_Mnsfg, BoxSize)
    HIL.HI_mass_SO(halo_pos, halo_R, pos_nsfg, mass_nsfg*T_nsfg, offset_nsfg, 
                   halo_TMnsfg, BoxSize)
    HIL.HI_mass_SO(halo_pos, halo_R, pos_nsfg, Nnsfg,            offset_nsfg, 
                   halo_Nnsfg, BoxSize)
    del pos_nsfg, mass_nsfg, Nnsfg, offset_nsfg
    ################################
    f.close()

    # check that masses from routine give similar results that SUBFIND
    ratio = (halo_Mg + halo_Mc + halo_Ms + halo_Mbh)/halo_mass
    print(np.min(ratio), np.max(ratio))
    
    # compute average halo gas temperature
    halo_Mnsfg[np.where(halo_Mnsfg==0.0)[0]] = 1.0
    halo_T = halo_TMnsfg/halo_Mnsfg
    halo_Mnsfg[np.where(halo_Mnsfg==1.0)[0]] = 0.0

    # save results to file
    np.savetxt(fout, np.transpose([halo_mass, halo_R, halo_pos[:,0], halo_pos[:,1], 
                                   halo_pos[:,2], halo_Mg, halo_Mc, halo_Ms, halo_Mbh,
                                   halo_T, halo_Ng, halo_Nc, halo_Ns, halo_Nbh, 
                                   halo_Nnsfg]))
########################################################################################

########################################################################################
# This routine computes the mean and std of different files
# root -----------> folder where data is
# sim ------------> simulation considered: 'SIMBA' or 'IllustrisTNG'
# name -----------> The generic name of the files
# realizations ---> array with the realizations to use for the mean and std
# first ----------> integer representing the first column to read in the files
# second ---------> integer representing the second column to read in the files
# fout -----------> name of output file
def mean_std(root, sim, name, realizations, first, second, fout, verbose=False):
    
    # read the first realization and get dimensions of data vector
    fin = '%s/%s/%s/%s'%(root, sim, realizations[0], name)
    data_real = np.loadtxt(fin);  X,Y = data_real[:,first], data_real[:,second]
    data = np.zeros((len(realizations), len(X)), dtype=np.float64)

    # read all files and fill up the array
    count = 0
    for i in realizations:
        fin = '%s/%s/%s/%s'%(root, sim, i, name)
        if not(os.path.exists(fin)):  continue
        data_real = np.loadtxt(fin);  data[count] = data_real[:,second]
        count += 1
    if verbose:  print('Found %d realizations for %s'%(count,sim))
    data = data[:count]
    
    # save mean and std to file
    np.savetxt(fout, np.transpose([X, np.mean(data, axis=0), np.std(data, axis=0),
                                   np.percentile(data, 84, axis=0), 
                                   np.percentile(data, 16, axis=0),
                                   np.median(data, axis=0)]))
########################################################################################

########################################################################################
# This routine computes the mean and std of the halos temperature
# root -----------> folder where data is
# sim ------------> simulation considered: 'SIMBA' or 'IllustrisTNG'
# name -----------> The generic name of the files
# realizations ---> array with the realizations to use for the mean and std
# Mmin_T ---------> minimum halo mass
# Mmax_T ---------> maximum halo mass
# bins_T ---------> number of bins between Mmin_T and Mmax_T
# fout -----------> name of output file
def mean_std_T(root, sim, name, realizations, Mmin_T, Mmax_T, bins_T, 
               fout, verbose=False):

    # define the arrays containing the temperatures and number of halos
    bins_mass = np.logspace(np.log10(Mmin_T), np.log10(Mmax_T), bins_T+1)
    mass_mean = 0.5*(bins_mass[1:] + bins_mass[:-1])
    log_min, log_max = np.log10(Mmin_T), np.log10(Mmax_T)

    # define the structure containing the halo temperatures
    T = []
    for i in range(bins_T):  T.append([])

    # do a loop over all realizations
    count = 0
    for i in realizations:

        # read data
        fin = '%s/%s/%s/%s'%(root, sim, i, name)
        if not(os.path.exists(fin)):  continue
        data = np.loadtxt(fin)  
        halo_M, halo_T, Nnsfg = data[:,0], data[:,9], data[:,14]
            
        # only consider halos with more than 50 gas particles
        indexes = np.where(Nnsfg>50.0)[0]
        halo_M  = halo_M[indexes]
        halo_T  = halo_T[indexes]
        log_M   = np.log10(halo_M)

        # do a loop over the different halos
        for j in range(len(halo_M)):
            index = (log_M[j] - log_min)/(log_max - log_min)*bins_T
            if index<0.0 or index>bins_T:  continue
            index = int(index)
            T[index].append(halo_T[j])

        count +=1
    print('Found %d realization for %s'%(count,sim))

    # save results to file
    f = open(fout, 'w')
    for i in range(bins_T):
        array = np.array(T[i])
        f.write('%.5e %.5e %.5e %.5e %.5e %.5e\n'%(mass_mean[i], np.mean(array),
                                            np.std(array), np.percentile(array,84),
                                            np.percentile(array,16), np.median(array)))
    f.close()
########################################################################################

########################################################################################
# This routine computes the mean and std of galaxy:
# 1) radii
# 2) black hole masses
# 3) SFR
# 4) maximum velocities
# root -----------> folder where data is
# sim ------------> simulation considered: 'SIMBA' or 'IllustrisTNG'
# name -----------> The generic name of the files
# realizations ---> array with the realizations to use for the mean and std
# SMmin ----------> minimum stellar mass
# SMmax ----------> maximum stellar mass
# bins -----------> number of bins between SMmin and SMmax
# fout -----------> name of output file
def mean_std_SM(root, sim, name, realizations, SMmin, SMmax, bins,
                fout_R, fout_BH, fout_SFR, fout_V, verbose=False):

    # define the arrays containing the temperatures and number of halos
    bins_SM = np.logspace(np.log10(SMmin), np.log10(SMmax), bins+1)
    SM_mean = 0.5*(bins_SM[1:] + bins_SM[:-1])

    # define the lists containing the galaxy properties
    R, BH, SFR, V = [], [], [], []
    for i in range(bins):
        R.append([]);  BH.append([]);  SFR.append([]);  V.append([])

    # do a loop over all realizations
    count = 0
    for i in realizations:

        # read data
        fin = '%s/%s/%s/%s'%(root, sim, i, name)
        if not(os.path.exists(fin)):  continue
        f    = h5py.File(fin, 'r')
        SM   = f['Subhalo/SubhaloMassType'][:][:,4]*1e10   #Msun/h
        Rp   = f['Subhalo/SubhaloHalfmassRadType'][:][:,4] #kpc/h
        BHp  = f['Subhalo/SubhaloBHMass'][:]*1e10          #Msun/h
        SFRp = f['Subhalo/SubhaloSFR'][:]
        Vp   = f['Subhalo/SubhaloVmax'][:]                 #km/s
        f.close()
        
        # consider only galaxies within given stellar mass range
        indexes = np.where((SM>=SMmin) & (SM<SMmax))
        SM   = SM[indexes]
        Rp   = Rp[indexes]
        BHp  = BHp[indexes]
        SFRp = SFRp[indexes]
        Vp   = Vp[indexes]

        # do a loop over all galaxies
        index = (np.log10(SM)-np.log10(SMmin))/(np.log10(SMmax)-np.log10(SMmin))*bins
        index = np.int32(index)
        for j in range(len(SM)):
            R[index[j]].append(Rp[j])
            BH[index[j]].append(BHp[j])
            SFR[index[j]].append(SFRp[j])
            V[index[j]].append(Vp[j])

        count += 1
    print('found %d realization for %s'%(count,sim))

    f1 = open(fout_R,   'w');  f2 = open(fout_BH, 'w');  
    f3 = open(fout_SFR, 'w');  f4 = open(fout_V,  'w')
    for i in range(bins):
        array = np.array(R[i])
        f1.write('%.5e %.5e %.5e %.5e %.5e %.5e\n'%(SM_mean[i], np.mean(array),
                                        np.std(array), np.percentile(array,84),
                                        np.percentile(array,16), np.median(array)))
        array = np.array(BH[i])
        f2.write('%.5e %.5e %.5e %.5e %.5e %.5e\n'%(SM_mean[i], np.mean(array),
                                        np.std(array), np.percentile(array,84),
                                        np.percentile(array,16), np.median(array)))
        array = np.array(SFR[i])
        indexes = np.where(array>0.0)[0]  #select galaxies with SFR>0
        array2 = array[indexes]
        f3.write('%.5e %.5e %.5e %.5e %.5e %.5e %.5e %.5e %.5e %.5e %.5e\n'%(SM_mean[i], np.mean(array),
                                        np.std(array), np.percentile(array,84),
                                        np.percentile(array,16), np.median(array),
                                        np.mean(array2), np.std(array2), 
                                        np.percentile(array2,84), 
                                        np.percentile(array2,16), np.median(array2)))
        array = np.array(V[i])
        f4.write('%.5e %.5e %.5e %.5e %.5e %.5e\n'%(SM_mean[i], np.mean(array),
                                        np.std(array), np.percentile(array,84),
                                        np.percentile(array,16), np.median(array)))
    f1.close();  f2.close();  f3.close();  f4.close()

########################################################################################

########################################################################################
# This routine computes the mean and std of galaxy:
# 1) radii
# 2) black hole masses
# 3) SFR
# 4) maximum velocities
# root -----------> folder where data is
# sim ------------> simulation considered: 'SIMBA' or 'IllustrisTNG'
# name -----------> The generic name of the files
# realizations ---> array with the realizations to use for the mean and std
# SMmin ----------> minimum stellar mass
# SMmax ----------> maximum stellar mass
# bins -----------> number of bins between SMmin and SMmax
# fout -----------> name of output file
def mean_std_SM_old(root, sim, name, realizations, SMmin, SMmax, bins,
                    fout_R, fout_BH, fout_SFR, fout_V, verbose=False):
    
    #if os.path.exists(fout_R) and os.path.exists(fout_BH) and\
    #   os.path.exists(fout_Z) and os.path.exists(fout_V):  return 0

    # define the arrays containing the temperatures and number of halos
    bins_SM = np.logspace(np.log10(SMmin), np.log10(SMmax), bins+1)
    SM_mean = 0.5*(bins_SM[1:] + bins_SM[:-1])
    R    = np.zeros(bins, dtype=np.float64)
    R2   = np.zeros(bins, dtype=np.float64)
    BH   = np.zeros(bins, dtype=np.float64)
    BH2  = np.zeros(bins, dtype=np.float64)
    SFR  = np.zeros(bins, dtype=np.float64)
    SFR2 = np.zeros(bins, dtype=np.float64)
    V    = np.zeros(bins, dtype=np.float64)
    V2   = np.zeros(bins, dtype=np.float64)
    N    = np.zeros(bins, dtype=np.float64)
    N_BH = np.zeros(bins, dtype=np.float64)

    # do a loop over all realizations
    count = 0
    for i in realizations:

        # read data
        fin = '%s/%s/%d/%s'%(root, sim, i, name)
        if not(os.path.exists(fin)):  continue
        f    = h5py.File(fin, 'r')
        SM   = f['Subhalo/SubhaloMassType'][:][:,4]*1e10   #Msun/h
        Rp   = f['Subhalo/SubhaloHalfmassRadType'][:][:,4] #kpc/h
        BHp  = f['Subhalo/SubhaloBHMass'][:]*1e10          #Msun/h
        SFRp = f['Subhalo/SubhaloSFR'][:]
        Vp   = f['Subhalo/SubhaloVmax'][:]                 #km/s
        f.close()

        ids = np.where(SM>3e11)[0]
        if len(ids)>0:
            f = open('BH_test.txt', 'a')
            for i in range(len(ids)):
                f.write('%.4e\n'%BHp[ids][i])
            f.close()


        # radii
        R  += np.histogram(SM, bins_SM, weights=Rp)[0]
        R2 += np.histogram(SM, bins_SM, weights=Rp**2)[0]

        # black-holes masses
        indexes = np.where(BHp>1e8)[0]
        BH   += np.histogram(SM[indexes], bins_SM, weights=BHp[indexes])[0]
        BH2  += np.histogram(SM[indexes], bins_SM, weights=BHp[indexes]**2)[0]
        N_BH += np.histogram(SM[indexes], bins_SM)[0]
        #BH  += np.histogram(SM, bins_SM, weights=BHp)[0]
        #BH2 += np.histogram(SM, bins_SM, weights=BHp**2)[0]

        # SFR
        SFR  += np.histogram(SM, bins_SM, weights=SFRp)[0]
        SFR2 += np.histogram(SM, bins_SM, weights=SFRp**2)[0]

        # maximum velocity
        indexes = np.where(Vp!=np.inf)[0]
        V  += np.histogram(SM[indexes], bins_SM, weights=Vp[indexes])[0]
        V2 += np.histogram(SM[indexes], bins_SM, weights=Vp[indexes]**2)[0]

        # number of galaxies
        N  += np.histogram(SM, bins_SM)[0]
        count += 1
    print('found %d realization for %s'%(count,sim))

    # find average and standard deviation; save results to file
    R   = R/N;    dR   = np.sqrt(R2/N -   R**2)
    BH  = BH/N_BH;   dBH  = np.sqrt(BH2/N_BH -  BH**2)
    #BH  = BH/N;   dBH  = np.sqrt(BH2/N -  BH**2)
    SFR = SFR/N;  dSFR = np.sqrt(SFR2/N - SFR**2)
    V   = V/N;    dV   = np.sqrt(V2/N -   V**2)

    np.savetxt(fout_R,   np.transpose([SM_mean, R,   dR,   N]))
    np.savetxt(fout_BH,  np.transpose([SM_mean, BH,  dBH,  N]))
    np.savetxt(fout_SFR, np.transpose([SM_mean, SFR, dSFR, N]))
    np.savetxt(fout_V,   np.transpose([SM_mean, V,   dV,   N]))
########################################################################################

########################################################################################
# This routine computes the mean and std of the halos temperature
# root -----------> folder where data is
# sim ------------> simulation considered: 'SIMBA' or 'IllustrisTNG'
# name -----------> The generic name of the files
# realizations ---> array with the realizations to use for the mean and std
# Mmin_T ---------> minimum halo mass
# Mmax_T ---------> maximum halo mass
# bins_T ---------> number of bins between Mmin_T and Mmax_T
# fout -----------> name of output file
def mean_std_T_old(root, sim, name, realizations, Mmin_T, Mmax_T, bins_T, 
                   fout, verbose=False):

    # define the arrays containing the temperatures and number of halos
    bins_mass = np.logspace(np.log10(Mmin_T), np.log10(Mmax_T), bins_T+1)
    mass_mean = 0.5*(bins_mass[1:] + bins_mass[:-1])
    T  = np.zeros(bins_T, dtype=np.float64)
    T2 = np.zeros(bins_T, dtype=np.float64)
    N  = np.zeros(bins_T, dtype=np.float64)

    # do a loop over all realizations
    count = 0
    for i in realizations:

        # read data
        fin = '%s/%s/%d/%s'%(root, sim, i, name)
        if not(os.path.exists(fin)):  continue
        data = np.loadtxt(fin)  
        halo_M, halo_T, Nnsfg = data[:,0], data[:,9], data[:,14]
        #if i in [243,408,424] and sim=='SIMBA':
        #    continue
            #if np.any(halo_T>1e9):  
            #print(sim,i)
            #continue
            
        # only consider halos with more than 50 gas particles
        indexes = np.where(Nnsfg>50.0)[0]
        halo_M  = halo_M[indexes]
        halo_T  = halo_T[indexes]
        
        T  += np.histogram(halo_M, bins_mass, weights=halo_T)[0]
        T2 += np.histogram(halo_M, bins_mass, weights=halo_T**2)[0]
        N  += np.histogram(halo_M, bins_mass)[0]
        count += 1
    print('found %d realization for %s'%(count,sim))

    # find average and standard deviation;  save results to file
    T  = T/N
    dT = np.sqrt(T2/N - T**2)
    np.savetxt(fout, np.transpose([mass_mean, T, dT, N]))
########################################################################################

########################################################################################
# This routine will read data from a snapshot and will return the relevant quantities
# for a given field. For instance, for the field T, it will return the positions, 
# masses, and temperature of gas particles.
# snapshot -------> the name of considered snapshot
# field ----------> the considered field, e.g. 'T', or 'Mgas'
# sim ------------> 'IllustrisTNG' or 'SIMBA'
def field_properties(snapshot, field, sim):

    # check whether the snapshot exists
    if not(os.path.exists(snapshot)):  raise Exception('%s does not exists'%snapshot)

    # check that the field is included
    if field not in ['Mgas', 'Mcdm', 'Mtot', 'Mstar', 'T', 'Z', 'P', 
                     'ne', 'HI', 'Vgas', 'Vcdm', 'B', 'MgFe']:
        raise Exception('%s not implemented'%field)

    # read the main properties of the snapshot
    f = h5py.File(snapshot, 'r')
    BoxSize  = f['Header'].attrs[u'BoxSize']/1e3 #Mpc/h
    redshift = f['Header'].attrs[u'Redshift']
    h        = f['Header'].attrs[u'HubbleParam']
    Masses   = f['Header'].attrs[u'MassTable'][:]*1e10 #Msun/h
    Ntot     = f['Header'].attrs[u'NumPart_ThisFile']

    # read the positions and masses of the gas particles for all these fields
    if field in ['Mgas', 'T', 'Z', 'P', 'ne', 'HI', 'Vgas', 'B', 'MgFe', 'Mtot']:
        pos_g = f['PartType0/Coordinates'][:]/1e3 #Mpc/h
        pos_g = pos_g.astype(np.float32)          #Mpc/h
        Mg    = f['PartType0/Masses'][:]*1e10     #Msun/h  

    # read the positions and masses of the dark matter particles for these fields
    if field in ['Mcdm', 'Vcdm', 'Mtot']:
        pos_c = f['PartType1/Coordinates'][:]/1e3 #Mpc/h
        pos_c = pos_c.astype(np.float32)          #Mpc/h
        if sim=='IllustrisTNG':
            Mc = np.ones(pos_c.shape[0], dtype=np.float32)*Masses[1] #Msun/h
        if sim=='SIMBA':
            Mc = f['PartType1/Masses'][:]*1e10 #Msun/h

    # read the positions and masses of the star particles for these fields
    if field in ['Mstar', 'Mtot']:
        if sim=='IllustrisTNG':
            pos_sw = (f['PartType4/Coordinates'][:]/1e3).astype(np.float32)
            Msw    = f['PartType4/Masses'][:]*1e10     #Msun/h
            #Age    = f['PartType4/GFM_StellarFormationTime'][:] #stars have Age>0
            #indexes = np.where(Age>0)[0]
            #pos_s  = pos_sw[indexes] # FIXME unused! -- Paco double check
            #Ms     = Msw[indexes]
        else:
            pos_sw = (f['PartType4/Coordinates'][:]/1e3).astype(np.float32) #Mpc/h
            Msw    = f['PartType4/Masses'][:]*1e10 #Msun/h
            #pos_s  = np.copy(pos_sw)
            #Ms     = np.copy(Msw)

    # gas mass
    if field=='Mgas':  
        return pos_g, Mg

    # dark matter mass
    if field=='Mcdm':
        return pos_c, Mc

    # stellar mass
    if field=='Mstar':
        return pos_sw, Msw

    # gas temperature
    if field=='T':
        T  = temperature(snapshot) #K
        return pos_g, Mg, T

    # gas metallicity
    if field=='Z':
        if sim=='IllustrisTNG':
            Z = f['PartType0/GFM_Metallicity'][:] #metallicity
        if sim=='SIMBA':
            Z = f['PartType0/Metallicity'][:,0]+8e-10 #metallicity
        return pos_g, Mg, Z

    # gas pressure
    if field=='P':
        P = pressure(snapshot) #Msun*(km/s)^2/kpc^3
        return pos_g, Mg, P

    # electron density
    if field=='ne':
        rho_g = f['PartType0/Density'][:]*1e19    #(Msun/h)/(Mpc/h)^3
        Vol_g = Mg/rho_g;  del rho_g              #(Mpc/h)^3
        ne = electron_density(snapshot)*Vol_g #electrons/h
        return pos_g, Mg, ne

    # neutral hydrogen
    if field=='HI':
        HI = HI_mass(snapshot, TREECOOL_file, sim)
        return pos_g, HI

    # gas velocity
    if field=='Vgas':
        vel_g = f['PartType0/Velocities'][:]/np.sqrt(1.0+redshift)
        vel_g = np.sqrt(vel_g[:,0]**2 + vel_g[:,1]**2 + vel_g[:,2]**2)
        return pos_g, Mg, vel_g

    # dark matter velocity
    if field=='Vcdm':
        vel_c = f['PartType1/Velocities'][:]/np.sqrt(1.0+redshift)
        vel_c = np.sqrt(vel_c[:,0]**2 + vel_c[:,1]**2 + vel_c[:,2]**2)
        return pos_c, Mc, vel_c

    # magnetic fields
    if field=='B' and sim=='IllustrisTNG':
        B = np.linalg.norm(f['PartType0/MagneticField'][:]*2.6e-6*h/(1.0+redshift)**2, 
                           axis=-1) #Gauss
        return pos_g, Mg, B

    # magnesium over iron
    if field=='MgFe':
        if sim=='IllustrisTNG':
            Mmg = f['PartType0/GFM_Metals'][:,6]*Mg #magnesium
            Mfe = f['PartType0/GFM_Metals'][:,8]*Mg #iron
        if sim=='SIMBA':
            Mmg = (f['PartType0/Metallicity'][:,6]+1e-10)*Mg  #magnesium
            Mfe = (f['PartType0/Metallicity'][:,10]+1e-10)*Mg #iron
        return pos_g, Mmg, Mfe

    # total matter mass
    if field=='Mtot':
        if Ntot[5]>0:  
            pos_bh = f['PartType5/Coordinates'][:]/1e3 #Mpc/h
            pos_bh = pos_bh.astype(np.float32)         #Mpc/h
            Mbh    = f['PartType5/Masses'][:]*1e10     #Msun/h        
            return pos_g, Mg, pos_c, Mc, pos_sw, Msw, pos_bh, Mbh
        else:
            return pos_g, Mg, pos_c, Mc, pos_sw, Msw, pos_bh, Mbh

    # close file
    f.close()
