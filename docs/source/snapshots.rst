.. _snapshots:

***********
Simulations
***********

The ``Sims`` folder contains the raw data from all CAMELS simulations. The data is organized following the general hierarchical structure described in :ref:`suite_folders`. We however repeat it here for clarity:

The ``Sims`` folder contains four different `suite folders`:

- ``IllustrisTNG``. This folder contains all simulations of the IllustrisTNG suite.
- ``IllustrisTNG_DM``. This folder contains all the N-body simulations corresponding the IllustrisTNG suite.
- ``SIMBA``. This folder contains all simulations of the SIMBA suite. 
- ``SIMBA_DM``. This folder contains all the N-body simulations corresponding the SIMBA suite.
- ``Astrid``. This folder contains all simulations of the Astrid suite. 
- ``Astrid_DM``. This folder contains all the N-body simulations corresponding the Astrid suite.

.. Note::
  
   The value of the cosmological, astrophysical, and initial random seed for simulations in the different suites can be found in :ref:`params`. Those files also hold for the N-body simulations; each N-body simulation has the same value of the cosmological parameters and initial random seed as their hydrodynamic counterpart.

Suite folders
~~~~~~~~~~~~~
  
Inside each `suite folder` there are `simulation folders` from all available simulations, e.g.

.. code-block:: bash

   >> ls Sims/IllustrisTNG
   EX_1    LH_146  LH_197  LH_247  LH_298  LH_348  LH_399  LH_449  LH_5    LH_55   LH_60   LH_650  LH_700  LH_751  LH_801  LH_852  LH_902  LH_953
   EX_2    LH_147  LH_198  LH_248  LH_299  LH_349  LH_4    LH_45   LH_50   LH_550  LH_600  LH_651  LH_701  LH_752  LH_802  LH_853  LH_903  LH_954
   EX_3    LH_148  LH_199  LH_249  LH_3    LH_35   LH_40   LH_450  LH_500  LH_551  LH_601  LH_652  LH_702  LH_753  LH_803  LH_854  LH_904  LH_955
   LH_0    LH_149  LH_2    LH_25   LH_30   LH_350  LH_400  LH_451  LH_501  LH_552  LH_602  LH_653  LH_703  LH_754  LH_804  LH_855  LH_905  LH_956
   LH_1    LH_15   LH_20   LH_250  LH_300  LH_351  LH_401  LH_452  LH_502  LH_553  LH_603  LH_654  LH_704  LH_755  LH_805  LH_856  LH_906  LH_957
   LH_10   LH_150  LH_200  LH_251  LH_301  LH_352  LH_402  LH_453  LH_503  LH_554  LH_604  LH_655  LH_705  LH_756  LH_806  LH_857  LH_907  LH_958
   LH_100  LH_151  LH_201  LH_252  LH_302  LH_353  LH_403  LH_454  LH_504  LH_555  LH_605  LH_656  LH_706  LH_757  LH_807  LH_858  LH_908  LH_959
   LH_101  LH_152  LH_202  LH_253  LH_303  LH_354  LH_404  LH_455  LH_505  LH_556  LH_606  LH_657  LH_707  LH_758  LH_808  LH_859  LH_909  LH_96
   LH_102  LH_153  LH_203  LH_254  LH_304  LH_355  LH_405  LH_456  LH_506  LH_557  LH_607  LH_658  LH_708  LH_759  LH_809  LH_86   LH_91   LH_960
   LH_103  LH_154  LH_204  LH_255  LH_305  LH_356  LH_406  LH_457  LH_507  LH_558  LH_608  LH_659  LH_709  LH_76   LH_81   LH_860  LH_910  LH_961
   LH_104  LH_155  LH_205  LH_256  LH_306  LH_357  LH_407  LH_458  LH_508  LH_559  LH_609  LH_66   LH_71   LH_760  LH_810  LH_861  LH_911  LH_962
   LH_105  LH_156  LH_206  LH_257  LH_307  LH_358  LH_408  LH_459  LH_509  LH_56   LH_61   LH_660  LH_710  LH_761  LH_811  LH_862  LH_912  LH_963
   LH_106  LH_157  LH_207  LH_258  LH_308  LH_359  LH_409  LH_46   LH_51   LH_560  LH_610  LH_661  LH_711  LH_762  LH_812  LH_863  LH_913  LH_964
   ...
   
