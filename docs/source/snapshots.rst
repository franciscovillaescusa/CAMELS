.. _snapshots:

***********
Simulations
***********

.. important::

   A reorganization of the data has been performed in 2024 in order to enhance its uniformity and simplicity. This will require slight changes to existing codes that access the data.

   - Folders in the 1P sets are now named ``1P_pX_Y`` and each parameter only has 4 variations, rather than 10, such that ``X`` ranges from n2 to 2. In a few exceptions (e.g. when fiducial value is 0 and negative values are not physical), a parameter may vary from 0 (fiducial) to 4 instead of from n2 to 2.
   - Snapshot numbers in the IllustrisTNG and SIMBA suites, where simulations had only 34 snapshots, have been updated to match the numbering in the Astrid suite (and some TNG simulations) that have 91 snapshots. For example, where 33 used to be the z=0 snapshot, now it is 90 uniformly for all suites.
   - Snapshot files have been renamed from ``snap_###.hdf5`` to ``snapshot_###.hdf5`` and fof/subfind files from ``fof_subhalo_tab_###.hdf5`` to ``groups_###.hdf5``.
     

The ``Sims`` folder contains the raw data from all CAMELS simulations. The data is organized following the general hierarchical structure described in :ref:`suite_folders`. Thus, the simulations are organized by:

1. the code used to run the simulations: *suite folder*
2. the volume of the simulations: *volume folder*
3. the way simulations parameters are arranged: *set folder*


Suite folders
~~~~~~~~~~~~~

The ``Sims`` folder contains different *suite folders*, that contain all simulations run with a given code:

- ``IllustrisTNG``. This folder contains all simulations of the IllustrisTNG suite.
- ``SIMBA``. This folder contains all simulations of the SIMBA suite.
- ``Astrid``. This folder contains all simulations of the Astrid suite.
- ``Magneticum``. This folder contains all simulations of the Magneticum suite.
- ``Ramses``. This folder contains all simulations of the Ramses suite.
- ``EAGLE``. This folder contains all simulations of the Swift-EAGLE suite.
- ``Enzo``. This folder contains all simulations of the Enzo suite.

Each of the above suites have an associated N-body suite. Those simulations are located in a folder with the name of the suite followed by ``DM``. For instance, the folder ``IllustrisTNG_DM`` contains all the N-body simulations that are the counterpart of the full hydrodynamic simulations contained in the ``IllustrisTNG`` folder.

.. Note::
  
   The value of the cosmological, astrophysical, and initial random seed for simulations in the different suites can be found in :ref:`params`. Those files also hold for the N-body simulations; each N-body simulation has the same value of the cosmological parameters and initial random seed as their hydrodynamic counterpart.
   

Volume folders
~~~~~~~~~~~~~~

The vast majority of the CAMELS simulations follow the evolution of :math:`256^3` dark matter and :math:`256^3` initial fluid elements in a periodic :math:`(25~h^{-1}{\rm Mpc})^3` volume. As the CAMELS project evolves and matures, it will contain simulations with larger volumes while keeping the same mass and spatial resolution. As of January 2024, only simulations in the IllustrisTNG suite have simulations at two different volumes: :math:`(25~{\rm Mpc/h})^3` and :math:`(50~{\rm Mpc/h})^3`.

In general, between the *suite* and the *set folders*, there may be some *volume folders* indicating the volume and number of particles of the simulations. For the foreseable future, only these three folders will exist:

- ``L25n256``. This folder contains the simulations that follow the evolution of :math:`256^3` dark matter particles and :math:`256^3` initial fluid elements in a :math:`(25~{\rm Mpc/h})^3` volume.
- ``L50n512``. This folder contains the simulations that follow the evolution of :math:`512^3` dark matter particles and :math:`512^3` initial fluid elements in a :math:`(50~{\rm Mpc/h})^3` volume.
- ``L100n1024``. This folder contains the simulations that follow the evolution of :math:`1024^3` dark matter particles and :math:`1024^3` initial fluid elements in a :math:`(100~{\rm Mpc/h})^3` volume.
  
