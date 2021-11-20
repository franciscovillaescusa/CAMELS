.. _differences:

******************
Suites differences
******************

Snapshots
---------

The SIMBA and IllustrisTNG simulations are very different: they solve the hydrodynamic equations using completely different methods and the subgrid models employed are distinct. However, the format of the data is very similar in the two sets. The main differences are these:

- The format of the metallicity array is slightly different.  In SIMBA, ``Metallicity`` is an 11-element array where the n=0 component is the `total` metal mass fraction (everything except H, He), and the remaining elements contain the mass fraction in the order [He,C,N,O,Ne,Mg,Si,S,Ca,Fe].

- Particle positions are saved in single precision in SIMBA, while in IllustrisTNG, they are stored in double precision.

- The SIMBA simulations track ``Dust_Masses`` and ``Dust_Metallicity`` (that are not available in IllustrisTNG), while IllustrisTNG simulations contain magnetic fields (not available in SIMBA).

- In SIMBA simulations, the masses of the dark matter particles are listed individually in ``PartType1/Masses``. In IllustrisTNG simulations, the dark matter particle mass is only stored in the header.

- The hydrodynamics methods are different and so the sizes (and shapes) that gas elements represent are different in IllustrisTNG and SIMBA. 

  
Halo/galaxy catalogues
----------------------

The halo/subhalo catalogues are designed to be as uniform as possible across the two suites. Thus, the metallicity field in the subfind catalogues of SIMBA differ from the metallicity field of the SIMBA snapshots. The ``Metallicity`` and ``MetalFraction`` fields in the subfind catalogues follow the same convention as those from the IllustrisTNG catalogues, except that the elements are the same as in the SIMBA snapshots.

In particular:

- In IllustrisTNG snapshots and group catalogs, ``Metallicity`` is the total content of elements heavier than H & He, and ``Metals`` or ``MetalFractions`` is a 10-element array with the elements in this order: [H, He, C, N, O, Ne, Mg, Si, Fe, other metals]
  
- In SIMBA snapshots, ``Metallicity`` is an 11-element array with the elements in the order: [the total content of elements heavier than H & He, He,C,N,O,Ne,Mg,Si,S,Ca,Fe].
  
- In SIMBA FOF+Subfind catalogs, the structure is similar to IllustrisTNG: ``Metallicity`` is the total content of elements heavier than H & He, and ``Metals`` or ``MetalFractions`` is a 11-element array with the elements in this (SIMBA-snapshot-like) order: [H,He,C,N,O,Ne,Mg,Si,S,Ca,Fe]


In the SIMBA catalogues, the ``SubhaloStellarPhotometrics`` and ``WindMass`` fields contain some irrelevant numbers as those quantities are not calculated within the SIMBA simulations.