- ``1P_X_Y``. These folders contain the data from 1P simulations. ``X`` ranges from ``1`` to ``6`` while ``Y`` goes from ``n5`` (-5) to ``5``.
- ``CV_X``. These folders contain the simulations of the CV set. X goes from 0 to 26.
- ``EX_X``. These folders contain the simulations of the EX set. X goes from 0 to 3.
- ``LH_X``. These folders contain the simulations of the LH set. X goes from 0 to 999.
- ``CosmoAstroSeed_params.txt``. This file contains the value of the cosmological and astrophysical parameter, together with the value of the random seed, for each simulation in the suite. The format of the file is: simulation_name :math:`\Omega_{\rm m}`  :math:`\sigma_8`  :math:`A_{\rm SN1}`  :math:`A_{\rm AGN1}`  :math:`A_{\rm SN2}`  :math:`A_{\rm AGN2}` seed.

See :ref:`simulation_folders` for details about the naming of the simulations in the 1P set.
  
.. Note::

   The structure and organization of the different folders inside the ``IllustrisTNG_DM`` and ``SIMBA_DM`` is the same as in the ``IllustrisTNG`` and ``SIMBA`` folders.

Simulation folders
~~~~~~~~~~~~~~~~~~
   
Inside each simulation folder there are different files and folders, e.g.:

.. code-block:: bash

   >> ls SIMBA/LH_24
   AGBcyield_v2.tab            fofrad_004.txt  fofrad_019.txt  fof_subhalo_tab_000.hdf5  fof_subhalo_tab_015.hdf5  fof_subhalo_tab_030.hdf5  OUTPUT.err             snap_009.hdf5  snap_024.hdf5
   AGBmdot.tab                 fofrad_005.txt  fofrad_020.txt  fof_subhalo_tab_001.hdf5  fof_subhalo_tab_016.hdf5  fof_subhalo_tab_031.hdf5  OUTPUT.o24             snap_010.hdf5  snap_025.hdf5
   AGBoyield_v2.tab            fofrad_006.txt  fofrad_021.txt  fof_subhalo_tab_002.hdf5  fof_subhalo_tab_017.hdf5  fof_subhalo_tab_032.hdf5  OUTPUT.o632254         snap_011.hdf5  snap_026.hdf5
   balance.txt                 fofrad_007.txt  fofrad_022.txt  fof_subhalo_tab_003.hdf5  fof_subhalo_tab_018.hdf5  fof_subhalo_tab_033.hdf5  parameters-usedvalues  snap_012.hdf5  snap_027.hdf5
   blackhole_details           fofrad_008.txt  fofrad_023.txt  fof_subhalo_tab_004.hdf5  fof_subhalo_tab_019.hdf5  GIZMO.param               script.sh              snap_013.hdf5  snap_028.hdf5
   blackholes.txt              fofrad_009.txt  fofrad_024.txt  fof_subhalo_tab_005.hdf5  fof_subhalo_tab_020.hdf5  GIZMO.param-usedvalues    sfr.txt                snap_014.hdf5  snap_029.hdf5
   CosmoAstro_params.txt       fofrad_010.txt  fofrad_025.txt  fof_subhalo_tab_006.hdf5  fof_subhalo_tab_021.hdf5  gizmo-simba               snap_000.hdf5          snap_015.hdf5  snap_030.hdf5
   cpu.txt                     fofrad_011.txt  fofrad_026.txt  fof_subhalo_tab_007.hdf5  fof_subhalo_tab_022.hdf5  GRACKLE_INFO              snap_001.hdf5          snap_016.hdf5  snap_031.hdf5
   dust.txt                    fofrad_012.txt  fofrad_027.txt  fof_subhalo_tab_008.hdf5  fof_subhalo_tab_023.hdf5  grids                     snap_002.hdf5          snap_017.hdf5  snap_032.hdf5
   energy.txt                  fofrad_013.txt  fofrad_028.txt  fof_subhalo_tab_009.hdf5  fof_subhalo_tab_024.hdf5  ICs                       snap_003.hdf5          snap_018.hdf5  snap_033.hdf5
   ewald_spc_table_64_dbl.dat  fofrad_014.txt  fofrad_029.txt  fof_subhalo_tab_010.hdf5  fof_subhalo_tab_025.hdf5  info.txt                  snap_004.hdf5          snap_019.hdf5  spcool_tables
   fofrad_000.txt              fofrad_015.txt  fofrad_030.txt  fof_subhalo_tab_011.hdf5  fof_subhalo_tab_026.hdf5  logfile                   snap_005.hdf5          snap_020.hdf5  timebin.txt
   fofrad_001.txt              fofrad_016.txt  fofrad_031.txt  fof_subhalo_tab_012.hdf5  fof_subhalo_tab_027.hdf5  OUTPUT                    snap_006.hdf5          snap_021.hdf5  timings.txt
   fofrad_002.txt              fofrad_017.txt  fofrad_032.txt  fof_subhalo_tab_013.hdf5  fof_subhalo_tab_028.hdf5  OUTPUT.e24                snap_007.hdf5          snap_022.hdf5  TREECOOL
   fofrad_003.txt              fofrad_018.txt  fofrad_033.txt  fof_subhalo_tab_014.hdf5  fof_subhalo_tab_029.hdf5  OUTPUT.e632254            snap_008.hdf5          snap_023.hdf5  variable_wind_scaling.txt