In general, the volume folders will follow the convention ``LXnY``, where ``X`` is the box size in Mpc/h and Y is the cubic root of the number of dark matter particles in the simulations.

.. Warning::

   If no volume folder is present in a given simulation suite, it means that all simulations are simulations are standard, i.e. they follow the evolution of :math:`256^3` dark matter particles and :math:`256^3` initial fluid elements in a :math:`(25~{\rm Mpc/h})^3` volume.


Set folders
~~~~~~~~~~~
  
Inside each *suite folder* (or *volume folder*) there are the *set folders* (see :ref:`suites_sets` for details):

- ``1P``. This folder constains the simulations of the 1P set. Inside this folder, there are subfolders named ``1P_pX_Y`` that contain the different simulations in the 1P set. ``X`` ranges from ``1`` to ``N``, where ``N`` is the number of parameters  while ``Y`` goes from ``n2`` (-2) to ``2`` and denotes the variation of the parameter where 0 is the fiducial value. In a few exceptions (e.g. when fiducial value is 0 and negative values are not physical), a parameter may vary from 0 (fiducial) to 4 instead of from n2 to 2. See :ref:`set_folders` for details about the naming of the simulations in the 1P set.
- ``CV``. This folder contains the simulation of the CV set. The subfolders in this folder are named ``CV_X``, where X goes from 0 to 26.
- ``LH``. This folder contains the simulation of the LH set. The subfolders in this folder are named ``LH_X`` where X goes from 0 to 999.
- ``EX``. This folder contains the simulation of the EX set. The subfolders in this folder are named ``EX_X`` where X goes from 0 to 3.
- ``BE``. This folder contains the simulation of the BE set. The subfolders in this folder are named ``BE_X``, where X goes from 0 to 26.
- ``SB``. This folder contains the simulation of the SB set. In general, this set is named as ``SBY``, where Y is the number of dimensions sampled in the Sobol Sequence (e.g. SB28 for IllustrisTNG). The subfolders in this folder are named ``SBY_X``, where X goes from 0 to N-1, where N is the number of simulations in the Sobol sequence.
- ``zoom``. This folder contains sets of zoom-in simulations. The subfolders correspond to the halo type of zoom-in simulations, e.g. ``GZY`` representing Group Zoom, and Y the number of parameter space dimensions sampled. The individual zoom-in simulations are in the corresponding subfolders with GZY_X where X goes from 0 to N-1 with N being the number of simulations.
- ``CosmoAstroSeed_<suitname>_<volumename>_<setname>.txt``. This file contains the value of the cosmological and astrophysical parameter, together with the value of the random seed, for each simulation in the set. The format of the file is: simulation_name [parameter1 parameter2 … parameterN] seed.

Besides the above, the *set folders* may also contain some files with the value of the cosmological and astrophysical parameters for the Sobol sequences. 
  
  
.. Note::

   The structure and organization of the N-body simulations (e.g. ``IllustrisTNG_DM``) is the same as their full hydrodynamic counterparts.



Simulation folders
~~~~~~~~~~~~~~~~~~

The subfolders inside the *set folders* are *simulations folders*, and they contain the actual simulations:

