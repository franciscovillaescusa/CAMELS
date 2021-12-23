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
 
  data_dir='/mnt/ceph/users/camels/PUBLIC_RELEASE/Sims'
  prof_dir='/mnt/home/elau/ceph/illstack_CAMELS/Profiles/'
  #-----------------------------------input section
  suite='SIMBA'
  sim='1P_0'
  snap='024'
  #--------------------------------------------------------------- 


  def extract(simulation,snap):
      data_file= data_dir+'/'+suite+'/'+simulation+'/snap_'+snap+'.hdf5'
      profile_file = prof_dir+'/'+suite+'_'+simulation+'_'+snap+'.hdf5'
      b=h5py.File(data_file,'r')
      z=b['/Header'].attrs[u'Redshift']
      stacks=h5py.File(profile_file,'r')
      val            = stacks['Profiles']
      val_dens       = np.array(val[0,:,:])
      val_pres       = np.array(val[1,:,:])
      bins           = np.array(stacks['nbins'])
      r              = np.array(stacks['r'])
      nprofs         = np.array(stacks['nprofs'])
      mh             = np.array(stacks['Group_M_Crit200']) #units 1e10 Msol/h, M200c
      rh             = np.array(stacks['Group_R_Crit200']) #R200c
      
      r_mpc=r/1.e3
      
      return z,val_dens,bins,r,val_pres,nprofs,mh,rh

  z,val_dens,bins,r,val_pres,nprofs,mh,rh=extract(sim,snap)
  