The most relevant ones are these:

- ``ICs``. This folder contains the initial conditions of the simulations. See :ref:`ICs` for further details.

- ``snap_0XY.hdf5``. These are the simulation snapshots. Numbers go from 000 (corresponding to :math:`z=6`) to 033 (corresponding to :math:`z=0`). These files contain the positions, velocities, IDs and other properties of the dark matter particles and the fluid resolution elements of the simulation. See :ref:`snapshots` for details on how to read these files.
  
- ``fof_subhalo_tab_0XY.hdf5``. These files contain the halo/galaxy catalogues. Numbers go from 000 (corresponding to :math:`z=6`) to 033 (corresponding to :math:`z=0`). These files contain the properties of the halos and subhalos identified by SUBFIND. See :ref:`subfind` to see how to read these files.

- ``CosmoAstro_params.txt``. This file contains the value of the cosmological and astrophysical parameter of the simulation. Format is: :math:`\Omega_{\rm m}`  :math:`\sigma_8`  :math:`A_{\rm SN1}`  :math:`A_{\rm SN2}`   :math:`A_{\rm AGN1}`   :math:`A_{\rm AGN2}`.

.. _Reach out to us: camel.simulations@gmail.com
  
There are many other files in a simulation folder that we do not describe as they are barely used. `Reach out to us`_ if you need help with those.


Snapshots
~~~~~~~~~

CAMELS snapshots are stored as single hdf5 files. In order to read them in python, you will need ``h5py``. The simplest way to inspect the content of a snapshot is this:

