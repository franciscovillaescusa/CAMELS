Profiles
=============

For each snapshot, we provide three-dimensional spherically-averaged profiles of gas density, thermal pressure, gas mass-weighted temperature, and gas mass-weighted metallicity for the 1P, LH, and CV runs for both IllustrisTNG and SIMBA.  

Specifically, we use `illstack_CAMELS <https://github.com/emilymmoser/illstack_CAMELS>`_, a CAMELS-specific version  of the original, more general code `illstack <https://github.com/marcelo-alvarez/illstack>`_ to generate the three-dimensional profiles, extending radially from 0.01-10 comoving Mpc in 25 log10 bins. The profiles are stored in hdf5 format which can be read with the python script provided in the repository.

The profiles are located in

``Profiles/suite/sim/suite_sim_0##.hdf5``

where ``suite`` is either ``IllustrisTNG`` or ``SIMBA``, ``sim`` is the simulation of interest, e.g. ``1P_0``, ``LH_42``, ``CV_130``, and ``0##`` is the snapshot number, ranging from ``000`` to ``033``. 

Below is an example python script for extracting the profile data from the hdf5 file: 

.. code::  python

  import matplotlib.pyplot as plt 
  import numpy             as np
  import h5py
 
  #-------------------------input section---------------
  suite='SIMBA'
  sim='1P_0'
  snap='024'
  #------------- --------------------------------------- 
  data_dir='/mnt/ceph/users/camels/PUBLIC_RELEASE/Sims'
  prof_dir='/mnt/home/elau/ceph/illstack_CAMELS/Profiles/'

  Zsun = 0.0127
  Msun = 1.99e33 #g cm^-3
  kpc = 3.086e21 #cm
  
  def extract(simulation,snap):
  
      '''
      Return values of the CGM profiles from the CAMELS simulation
      
      Inputs: 
        simulation: string, name of the simulation, e.g., 1P_0, LH_123, CV_12
        snap: sting, number of the snapshot, from '000' to '033', '033' being the last snapshot corresponding to z=0
        
      Outputs:
        z: float, redshift
        r: radial bin on kpc
        val_dens: density profile in g/cm^3
        val_pres: volume-weighted thermal pressure profile in erg/cm^3
        val_temp_mw: mass-weighted temperature in K
        val_metals_mw: mass-weighted metallcity in Zsun
        mh: halo mass (M200c) in Msun
        rh: halo radius (R200c) in kpc
      
      '''
  
      h=0.6711
      omegab=0.049
      omegam,sigma8=np.loadtxt(data_dir+'/'+suite+'/'+simulation+'/CosmoAstro_params.txt',usecols=(1,2),unpack=True)
      omegalam=1.0-omegam
      
      density_to_cgs = Msun*kpc**(-3)
      pressure_to_cgs = density_to_cgs*1e10

      data_file= data_dir+'/'+suite+'/'+simulation+'/snap_'+snap+'.hdf5'
      profile_file = prof_dir+'/'+suite+'/'+simulation+'/'+suite+'_'+simulation+'_'+snap+'.hdf5'
      b=h5py.File(data_file,'r')
      z=b['/Header'].attrs[u'Redshift']

      stacks=h5py.File(profile_file,'r')
      val            = stacks['Profiles']
      val_dens       = np.array(val[0,:,:]) * 1e10 * h**2 * comoving_factor**3 #density in Msun kpc^-3
      val_pres       = np.array(val[1,:,:]) * 1e10 * h**2 / (3.086e16*3.086e16) * comoving_factor**3 #thermal pressure in Msun kpc^-3 (km/s)^2
      val_metals_mw  = np.array(val[2,:,:])/Zsun #mass-weighted metallicity in solar units
      val_temp_mw    = np.array(val[3,:,:])*1e10 #mass-weighted temperature in K
      bins           = np.array(stacks['nbins']) #number of radial bins
      r              = np.array(stacks['r']) / h / comoving_factor #radial bins in comoving kpc
      nprofs         = np.array(stacks['nprofs']) #number of halos
      mh             = np.array(stacks['Group_M_Crit200'])*1e10 / h #M200c in Msol
      rh             = np.array(stacks['Group_R_Crit200']) / h / comoving_factor #R200c in kpc
      
      val_dens *= density_to_cgs # density in g cm^-3
      val_pres *= pressure_to_cgs # pressure in erg cm^-3
      
      return z, r, val_dens, val_pres, val_temp_mw, val_metals_mw, mh, rh

  z,r,val_dens,val_pres,val_temp_mw, val_metals_mw, mh, rh = extract(sim,snap)
  print(r,val_dens,val_pres,val_metals_mw,val_temp_mw)

