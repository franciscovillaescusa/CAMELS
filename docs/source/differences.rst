******************
Suites differences
******************

The SIMBA and IllustrisTNG simulations are very different: they solve the hydrodynamic equations using completely different methods and the subgrid models employed are distinct. However, the format of the data is very similar in the two sets. The main differences are these:

- The format of the metallicity array is slightly different.  In SIMBA, `Metallicity` is an 11-element array where the n=0 component is the `total` metal mass fraction (everything not H, He), and the remaining elements contain the mass fraction in [He,C,N,O,Ne,Mg,Si,S,Ca,Fe].

- Particle positions are saved in single precision, while in IllustrisTNG are stored in double precision.

- The SIMBA simulations track `Dust_Masses` and `Dust_Metallicity` (that are not available in IllustrisTNG), while IllustrisTNG simulations contain magnetic fields (not available in SIMBA).

- In the SIMBA simulations the masses of the dark matter particles are listed individually in `PartType1/Masses`. In the IllustrisTNG simulations the dark matter particle mass is only stored in the header.

- The hydrodynamics methods are different and so the sizes (and shapes) that gas elements represent are different in IllustrisTNG and SIMBA. 