.. code-block:: bash

   >> h5ls -r Sims/IllustrisTNG/CV_14/snap_024.hdf5
   /                        Group
   /Config                  Group
   /Header                  Group
   /Parameters              Group
   /PartType0               Group
   /PartType0/Coordinates   Dataset {15879574, 3}
   /PartType0/Density       Dataset {15879574}
   /PartType0/ElectronAbundance Dataset {15879574}
   /PartType0/EnergyDissipation Dataset {15879574}
   /PartType0/GFM_AGNRadiation Dataset {15879574}
   /PartType0/GFM_CoolingRate Dataset {15879574}
   /PartType0/GFM_Metallicity Dataset {15879574}
   /PartType0/GFM_Metals    Dataset {15879574, 10}
   /PartType0/GFM_MetalsTagged Dataset {15879574, 6}
   /PartType0/GFM_WindDMVelDisp Dataset {15879574}
   /PartType0/GFM_WindHostHaloMass Dataset {15879574}
   /PartType0/InternalEnergy Dataset {15879574}
   /PartType0/Machnumber    Dataset {15879574}
   /PartType0/MagneticField Dataset {15879574, 3}
   /PartType0/MagneticFieldDivergence Dataset {15879574}
   /PartType0/Masses        Dataset {15879574}
   /PartType0/NeutralHydrogenAbundance Dataset {15879574}
   /PartType0/ParticleIDs   Dataset {15879574}
   /PartType0/Potential     Dataset {15879574}
   /PartType0/StarFormationRate Dataset {15879574}
   /PartType0/SubfindDMDensity Dataset {15879574}
   /PartType0/SubfindDensity Dataset {15879574}
   /PartType0/SubfindHsml   Dataset {15879574}
   /PartType0/SubfindVelDisp Dataset {15879574}
   /PartType0/Velocities    Dataset {15879574, 3}
   /PartType1               Group
   /PartType1/Coordinates   Dataset {16777216, 3}
   /PartType1/ParticleIDs   Dataset {16777216}
   /PartType1/Potential     Dataset {16777216}
   /PartType1/SubfindDMDensity Dataset {16777216}
   /PartType1/SubfindDensity Dataset {16777216}
   /PartType1/SubfindHsml   Dataset {16777216}
   /PartType1/SubfindVelDisp Dataset {16777216}
   /PartType1/Velocities    Dataset {16777216, 3}
   /PartType4               Group
   /PartType4/BirthPos      Dataset {524754, 3}
   /PartType4/BirthVel      Dataset {524754, 3}
   /PartType4/Coordinates   Dataset {524754, 3}
   /PartType4/GFM_InitialMass Dataset {524754}
   /PartType4/GFM_Metallicity Dataset {524754}
   /PartType4/GFM_Metals    Dataset {524754, 10}
   /PartType4/GFM_MetalsTagged Dataset {524754, 6}
   /PartType4/GFM_StellarFormationTime Dataset {524754}
   /PartType4/GFM_StellarPhotometrics Dataset {524754, 8}
   /PartType4/Masses        Dataset {524754}
   /PartType4/ParticleIDs   Dataset {524754}
   /PartType4/Potential     Dataset {524754}
   /PartType4/SubfindDMDensity Dataset {524754}
   /PartType4/SubfindDensity Dataset {524754}
   /PartType4/SubfindHsml   Dataset {524754}
   /PartType4/SubfindVelDisp Dataset {524754}
   /PartType4/Velocities    Dataset {524754, 3}
   /PartType5               Group
   /PartType5/BH_BPressure  Dataset {1257}
   /PartType5/BH_CumEgyInjection_QM Dataset {1257}
   /PartType5/BH_CumEgyInjection_RM Dataset {1257}
   /PartType5/BH_CumMassGrowth_QM Dataset {1257}
   /PartType5/BH_CumMassGrowth_RM Dataset {1257}
   /PartType5/BH_Density    Dataset {1257}
   /PartType5/BH_HostHaloMass Dataset {1257}
   /PartType5/BH_Hsml       Dataset {1257}
   /PartType5/BH_Mass       Dataset {1257}
   /PartType5/BH_Mdot       Dataset {1257}
   /PartType5/BH_MdotBondi  Dataset {1257}
   /PartType5/BH_MdotEddington Dataset {1257}
   /PartType5/BH_Pressure   Dataset {1257}
   /PartType5/BH_Progs      Dataset {1257}
   /PartType5/BH_U          Dataset {1257}
   /PartType5/Coordinates   Dataset {1257, 3}
   /PartType5/Masses        Dataset {1257}
   /PartType5/ParticleIDs   Dataset {1257}
   /PartType5/Potential     Dataset {1257}
   /PartType5/SubfindDMDensity Dataset {1257}
   /PartType5/SubfindDensity Dataset {1257}
   /PartType5/SubfindHsml   Dataset {1257}
   /PartType5/SubfindVelDisp Dataset {1257}
   /PartType5/Velocities    Dataset {1257, 3}

