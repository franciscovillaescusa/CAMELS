.. _snapshots:

*********
Snapshots
*********


CAMELS snapshots are stored as single hdf5 files. In order to read them in python, you will need ``h5py``. The simplest way to inspect the content of a snapshot is this:

.. code-block:: bash

   >> h5ls -r IllustrisTNG/CV_14/snap_024.hdf5
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

- ``Header``. This group contains different properties of the simulations such as its box size, number of particles, value of the cosmological parameters, etc.
- ``PartType0``. This group contains the properties of the gas particles.
- ``PartType1``. This group contains the properties of the dark matter particles.
- ``PartType4``. This group contains the properties of the star particles.
- ``PartType5``. This group contains the properties of the black hole particles.

For instance, the block ``/PartType4/Coordinates`` contains the coordinates of the star particles. A detailed description of the different blocks can be found `here <https://www.tng-project.org/data/docs/specifications/#sec1b>`_

.. Note::

   While the format of the snapshots in the IllustrisTNG and SIMBA suites is almost identical, there are a few differences. See :ref:`differences` for more information.

Reading the header or different blocks can be done as follows:

.. code-block:: python

   import numpy as np
   import h5py

   # snapshot name
   snapshot = 'IllustrisTNG/CV_14/snap_014.hdf5'

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
