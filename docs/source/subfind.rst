.. _subfind:

******************
SUBFIND catalogues
******************

The ``FOF_Subfind`` folder contains the SUBFIND halo/subhalo/galaxy catalogues. The data is organized following the general hierarchical structure described in :ref:`suite_folders`.

The catalogues are stored as hdf5 files. ``h5py`` is needed in order to read these files using python. CAMELS provides a halo/subhalo catalogue for each snapshot. The halos and subhalos are identified through SUBFIND.

The easiest way to inspect the content of these files is:

.. code-block:: bash

   >> h5ls -r SIMBA/CV_5/fof_subhalo_tab_031.hdf5
   /                        Group
   /Config                  Group
   /Group                   Group
   /Group/GroupBHMass       Dataset {32272}
   /Group/GroupBHMdot       Dataset {32272}
   /Group/GroupCM           Dataset {32272, 3}
   /Group/GroupFirstSub     Dataset {32272}
   /Group/GroupGasMetalFractions Dataset {32272, 11}
   /Group/GroupGasMetallicity Dataset {32272}
   /Group/GroupLen          Dataset {32272}
   /Group/GroupLenType      Dataset {32272, 6}
   /Group/GroupMass         Dataset {32272}
   /Group/GroupMassType     Dataset {32272, 6}
   /Group/GroupNsubs        Dataset {32272}
   /Group/GroupPos          Dataset {32272, 3}
   /Group/GroupSFR          Dataset {32272}
   /Group/GroupStarMetalFractions Dataset {32272, 11}
   /Group/GroupStarMetallicity Dataset {32272}
   /Group/GroupVel          Dataset {32272, 3}
   /Group/GroupWindMass     Dataset {32272}
   /Group/Group_M_Crit200   Dataset {32272}
   /Group/Group_M_Crit500   Dataset {32272}
   /Group/Group_M_Mean200   Dataset {32272}
   /Group/Group_M_TopHat200 Dataset {32272}
   /Group/Group_R_Crit200   Dataset {32272}
   /Group/Group_R_Crit500   Dataset {32272}
   /Group/Group_R_Mean200   Dataset {32272}
   /Group/Group_R_TopHat200 Dataset {32272}
   /Header                  Group
   /IDs                     Group
   /IDs/ID                  Dataset {14575639}
   /Parameters              Group
   /Subhalo                 Group
   /Subhalo/SubhaloBHMass   Dataset {22315}
   /Subhalo/SubhaloBHMdot   Dataset {22315}
   /Subhalo/SubhaloBfldDisk Dataset {22315}
   /Subhalo/SubhaloBfldHalo Dataset {22315}
   /Subhalo/SubhaloCM       Dataset {22315, 3}
   /Subhalo/SubhaloGasMetalFractions Dataset {22315, 11}
   /Subhalo/SubhaloGasMetalFractionsHalfRad Dataset {22315, 11}
   /Subhalo/SubhaloGasMetalFractionsMaxRad Dataset {22315, 11}
   /Subhalo/SubhaloGasMetalFractionsSfr Dataset {22315, 11}
   /Subhalo/SubhaloGasMetalFractionsSfrWeighted Dataset {22315, 11}
   /Subhalo/SubhaloGasMetallicity Dataset {22315}
   /Subhalo/SubhaloGasMetallicityHalfRad Dataset {22315}
   /Subhalo/SubhaloGasMetallicityMaxRad Dataset {22315}
   /Subhalo/SubhaloGasMetallicitySfr Dataset {22315}
   /Subhalo/SubhaloGasMetallicitySfrWeighted Dataset {22315}
   /Subhalo/SubhaloGrNr     Dataset {22315}
   /Subhalo/SubhaloHalfmassRad Dataset {22315}
   /Subhalo/SubhaloHalfmassRadType Dataset {22315, 6}
   /Subhalo/SubhaloIDMostbound Dataset {22315}
   /Subhalo/SubhaloLen      Dataset {22315}
   /Subhalo/SubhaloLenType  Dataset {22315, 6}
   /Subhalo/SubhaloMass     Dataset {22315}
   /Subhalo/SubhaloMassInHalfRad Dataset {22315}
   /Subhalo/SubhaloMassInHalfRadType Dataset {22315, 6}
   /Subhalo/SubhaloMassInMaxRad Dataset {22315}
   /Subhalo/SubhaloMassInMaxRadType Dataset {22315, 6}
   /Subhalo/SubhaloMassInRad Dataset {22315}
   /Subhalo/SubhaloMassInRadType Dataset {22315, 6}
   /Subhalo/SubhaloMassType Dataset {22315, 6}
   /Subhalo/SubhaloParent   Dataset {22315}
   /Subhalo/SubhaloPos      Dataset {22315, 3}
   /Subhalo/SubhaloSFR      Dataset {22315}
   /Subhalo/SubhaloSFRinHalfRad Dataset {22315}
   /Subhalo/SubhaloSFRinMaxRad Dataset {22315}
   /Subhalo/SubhaloSFRinRad Dataset {22315}
   /Subhalo/SubhaloSpin     Dataset {22315, 3}
   /Subhalo/SubhaloStarMetalFractions Dataset {22315, 11}
   /Subhalo/SubhaloStarMetalFractionsHalfRad Dataset {22315, 11}
   /Subhalo/SubhaloStarMetalFractionsMaxRad Dataset {22315, 11}
   /Subhalo/SubhaloStarMetallicity Dataset {22315}
   /Subhalo/SubhaloStarMetallicityHalfRad Dataset {22315}
   /Subhalo/SubhaloStarMetallicityMaxRad Dataset {22315}
   /Subhalo/SubhaloStellarPhotometrics Dataset {22315, 8}
   /Subhalo/SubhaloStellarPhotometricsMassInRad Dataset {22315}
   /Subhalo/SubhaloStellarPhotometricsRad Dataset {22315}
   /Subhalo/SubhaloVel      Dataset {22315, 3}
   /Subhalo/SubhaloVelDisp  Dataset {22315}
   /Subhalo/SubhaloVmax     Dataset {22315}
   /Subhalo/SubhaloVmaxRad  Dataset {22315}
   /Subhalo/SubhaloWindMass Dataset {22315}