As can be seen, the snapshots contain different groups and blocks:

- ``Header``. This group contains different properties of the simulations such as its box size, number of particles, value of the cosmological parameters...etc.
- ``PartType0``. This group contains the properties of the gas particles.
- ``PartType1``. This group contains the properties of the dark matter particles.
- ``PartType4``. This group contains the properties of the star particles.
- ``PartType5``. This group contains the properties of the black hole particles.

For instance, the block ``/PartType4/Coordinates`` contains the coordinates of the star particles. A detailed description of the different blocks can be found `here <https://www.tng-project.org/data/docs/specifications/#sec1b>`_.

.. Note::

   While the format of the snapshots in the IllustrisTNG and SIMBA suites is almost identical, there are a few differences. See :ref:`suite_differences` for more information.

Reading the snapshot header and blocks can be done as follows:

.. code-block:: python

   import numpy as np
   import h5py

   # snapshot name
   snapshot = 'Sims/IllustrisTNG/CV_14/snap_014.hdf5'

   # open file
   f = h5py.File(snapshot, 'r')

   # read different attributes of the header
   BoxSize      = f['Header'].attrs[u'BoxSize']/1e3 #Mpc/h
   redshift     = f['Header'].attrs[u'Redshift']
   h            = f['Header'].attrs[u'HubbleParam']
   Masses       = f['Header'].attrs[u'MassTable']*1e10 #Msun/h
   Np           = f['Header'].attrs[u'NumPart_Total']
   Omega_m      = f['Header'].attrs[u'Omega0']
   Omega_L      = f['Header'].attrs[u'OmegaLambda']
   Omega_b      = f['Header'].attrs[u'OmegaBaryon']
   scale_factor = f['Header'].attrs[u'Time'] #scale factor
   
   # read gas positions
   pos_g = f['PartType0/Coordinates'][:]/1e3  #positions in Mpc/h

   # read dark matter velocities; need to multiply by sqrt(a) to get peculiar velocities
   vel_c = f['PartType1/Velocities'][:]*np.sqrt(scale_factor) #velocities in km/s
   
   # read star masses
   mass_s = f['PartType4/Masses'][:]*1e10  #Masses in Msun/h

   # read black hole positions and the gravitational potential at their locations
   pos_bh       = f['PartType5/Coordinates'][:]/1e3  #positions in Mpc/h
   potential_bh = f['PartType5/Potential'][:]/scale_factor #potential in (km/s)^2

   
   # close file
   f.close()

.. Note::

   Note that the N-body simulations only contain the positions, velocities and IDs of the dark matter particles.


.. _ICs:   

Initial conditions
~~~~~~~~~~~~~~~~~~

The initial conditions of all simulations were generated at :math:`z=127` using second order lagrangian perturbation theory (2LPT). The same transfer function (total matter) was used for the gas and dark matter components. Particles were initially laid down in a regular grid: one grid for the dark matter particles and another grid, offset by half a grid cell, for the gas.

The initial condition files can be found inside each simulation folder. For instance, to access the initial conditions of the LH_156 simulation of the SIMBA suite:

.. code-block:: bash

   >> ls Sims/SIMBA/LH_156/ICs
   2LPT.param   ics.1  ics.4  ics.7              Pk_m_z=0.000.txt
   CAMB.params  ics.2  ics.5  inputspec_ics.txt
   ics.0        ics.3  ics.6  logIC

There are different files:

