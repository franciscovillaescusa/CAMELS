from mpi4py import MPI
import numpy as np
import sys,os
import camb

###### MPI DEFINITIONS ######                                    
comm   = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm.Get_rank()

#################################### INPUT #############################################
root_out = '/simons/scratch/fvillaescusa/CAMELS/Sims/IllustrisTNG'

dimensions = 6
points     = 27

# CAMB parameters
Omega_b      = 0.049
h            = 0.6711
ns           = 0.9624
hierarchy    = 'degenerate'
Mnu          = 0.0 #eV
Nnu          = 0   #number of massive neutrinos
Neff         = 3.046
As           = 2.13e-9
tau          = None
Omega_k      = 0.0
pivot_scalar = 0.05
pivot_tensor = 0.05
kmax         = 200.0
k_per_logint = 20
redshifts    = [0]
########################################################################################

# generate the parameters
params = np.zeros((points,dimensions), dtype=np.float64)

# set fiducial values
params[:,0] = 0.3
params[:,1] = 0.8
params[:,2] = 1.0
params[:,3] = 1.0
params[:,4] = 1.0
params[:,5] = 1.0

# get the numbers each cpu will work on
numbers = np.where(np.arange(points)%nprocs==myrank)[0]

# do a loop over all the points in the latin hypercube
for i in numbers:

    # create output folder in case it does not exists
    folder = '%s/1505_%d/'%(root_out,i)
    if not(os.path.exists(folder)):  os.system('mkdir %s'%folder)

    # create initial conditions folder if it does not exists
    folder_ICs = '%s/ICs'%(folder) 
    if not(os.path.exists(folder_ICs)):  os.system('mkdir %s'%folder_ICs)

    # find the values of the cosmological parameters
    Omega_m = params[i,0]
    s8      = params[i,1]
    astro1  = params[i,2]
    astro2  = params[i,3]
    astro3  = params[i,4]
    astro4  = params[i,5]

    g = open('%s/CosmoAstro_params.txt'%folder, 'w')
    g.write('%.5f %.5f %.5f %.5f %.5f %.5f\n'\
            %(Omega_m, s8, astro1, astro2, astro3, astro4))
    g.close()

    print('realization %d'%i)
    print('Omega_m = %.5f'%Omega_m)
    print('s8      = %.5f'%s8)
    print('Astro1  = %.5f'%astro1)
    print('Astro2  = %.5f'%astro2)
    print('Astro3  = %.5f'%astro3)
    print('Astro4  = %.5f'%astro4)

    ##### run CAMB #####
    Omega_c  = Omega_m - Omega_b
    pars     = camb.CAMBparams()

    # set accuracy of the calculation
    pars.set_accuracy(AccuracyBoost=4.0, lSampleBoost=4.0, lAccuracyBoost=4.0, 
                      HighAccuracyDefault=True, DoLateRadTruncation=True)

    # set value of the cosmological parameters
    pars.set_cosmology(H0=h*100.0, ombh2=Omega_b*h**2, omch2=Omega_c*h**2, 
                       mnu=Mnu, omk=Omega_k, neutrino_hierarchy=hierarchy, 
                       num_massive_neutrinos=Nnu, nnu=Neff, tau=tau)
                   
    # set the value of the primordial power spectrum parameters
    pars.InitPower.set_params(As=As, ns=ns, 
                              pivot_scalar=pivot_scalar, pivot_tensor=pivot_tensor)

    # set redshifts, k-range and k-sampling
    pars.set_matter_power(redshifts=redshifts, kmax=kmax, k_per_logint=k_per_logint)

    # compute results
    results = camb.get_results(pars)

    # save parameter values to file
    f = open('%s/CAMB.params'%folder_ICs,'w');  f.write('%s'%pars);  f.close()

    # interpolate to get Pmm, Pcc...etc
    k, zs, Pkmm = results.get_matter_power_spectrum(minkh=2e-5, maxkh=kmax, 
                                                    npoints=400, var1=7, var2=7, 
                                                    have_power_spectra=True, 
                                                    params=None)

    # do a loop over all redshifts
    for j,z in enumerate(zs):
        fout = '%s/Pk_m_z=%.3f.txt'%(folder_ICs,z)
        np.savetxt(fout, np.transpose([k,Pkmm[j,:]]))




    ########################## write 2LPT parameter file #######################
    # parameter file for standard simulations
    a="""
    Nmesh            512
    Nsample          256       
    Box              25000.0   
    FileBase         ics         
    OutputDir        ./
    GlassFile        /simons/scratch/fvillaescusa/CAMELS/Codes/2lpt/GLASS/dummy_glass_CDM_B_64_64.dat   
    GlassTileFac     4         
    Omega            %.4f    
    OmegaLambda      %.4f    
    OmegaBaryon      0.049    
    OmegaDM_2ndSpecies  0.0    
    HubbleParam      0.6711    
    Redshift         127       
    Sigma8           %.4f       
    SphereMode       0         
    WhichSpectrum    2         
    FileWithInputSpectrum   ./Pk_m_z=0.000.txt
    InputSpectrum_UnitLength_in_cm  3.085678e24 
    ShapeGamma       0.201     
    PrimordialIndex  1.0       
    
    Phase_flip          0      
    RayleighSampling    1      
    Seed                %d      
    
    NumFilesWrittenInParallel 8  
    UnitLength_in_cm          3.085678e21  
    UnitMass_in_g             1.989e43     
    UnitVelocity_in_cm_per_s  1e5          
    
    WDM_On               0      
    WDM_Vtherm_On        0      
    WDM_PartMass_in_kev  10.0   
    """%(Omega_m, 1.0-Omega_m, s8, i+1)

    # save parameters to file                                    
    f = open('%s/2LPT.param'%folder_ICs, 'w');  f.write(a);  f.close()

