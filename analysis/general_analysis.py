# This script computes different quantities for each snapshot of each simulation
from mpi4py import MPI
import numpy as np
import sys,os,h5py,glob
import camel_library as CL


###### MPI DEFINITIONS ###### 
comm   = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm.Get_rank()


##################################### INPUT ############################################
# CAMEL root folder
root = '/mnt/ceph/users/camels' 

sims = ['IllustrisTNG','SIMBA']#, 'IllustrisTNG']

# Pk parameters
grid    = 512
MAS     = 'CIC'
threads = 1

# halo mass function and baryon fraction parameters
RMmin   = 1e10  #minimum reduced mass (halo mass / Omega_m)
RMmax   = 1e14  #maximum reduced mass (halo mass / Omega_m)
RM_bins = 30

# star-formation rate history parameters
z_min     = 0.0
z_max     = 10.0
sfrh_bins = 10000
BoxSize   = 25.0 #Mpc/h

# stellar mass function parameters
SMmin   = 1e9  #Msun/h
SMmax   = 5e11 #Msun/h
SM_bins = 10

# SO properties
cell_size = 3.0 #Mpc/h maximum radius of a halo (for sorting in a grid)
########################################################################################

# define here an array with all the different realizations
numbers = []
for i in range(1000):  numbers.append('LH_%s'%i)   #LH set
for i in range(1,66):    numbers.append('1P_%s'%i)   #1P set
for i in range(27):    numbers.append('CV_%s'%i)   #CV set
for i in range(4):     numbers.append('EX_%s'%i)   #EX set
numbers = np.array(numbers)

# do a loop over the N-body sims
for sim in ['SIMBA_DM', 'IllustrisTNG_DM']:

    # get the realizations each cpu works on
    indexes      = np.where(np.arange(numbers.shape[0])%nprocs==myrank)[0]
    realizations = numbers[indexes]

    # do a loop over the different realizations
    for i in realizations:
        
        # see if simulation exists
        print(sim,i)
        root_in = '%s/Sims/%s/%s'%(root,sim,i)
        files = glob.glob('%s/*'%root_in)
        if len(files)==0:  continue

        ################# power spectra ###################
        root_out = '%s/Results/Pk/%s/%s'%(root,sim,i)
        if not(os.path.exists(root_out)):  os.makedirs(root_out)
        
        # initial conditions
        snapshot = '%s/Sims/%s/%s/ICs/ics'%(root,sim,i)
        CL.compute_Pk_ICs(snapshot, grid, MAS, threads, [0,1,4,5], root_out)

        # different snapshots
        for snapnum in np.arange(34):
            snapshot = '%s/Sims/%s/%s/snap_%03d.hdf5'%(root,sim,i,snapnum)
            CL.compute_Pk(snapshot, grid, MAS, threads, [0,1,4,5], root_out)
        ###################################################