- ``2LPT.param``. This is the 2LPT parameter file used to generate the simulation initial conditions.
- ``CAMB.params``. This CAMB parameter file used to generate the :math:`z=0` matter power spectrum needed to generate the initial conditions.
- ``ics.X``. These files contain the positions, velocities, and IDs of the particles in the initial conditions. They are Gadget Format-I files, that can be read with `Pylians3 <https://github.com/franciscovillaescusa/Pylians3>`_  as shown below.
- ``inputspec_ics.txt``. A file generated by 2LPT with the input power spectrum. Only needed for debugging.
- ``logIC``. This file contains the output generated by 2LPT when generating the initial conditions. One useful for internal debugging.
- ``Pk_m_z=0.000.txt``. The linear matter power spectrum at :math:`z=0` for the simulation. This file is generated by running the ``CAMB`` code with the ``CAMB.params`` parameter file. This file is used in ``2LPT.param`` to generate the initial conditions.

The files with the initial conditions can be read as follows:

.. code-block:: python

   import numpy as np
   import readgadget

   # name of the snapshot
   snapshot = '/mnt/ceph/users/camels/Sims/SIMBA/LH_156/ICs/ics'

   # read snapshot header
   header   = readgadget.header(snapshot)
   BoxSize  = header.boxsize/1e3  #Mpc/h
   Nall     = header.nall         #Total number of particles
   Masses   = header.massarr*1e10 #Masses of the particles in Msun/h
   Omega_m  = header.omega_m      #value of Omega_m
   Omega_l  = header.omega_l      #value of Omega_l
   h        = header.hubble       #value of h
   redshift = header.redshift     #redshift of the snapshot
   Hubble   = 100.0*np.sqrt(Omega_m*(1.0+redshift)**3+Omega_l)#Value of H(z) in km/s/(Mpc/h)

   # read positions, velocities and IDs of the gas particles
   ptype = [0] #gas is particle type 0
   pos_g = readgadget.read_block(snapshot, "POS ", ptype)/1e3 #positions in Mpc/h
   vel_g = readgadget.read_block(snapshot, "VEL ", ptype)     #peculiar velocities in km/s
   ids_g = readgadget.read_block(snapshot, "ID  ", ptype)-1   #IDs starting from 0

   # read positions, velocities and IDs of the dark matter particles
   ptype = [1] #dark matter is particle type 1
   pos_c = readgadget.read_block(snapshot, "POS ", ptype)/1e3 #positions in Mpc/h
   vel_c = readgadget.read_block(snapshot, "VEL ", ptype)     #peculiar velocities in km/s
   ids_c = readgadget.read_block(snapshot, "ID  ", ptype)-1   #IDs starting from 0


.. Note::

   When using the ``readgadget`` library, the particle velocities automatically incorporate the :math:`\sqrt{a}` Gadget factor.

.. Note::

   When reading initial conditions of N-body simulations, only positions, velocities, and IDs for dark matter particles are present, not for gas.


.. _suite_differences:
   
Suite differences
~~~~~~~~~~~~~~~~~

The simulations from the SIMBA and IllustrisTNG suites are very different: they solve the hydrodynamic equations using completely different methods and the subgrid models employed are distinct. However, the format of the data is very similar in the two sets. The main differences are these:

- The format of the metallicity array is slightly different.  In SIMBA, ``Metallicity`` is an 11-element array where the n=0 component is the `total` metal mass fraction (everything not H, He), and the remaining elements contain the mass fraction in [He,C,N,O,Ne,Mg,Si,S,Ca,Fe].

- Particle positions are saved in single precision in SIMBA, while in IllustrisTNG are stored in double precision.

- The SIMBA simulations track ``Dust_Masses`` and ``Dust_Metallicity`` (that are not available in IllustrisTNG), while IllustrisTNG simulations contain magnetic fields (not available in SIMBA).

- In the SIMBA simulations the masses of the dark matter particles are listed individually in ``PartType1/Masses``. In the IllustrisTNG simulations the dark matter particle mass is only stored in the header.

- The hydrodynamics methods are different and so the sizes (and shapes) that gas elements represent are different in IllustrisTNG and SIMBA. 