The catalogues contain two main groups:

- ``Group``. This group contains the properties of the halos.
- ``Subhalos``. This group contains the properties of the subhalos. Galaxies, are considered as subhalos with stellar mass larger than 0.

A detailed description of the different blocks in the catalogues can be found `here <https://www.tng-project.org/data/docs/specifications/#sec2>`_.

Reading these files with python is straightforward:

.. code-block:: python

   import numpy as np
   import h5py
   
   # catalogue name
   catalogue = 'SIMBA/CV_5/fof_subhalo_tab_033.hdf5'

   # value of the scale factor
   scale_factor = 1.0
   
   # open the catalogue
   f = h5py.File(catalogue, 'r')

   # read the positions, velocities and masses of the FoF halos
   pos_h  = f['Group/GroupPos'][:]/1e3           #positions in Mpc/h
   vel_h  = f['Group/GroupVel'][:]/scale_factor  #velocities in km/s
   mass_h = f['Group/GroupMass'][:]*1e10         #masses in Msun/h

   # read the positions, black hole masses and stellar masses of the subhalos/galaxies
   pos_g  = f['Subhalo/SubhaloMass'][:]/1e3        #positions in Mpc/h
   BH_g   = f['Subhalo/SubhaloBHMass'][:]*1e10     #black-hole masses in Msun/h
   M_star = f['Subhalo/SubhaloMassType'][:,4]*1e10 #stellar masses in Msun/h
   
   # close file
   f.close()


.. Note::

   Differently to the snapshots, the format of these files is identical across the simulations in the IllustrisTNG and SIMBA suites.


Suite differences
~~~~~~~~~~~~~~~~~

The halo/subhalo catalogues are designed to be as uniform as possible across the two suites. Thus, the metallicity field in the subfind catalogues of SIMBA differ from the metallicity field of the SIMBA snapshots. The ``Metallicity`` and ``MetalFraction`` fields in the subfind catalogues follow the same convention as those from the IllustrisTNG catalogues, except that the elements are the same as in the SIMBA snapshots.

In particular:

- In IllustrisTNG snapshots and group catalogs, ``Metallicity`` is the total content of elements heavier than H & He, and ``Metals`` or ``MetalFractions`` is a 10-element array with the elements in this order: [H, He, C, N, O, Ne, Mg, Si, Fe, other metals]
  
- In SIMBA snapshots, ``Metallicity`` is an 11-element array with the elements in this order: [the total content of elements heavier than H & He, He,C,N,O,Ne,Mg,Si,S,Ca,Fe].
  
- In SIMBA FOF+Subfind catalogs, the structure is similar to IllustrisTNG: ``Metallicity`` is the total content of elements heavier than H & He, and ``Metals`` or ``MetalFractions`` is a 11-element array with the elements in this (SIMBA-snapshot-like) order: [H,He,C,N,O,Ne,Mg,Si,S,Ca,Fe]

In the SIMBA catalogues, the ``SubhaloStellarPhotometrics`` and ``WindMass`` fields contain some irrelevant numbers as those quantities are not calculated within the SIMBA simulations.