# do a loop over the different simulations
for sim in sims:

    # get the realizations each cpu works on
    indexes      = np.where(np.arange(numbers.shape[0])%nprocs==myrank)[0]
    realizations = numbers[indexes]

    # do a loop over the different realizations
    for i in realizations:

        # see if simulation exists
        print(sim,i)
        root_in = '%s/Sims/%s/%s'%(root,sim,i)
        files = glob.glob('%s/*'%root_in)
        if len(files)==0:  continue

        ################# power spectra ###################
        root_out = '%s/Results/Pk/%s/%s'%(root,sim,i)
        if not(os.path.exists(root_out)):  os.makedirs(root_out)
        
        # initial conditions
        snapshot = '%s/Sims/%s/%s/ICs/ics'%(root,sim,i)
        CL.compute_Pk_ICs(snapshot, grid, MAS, threads, [0,1,4,5], root_out)

        # different snapshots
        for snapnum in np.arange(34):
            snapshot = '%s/Sims/%s/%s/snap_%03d.hdf5'%(root,sim,i,snapnum)
            CL.compute_Pk(snapshot, grid, MAS, threads, [0,1,4,5], root_out)
            CL.compute_Pk(snapshot, grid, MAS, threads, [0],       root_out)
            CL.compute_Pk(snapshot, grid, MAS, threads, [1],       root_out)
            CL.compute_Pk(snapshot, grid, MAS, threads, [4],       root_out)
            CL.compute_Pk(snapshot, grid, MAS, threads, [5],       root_out)
        ###################################################

        ################ Pk_hydro/Pk_Nbody ################
        root_out = '%s/Results/Pk_ratio/%s/%s'%(root,sim,i)
        if not(os.path.exists(root_out)):  os.makedirs(root_out)
        
        for snapnum in np.arange(34): 
            CL.compute_Pk_ratio(root, sim, i, snapnum, root_out)
        ###################################################

        ########### halo reduced mass function ############
        root_out = '%s/Results/HMF/%s/%s'%(root,sim,i)
        if not(os.path.exists(root_out)):  os.makedirs(root_out)

        # only z=0 for the time being
        snapnum = 33 
        
        snapshot  = '%s/Sims/%s/%s/snap_%03d'%(root,sim,i,snapnum)
        f_subfind = '%s/Sims/%s/%s/fof_subhalo_tab_%03d.hdf5'%(root,sim,i,snapnum)
        CL.halo_mass_function(RMmin, RMmax, RM_bins, f_subfind, snapshot, root_out)
        ###################################################

        ############### baryon fraction ###################
        # only z=0 for the time being
        snapnum   = 33 
        redshift  = 0.0
        snapshot  = '%s/Sims/%s/%s/snap_%03d'%(root,sim,i,snapnum)
        f_subfind = '%s/Sims/%s/%s/fof_subhalo_tab_%03d.hdf5'%(root,sim,i,snapnum)
        f_SO      = '%s/Results/SO/%s/%s/SO_z=%.2f.txt'%(root,sim,i,redshift)

        root_out = '%s/Results/baryon_fraction/%s/%s'%(root,sim,i)
        if not(os.path.exists(root_out)):  os.makedirs(root_out)
        CL.baryon_fraction_FoF(RMmin, RMmax, RM_bins, f_subfind, snapshot, root_out)

        root_out = '%s/Results/baryon_fraction_SO/%s/%s'%(root,sim,i)
        if not(os.path.exists(root_out)):  os.makedirs(root_out)
        CL.baryon_fraction_SO(RMmin, RMmax, RM_bins, f_SO, snapshot, root_out)
        ###################################################

        ######### star-formation rate history #############
        root_out = '%s/Results/SFRH/%s/%s'%(root,sim,i)
        if not(os.path.exists(root_out)):  os.makedirs(root_out)

        f_sfrh = '%s/Sims/%s/%s/sfr.txt'%(root,sim,i)
        CL.star_formation_rate_history(f_sfrh, z_min, z_max, sfrh_bins, BoxSize, root_out)
        ###################################################

        ############ stellar mass function ################
        root_out = '%s/Results/SMF/%s/%s'%(root,sim,i)
        if not(os.path.exists(root_out)):  os.makedirs(root_out)

        f_subfind = '%s/Sims/%s/%s/fof_subhalo_tab_%03d.hdf5'%(root,sim,i,snapnum)
        CL.stellar_mass_function(SMmin, SMmax, SM_bins, f_subfind, root_out)
        ###################################################

        ################# SO properties ###################
        root_out = '%s/Results/SO/%s/%s'%(root,sim,i)
        if not(os.path.exists(root_out)):  os.makedirs(root_out)

        snapshot  = '%s/Sims/%s/%s/snap_%03d.hdf5'%(root,sim,i,snapnum)
        f_subfind = '%s/Sims/%s/%s/fof_subhalo_tab_%03d.hdf5'%(root,sim,i,snapnum)
        CL.SO_properties(snapshot, f_subfind, cell_size, root_out)
        ###################################################

        ################ galaxy properties ################
        root_out  = '%s/Results'%root
        f_subfind = '%s/Sims/%s/%s/fof_subhalo_tab_%03d.hdf5'%(root,sim,i,snapnum)
        CL.properties_vs_SM(SMmin, SMmax, SM_bins, f_subfind, root_out, sim, i)
        ###################################################

