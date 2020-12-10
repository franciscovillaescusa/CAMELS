# This script computes the mean and standard deviation of the different statistics
import numpy as np
import sys,os
import camel_library as CL

#################################### INPUT ########################################
root = '/mnt/ceph/users/camels'

# Power spectrum parameters
z_Pk = 0.0

# Halo mass function parameters
RMmin   = 1e10 #Msun/h
RMmax   = 1e14 #Msun/h
RM_bins = 30
z_HMF   = 0.0

# star-formation rate history parameters
z_min     = 0.0
z_max     = 10.0
sfrh_bins = 10000

# stellar mass function parameters
SMmin   = 1e9  #Msun/h
SMmax   = 5e11 #Msun/h
SM_bins = 10
z_SM    = 0.0

# halo temperature parameters
Mmin_T = 1e12
Mmax_T = 1e14
bins_T = 10
z_T    = 0.0

# galaxy radii parameters
SMmin_R   = 1e9  #Msun/h
SMmax_R   = 5e11 #Msun/h
SM_bins_R = 10
snapnum_R = 33
###################################################################################

# define the array with the realizations
#realizations = np.arange(1000)
numbers = []
for i in range(1000): numbers.append('LH_%s'%i)   #CV set
realizations = np.array(numbers)
sim_set      = 'LH'

#numbers = []
#for i in range(27): numbers.append('CV_%s'%i)   #CV set
#realizations = np.array(numbers)
#sim_set = 'CV'

# do a loop over the two hydro sets
for model in ['SIMBA','IllustrisTNG']:

    """
    # Pk
    root_Pk = '%s/Results/Pk'%root
    first, second = 0, 1
    for suffix in ['m', 'c', 'g', 's', 'bh']:
        name = 'Pk_%s_z=%.2f.txt'%(suffix, z_Pk)
        fout = '%s/%s/mean_%s_%s'%(root_Pk, model, sim_set, name)
        CL.mean_std(root_Pk, model, name, realizations,first,second,fout,verbose=True)

    # Pk_hydro / Pk_Nbody
    root_Pkratio = '%s/Results/Pk_ratio'%root
    first, second = 0, 1
    name = 'Pk_ratio_m_z=%.2f.txt'%z_Pk
    fout = '%s/%s/mean_%s_%s'%(root_Pkratio, model, sim_set, name)
    CL.mean_std(root_Pkratio, model, name, realizations,first,second,fout,verbose=True)

    # HMF
    root_HMF = '%s/Results/HMF'%root
    first, second = 1, 2
    name = 'mass_function_%.2e_%.2e_%d_z=%.2f.txt'%(RMmin,RMmax,RM_bins,z_HMF)
    fout = '%s/%s/mean_%s_%s'%(root_HMF, model, sim_set, name)
    CL.mean_std(root_HMF, model, name, realizations, first, second, fout, verbose=True)

    # baryon fraction FoF
    root_bf = '%s/Results/baryon_fraction'%root
    first, second = 0, 1
    name = 'bf_%.2e_%.2e_%d_z=%.2f.txt'%(RMmin, RMmax, RM_bins, z_HMF)
    fout = '%s/%s/mean_%s_%s'%(root_bf, model, sim_set, name)
    CL.mean_std(root_bf, model, name, realizations, first, second, fout, verbose=True)

    # baryon fraction SO
    root_bf = '%s/Results/baryon_fraction_SO'%root
    first, second = 0, 1
    name = 'bf_SO_%.2e_%.2e_%d_z=%.2f.txt'%(RMmin, RMmax, RM_bins, z_HMF)
    fout = '%s/%s/mean_%s_%s'%(root_bf, model, sim_set, name)
    CL.mean_std(root_bf, model, name, realizations, first, second, fout, verbose=True)

    # gas fraction SO
    root_gf = '%s/Results/baryon_fraction_SO'%root
    first, second = 0, 1
    name = 'gf_SO_%.2e_%.2e_%d_z=%.2f.txt'%(RMmin, RMmax, RM_bins, z_HMF)
    fout = '%s/%s/mean_%s_%s'%(root_gf, model, sim_set, name)
    CL.mean_std(root_gf, model, name, realizations, first, second, fout, verbose=True)

    # SFRH
    root_SFRH = '%s/Results/SFRH'%root
    name = 'SFRH_%.2f_%.2f_%d.txt'%(z_min, z_max, sfrh_bins)
    fout = '%s/%s/mean_%s_%s'%(root_SFRH, model, sim_set, name)
    first, second = 0, 1
    CL.mean_std(root_SFRH, model, name, realizations, first, second, fout,verbose=True)

    # SMF
    root_SMF = '%s/Results/SMF'%root
    name = 'SMF_%.2e_%2.e_%d_z=%.2f.txt'%(SMmin, SMmax, SM_bins, z_SM)
    fout = '%s/%s/mean_%s_%s'%(root_SMF, model, sim_set, name)
    first, second = 0, 1
    CL.mean_std(root_SMF, model, name, realizations, first, second, fout, verbose=True)

    # halos temperature
    root_T = '%s/Results/SO'%root
    name = 'SO_z=%.2f.txt'%(z_T)
    fout = '%s/%s/mean_T_%s_%.2e_%.2e_%d_z=%.2f.txt'%(root_T, model, sim_set, 
                                                      Mmin_T, Mmax_T, bins_T, z_T)
    CL.mean_std_T(root_T, model, name, realizations, Mmin_T, Mmax_T, bins_T, 
                  fout, verbose=False)
    """
    # radii, black hole mass, metallicity & Vmax
    root_R   = '%s/Sims'%root
    name     = 'fof_subhalo_tab_%03d.hdf5'%snapnum_R
    fout_R   = '%s/Results/Radii/%s/mean_R_vs_SM_%s_z=0.00.txt'%(root,model,sim_set)
    fout_BH  = '%s/Results/BH/%s/mean_BH_vs_SM_%s_z=0.00.txt'%(root,model,sim_set)
    fout_SFR = '%s/Results/SFR/%s/mean_SFR_vs_SM_%s_z=0.00.txt'%(root,model,sim_set)
    fout_V   = '%s/Results/Vmax/%s/mean_V_vs_SM_%s_z=0.00.txt'%(root,model,sim_set)
    CL.mean_std_SM(root_R, model, name, realizations, SMmin_R, SMmax_R, SM_bins_R, 
                   fout_R, fout_BH, fout_SFR, fout_V, verbose=False)

# do a loop over the two N-body
#for model in ['SIMBA_DM', 'IllustrisTNG_DM']:

