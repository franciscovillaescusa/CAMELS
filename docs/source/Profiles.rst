Profiles
=============

For each snapshots, we provide three-dimensional spherically-averaged profiles of gas density, thermal pressure, gas mass-weighted temperature, and gas mass-weighted metallicity for the 1P, LH, and CV runs for both IllustrisTNG and SIMBA.  

Specifically, we use `illstack_CAMELS <https://github.com/emilymmoser/illstack_CAMELS>`_, a CAMELS-specific version  of the original, more general code `illstack <https://github.com/marcelo-alvarez/illstack>`_ to generate the three-dimensional profiles, extending radially from 0.01-10 comoving Mpc in 25 log10 bins. The profiles are stored in hdf5 format which can be read with the python script provided in the repository.

The profiles are located in

``Profiles/suite/sim/suite_sim_0##.hdf5``

where ``suite`` is either ``IllustrisTNG`` or ``SIMBA``, ``sim`` is the simulation of interest, e.g. ``1P_0``, ``LH_42``, ``CV_130``, and ``0##`` is the snapshot number, ranging from ``000`` to ``033``. 

Below is an example python script for extracting the profile data from the hdf5 file: 

.. code::  python

  import matplotlib.pyplot as plt 
  import numpy             as np
  import profile_functions
  import h5py
 
  #-------------------------input section---------------
  suite='SIMBA'
  sim='1P_0'
  snap='024'
  #------------- --------------------------------------- 
  data_dir='/mnt/ceph/users/camels/PUBLIC_RELEASE/Sims'
  prof_dir='/mnt/home/elau/ceph/illstack_CAMELS/Profiles/'

  Zsun = 0.0127
  
  def extract(simulation,snap):
      data_file= data_dir+'/'+suite+'/'+simulation+'/snap_'+snap+'.hdf5'
      profile_file = prof_dir+'/'+suite+'/'+simulation+'/'+suite+'_'+simulation+'_'+snap+'.hdf5'
      b=h5py.File(data_file,'r')
      z=b['/Header'].attrs[u'Redshift']
      stacks=h5py.File(profile_file,'r')
      val            = stacks['Profiles']
      val_dens       = np.array(val[0,:,:]) #density 
      val_pres       = np.array(val[1,:,:]) #thermal pressure
      val_metals_mw  = np.array(val[2,:,:])/Zsun #mass-weighted metallicity in solar units
      val_temp_mw    = np.array(val[3,:,:]) #mass-weighted temperature in keV
      bins           = np.array(stacks['nbins']) #number of radial bins
      r              = np.array(stacks['r'])/1.e3 #radial bins in Mpc/h
      nprofs         = np.array(stacks['nprofs']) #number of halos
      mh             = np.array(stacks['Group_M_Crit200'])*1e10 #M200c in Msol/h
      rh             = np.array(stacks['Group_R_Crit200'])/1.e3 #R200c in Mpc/h
      
      return z,r,val_dens,val_pres,val_temp_mw, val_metals_mw, mh, rh

  z,r,val_dens,val_pres,val_temp_mw, val_metals_mw, mh, rh = extract(sim,snap)
  print(r,val_dens,val_pres,val_metals_mw,val_temp_mw)