.. code-block:: bash

   >> ls Sims/IllustrisTNG/L25n256/CV/CV_0
   blackhole_details         fof_subhalo_tab_021.hdf5  snap_011.hdf5
   blackhole_mergers         fof_subhalo_tab_022.hdf5  snap_012.hdf5
   CosmoAstro_params.txt     fof_subhalo_tab_023.hdf5  snap_013.hdf5
   extra_files               fof_subhalo_tab_024.hdf5  snap_014.hdf5
   fof_subhalo_tab_000.hdf5  fof_subhalo_tab_025.hdf5  snap_015.hdf5
   fof_subhalo_tab_001.hdf5  fof_subhalo_tab_026.hdf5  snap_016.hdf5
   fof_subhalo_tab_002.hdf5  fof_subhalo_tab_027.hdf5  snap_017.hdf5
   fof_subhalo_tab_003.hdf5  fof_subhalo_tab_028.hdf5  snap_018.hdf5
   fof_subhalo_tab_004.hdf5  fof_subhalo_tab_029.hdf5  snap_019.hdf5
   fof_subhalo_tab_005.hdf5  fof_subhalo_tab_030.hdf5  snap_020.hdf5
   fof_subhalo_tab_006.hdf5  fof_subhalo_tab_031.hdf5  snap_021.hdf5
   fof_subhalo_tab_007.hdf5  fof_subhalo_tab_032.hdf5  snap_022.hdf5
   fof_subhalo_tab_008.hdf5  fof_subhalo_tab_033.hdf5  snap_023.hdf5
   fof_subhalo_tab_009.hdf5  ICs                       snap_024.hdf5
   fof_subhalo_tab_010.hdf5  snap_000.hdf5             snap_025.hdf5
   fof_subhalo_tab_011.hdf5  snap_001.hdf5             snap_026.hdf5
   fof_subhalo_tab_012.hdf5  snap_002.hdf5             snap_027.hdf5
   fof_subhalo_tab_013.hdf5  snap_003.hdf5             snap_028.hdf5
   fof_subhalo_tab_014.hdf5  snap_004.hdf5             snap_029.hdf5
   fof_subhalo_tab_015.hdf5  snap_005.hdf5             snap_030.hdf5
   fof_subhalo_tab_016.hdf5  snap_006.hdf5             snap_031.hdf5
   fof_subhalo_tab_017.hdf5  snap_007.hdf5             snap_032.hdf5
   fof_subhalo_tab_018.hdf5  snap_008.hdf5             snap_033.hdf5
   fof_subhalo_tab_019.hdf5  snap_009.hdf5
   fof_subhalo_tab_020.hdf5  snap_010.hdf5

		
The most relevant ones are these:

- ``ICs``. This folder contains the initial conditions of the simulations. See :ref:`ICs` for further details.

- ``snapshot_0XY.hdf5``. These are the simulation snapshots. Numbers go from 000 (corresponding to :math:`z=15`) to 090 (corresponding to :math:`z=0`). See :ref:`redshifts` to know the redshifts associated to the different numbers. These files contain the positions, velocities, IDs and other properties of the dark matter particles and the fluid resolution elements of the simulation. See :ref:`snapshots` for details on how to read these files.
  
- ``groups_0XY.hdf5``. These files contain the halo/galaxy catalogues. Numbers go from 000 (corresponding to :math:`z=15`) to 090 (corresponding to :math:`z=0`). See :ref:`redshifts` to know the redshifts associated to the different numbers. These files contain the properties of the halos and subhalos identified by SUBFIND. See :ref:`subfind` to see how to read these files.

.. _Reach out to us: camel.simulations@gmail.com
  
There are many other files in a simulation folder that we do not describe as they are barely used. `Reach out to us`_ if you need help with those.


.. _Snaps:

Snapshots
~~~~~~~~~

CAMELS snapshots are stored as single hdf5 files. In order to read them in python, you will need ``h5py``. The simplest way to inspect the content of a snapshot is this:

.. code-block:: bash

   >> h5ls -r Sims/IllustrisTNG/L25n256/CV/CV_14/snapshot_024.hdf5
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
- ``PartType2``. This group contains low-resolution dark matter particles, only relevant in zoom-in simulations. 
- ``PartType4``. This group contains the properties of the star particles.
- ``PartType5``. This group contains the properties of the black hole particles.

For instance, the block ``/PartType4/Coordinates`` contains the coordinates of the star particles. A detailed description of the different blocks can be found `here <https://www.tng-project.org/data/docs/specifications/#sec1b>`_. 

