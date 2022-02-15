.. _profiles:

*******************
CAMELS CGM Profiles
*******************

The folder ``Profiles`` contains the CGM profiles. The data is organized following the general hierarchical structure described in :ref:`suite_folders`.

For each snapshot of each simulation, we provide three-dimensional spherically-averaged profiles of gas density, thermal pressure, gas mass-weighted temperature, and gas mass-weighted metallicity for the simulations of the 1P, LH, and CV sets of both the IllustrisTNG and SIMBA suites. 

Specifically, we use `illstack_CAMELS <https://github.com/emilymmoser/illstack_CAMELS>`_, a CAMELS-specific version  of the original, more general code `illstack <https://github.com/marcelo-alvarez/illstack>`_ to generate the three-dimensional profiles, extending radially from 0.01-10 Mpc in 25 log10 bins. The profiles are stored in hdf5 format which can be read with the python script provided in the repository.

The profiles are located as

``Profiles/suite/sim/suite_sim_0##.hdf5``

where ``suite`` is either ``IllustrisTNG`` or ``SIMBA``, ``sim`` is the simulation of interest, e.g. ``1P_4_n5``, ``LH_42``, ``CV_130``, and ``0##`` is the snapshot number, ranging from ``000`` to ``033``. 

Below is an example python script for extracting the profile data from the hdf5 file: 

.. code::  python

  import matplotlib.pyplot as plt 
  import numpy             as np
  import h5py
 
  #-------------------------input section---------------
  suite='SIMBA'
  sim='CV_0'
  snap='024'
  #----------------------------------------------------- 
  data_dir='/mnt/ceph/users/camels/PUBLIC_RELEASE/Sims'
  prof_dir='/mnt/home/elau/ceph/illstack_CAMELS/Profiles/'

  def extract(simulation,snap):
  
      '''
      Return values of the CGM profiles from the CAMELS simulation
      
      Inputs: 
        simulation: string, name of the simulation, e.g., 1P_5_2, LH_123, CV_12
        snap: string, number of the snapshot, from '000' to '033', '033' being the last snapshot corresponding to z=0
        
      Outputs:
        z: float, redshift
        r: np array, radial bin on kpc
        val_dens: np array, density profile in g/cm^3
        val_pres: np array, volume-weighted thermal pressure profile in erg/cm^3
        val_temp_mw: np array, mass-weighted temperature in K
        val_metals_mw: np array, mass-weighted metallcity in Zsun
        mh: np array, halo mass (M200c) in Msun
        rh: np array, halo radius (R200c) in kpc
      
      '''
  
      h=0.6711
      omegab=0.049
      omegam,sigma8=np.loadtxt(data_dir+'/'+suite+'/'+simulation+'/CosmoAstro_params.txt',usecols=(1,2),unpack=True)
      omegalam=1.0-omegam
      
      kb = 1.38e-16 # erg/K
      erg_to_keV = 6.242e+8
      K_to_keV = kb * erg_to_keV
      m_e = 9.11e-28 # electron mass in g
      m_p = 1.6726e-24 # in g
      XH = 0.76 #primordial hydrogen fraction
      mu = 0.58824; # X=0.76 assumed
      mu_e = mue = 2.0/(1.0+XH); # X=0.76 assumed
      Msun = 1.989e33 
      kpc = 3.0856e21

      data_file= data_dir+'/'+suite+'/'+simulation+'/snap_'+snap+'.hdf5'
      profile_file = prof_dir+'/'+suite+'/'+simulation+'/'+suite+'_'+simulation+'_'+snap+'.hdf5'
      b=h5py.File(data_file,'r')
      z=b['/Header'].attrs[u'Redshift']

      comoving_factor = (1.0+z)

      density_conversion_factor = Msun*kpc**(-3) * 1e10 * h**2 * comoving_factor**3
      #from 1e10Msol/h*(km/s)**2 ckpc^{-3} to keV cm^{-3}
      pressure_conversion_factor = density_conversion_factor * 1e10 * erg_to_keV
      temperature_conversion_factor = (1e5)**2 * kb * erg_to_keV
    
      stacks=h5py.File(profile_file,'r')
      val            = stacks['Profiles']
      val_dens       = np.array(val[0,:,:]) * density_conversion_factor #density in g cm^3
      val_pres       = np.array(val[1,:,:]) * pressure_conversion_factor  #thermal pressure in keV cm^-3
      val_metals_mw  = np.array(val[2,:,:])/Zsun #mass-weighted metallicity in solar units
      val_temp_mw    = np.array(val[3,:,:]) * temperature_conversion_factor #mass-weighted temperature in keV
      bins           = np.array(stacks['nbins']) #number of radial bins
      r              = np.array(stacks['r']) / h / comoving_factor #radial bins in comoving kpc
      nprofs         = np.array(stacks['nprofs']) #number of halos
      m200c          = np.array(stacks['Group_M_Crit200'])*1e10 / h #M200c in Msol
      r200c          = np.array(stacks['Group_R_Crit200']) / h / comoving_factor #R200c in kpc
      
      return z, r, val_dens, val_pres, val_temp_mw, val_metals_mw, m200c, r200c