.. Note::

   While the format of the snapshots in the different suites is almost identical, there are a few differences. See :ref:`suite_differences` for more information.

.. Note::

   The zoom-in simulations contain snapshot directories as opposed to individual files.

.. _read_snaps:
   
Reading the snapshot header and blocks can be done as follows:

.. code-block:: python

   import numpy as np
   import h5py
   import hdf5plugin

   # snapshot name
   snapshot = 'Sims/IllustrisTNG/L25n256/CV/CV_14/snapshot_014.hdf5'

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

.. warning::

   To read the hdf5 files you need to do both ``import hdf5`` and ``import hdf5plugin``. This is because the CAMELS N-body simulations have been compressed in a way that requires an additional library: ``hdf5plugin``. We recommend loading that library always as its usage is transparent and will work with both compressed and uncompressed snapshots. If you don't have it already, you can install it with ``python -m pip install hdf5plugin``. Note that the hdf5plugin library is already installed on binder.

.. Note::

   Note that the N-body simulations only contain the positions, velocities and IDs of the dark matter particles.



.. _ICs:   

Initial conditions
~~~~~~~~~~~~~~~~~~

The initial conditions of all simulations were generated at :math:`z=127` using second order lagrangian perturbation theory (2LPT). The same transfer function (total matter) was used for the gas and dark matter components. Particles were initially laid down in a regular grid: one grid for the dark matter particles and another grid, offset by half a grid cell, for the gas.

The initial condition files can be found inside each simulation folder. For instance, to access the initial conditions of the LH_156 simulation of the SIMBA suite:

.. code-block:: bash

   >> ls Sims/SIMBA/L25n256/LH/LH_156/ICs
   2LPT.param   ics.1  ics.4  ics.7              Pk_m_z=0.000.txt
   CAMB.params  ics.2  ics.5  inputspec_ics.txt
   ics.0        ics.3  ics.6  logIC

There are different files:

- ``2LPT.param``. This is the 2LPT parameter file used to generate the simulation initial conditions.
- ``CAMB.params``. This CAMB parameter file used to generate the :math:`z=0` matter power spectrum needed to generate the initial conditions.
- ``ics.X``. These files contain the positions, velocities, and IDs of the particles in the initial conditions. They can be Gadget Format I (for the hydrodynamic simulations) or hdf5 format (for the N-body simulations). In both cases, the data can be read with `Pylians3 <https://github.com/franciscovillaescusa/Pylians3>`_  as shown below. The hdf5 files can also be read as standard snapshots (see read_snaps_).
- ``inputspec_ics.txt``. A file generated by 2LPT with the input power spectrum. Only needed for debugging.
- ``logIC``. This file contains the output generated by 2LPT when generating the initial conditions. One useful for internal debugging.
- ``Pk_m_z=0.000.txt``. The linear matter power spectrum at :math:`z=0` for the simulation. This file is generated by running the ``CAMB`` code with the ``CAMB.params`` parameter file. This file is used in ``2LPT.param`` to generate the initial conditions.

The files with the initial conditions can be read as follows:

.. code-block:: python

   import numpy as np
   import readgadget

   # name of the snapshot
   snapshot = '/mnt/ceph/users/camels/Sims/Astrid/L25n256/LH/LH_156/ICs/ics'

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

.. Warning::

   The format of the ICs of the N-body simulations is hdf5 instead of Gadget format I. These files can be read in the same way as above or can be read as hdf5 files; see read_snaps_. Keep in mind that those files have been compressed, so you need to use load the hdf5plugin library with ``import hdf5plugin``.
   
.. Note::

   When using the ``readgadget`` library, the particle velocities automatically incorporate the :math:`\sqrt{a}` Gadget factor.

.. Note::

   When reading initial conditions of N-body simulations, only positions, velocities, and IDs for dark matter particles are present, not for gas.


.. _suite_differences:
   
Suite differences
~~~~~~~~~~~~~~~~~

The simulations from the different suites are very different: they solve the hydrodynamic equations using completely different methods and the subgrid models employed are distinct. However, the format of the data is similar among the sets. The main differences are these:

- The format of the metallicity array is slightly different.  In SIMBA, ``Metallicity`` is an 11-element array where the n=0 component is the `total` metal mass fraction (everything not H, He), and the remaining elements contain the mass fraction in [He,C,N,O,Ne,Mg,Si,S,Ca,Fe].

- Particle positions are saved in single precision in SIMBA, while in IllustrisTNG are stored in double precision.

- The SIMBA simulations track ``Dust_Masses`` and ``Dust_Metallicity`` (that are not available in IllustrisTNG), while IllustrisTNG simulations contain magnetic fields (not available in SIMBA).

- In the SIMBA simulations the masses of the dark matter particles are listed individually in ``PartType1/Masses``. In the IllustrisTNG simulations the dark matter particle mass is only stored in the header.

- The hydrodynamics methods are different and so the sizes (and shapes) that gas elements represent are different in IllustrisTNG and SIMBA. 

.. _compression:

Compression
~~~~~~~~~~~

The snapshots of the CAMELS simulations are compressed to best utilize the available resources. The data is compressed using two different schemes: lossless and lossy. Currently, the snapshots of the hydrodynamic simulations are compressed using a lossless scheme, whereas the snapshots of the N-body simulations are compressed using a lossy method (see table below). We do this because N-body simulations are much faster to (re)run and also because this compression scheme has been well tested with other N-body simulations like `Abacus <https://abacussummit.readthedocs.io>`_ and `Quijote <https://quijote-simulations.readthedocs.io>`_.

+--------------------------+------------------+
| Simulation type          | Compression type |         
+==============+===========+==================+
| N-body       | Snapshots | lossy            |
|              +-----------+------------------+
|              |    ICs    | lossless         |
+--------------+-----------+------------------+
| Hydrodynamic | Snapshots | lossless         |
|              +-----------+------------------+
|              | ICs       | none             |
+--------------+-----------+------------------+

**Lossy compression**

This compression allows us to shrink the size of the files by a factor of :math:`\sim2.5`. The details of the lossy compression are the following. The snapshots are compressed with a Blosc filter, as implemented in the `hdf5plugin <https://github.com/silx-kit/hdf5plugin/>`_ Python package.  Blosc compression applies a transpose to the data then passes it to zstandard, all of which is lossless and transparent to the user.  As a preconditioning step to increase the Blosc compression ratio, we manually null out some bits of the positions and velocities to increase the compression ratio.  This step is lossy.  

In more detail, the positions are stored as absolute coordinates in float32 precision.  The lossy preconditioning we apply is to set several of the low bits in the float32 significand to zero.  The number of bits nulled out is B=6 for the :math:`1024^3` simulations, B=7 for :math:`512^3`, and B=8 for :math:`256^3`.  This introduces a fractional error of :math:`2^{(-24+B)}`, which is :math:`1.5\times10^{-5}` for simulations with :math:`256^3` particles. Thus, for traditional CAMELS boxes of 25 Mpc/h size, the worst-case is translated into an error of 0.38 kpc/h, smaller than the softening length of these simulations. Thus, this should have minimal impact on science projects. Likewise, we null out 11 low bits of the velocities, for a fractional precision of 0.01%.  The velocity rarely goes above 6000 km/s in LCDM N-body simulations, so this is a worst case of 0.6 km/s precision. The particle IDs are compressed in a lossless manner.

The HDF5 compressed in this way contains a new group called ``/CompressionInfo`` whose attributes contain a JSON string describing the exact compression options used. The scripts used to do the compression are here: https://github.com/lgarrison/quijote-compression. We thank Lehman Garrison for setting this up.
