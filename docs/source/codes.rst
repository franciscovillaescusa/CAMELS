.. _Codes:

*****
Codes
*****

As discussed in :ref:`suites_sets`, the CAMELS simulations can be classified into different suites depending on the code and subgrid model used to run them. Below we provide some details on the codes, physics, and subgrid models employed.

IllustrisTNG
~~~~~~~~~~~~

The simulations in the IllustrisTNG suite have been run with the Arepo code using the same subgrid physics as the IllustrisTNG simulation. Arepo uses TreePM to solve for gravity and a moving Voronoi mesh to solve for ideal magnetohydrodynamics (MHD). The IllustrisTNG galaxy formation physics implementation includes sub-grid models for star-formation, stellar evolution and galactic winds, as well as supermassive black hole (SMBH) seeding, merging, accretion and feedback. The latter operates in two modes, selected based on SMBH mass and Eddington ratio, where the high-accretion mode is thermal and the low accretion mode is kinetic and is the more efficient one in ejecting gas and quenching massive galaxies. The galactic winds feedback is kinetic, implemented via briefly hydrodynamically decoupled wind particles, with energy and mass loading factors that are prescribed based on local velocity dispersion and metallicity. Much more detail can be found on the `IllustrisTNG project website <https://www.tng-project.org/>`_.

The video below shows an example of a CAMELS-IllustrisTNG simulation:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/wWrED1ekB1c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   <br><br>
   

SIMBA
~~~~~

The simulations in the SIMBA suite have been run with GIZMO code using the same subgrid physics as the SIMBA simulation.

The video below shows an example of a CAMELS-SIMBA simulation:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/GtRfDw6tX5U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   <br><br>
   

Astrid
~~~~~~

The simulations in the ASTRID suite have been run with the `MP-Gadget <https://github.com/MP-Gadget/MP-Gadget>`__ code, a massively scalable version of the cosmological structure formation code Gadget-3, to solve the gravity (with TreePM), hydrodynamics (using entropy-conserving formulation of Smoothed Particle Hydrodynamics method). ASTRID models galaxy formation physics including sub-grid models for multi-phase ISM and star-formation (`Springel & Hernquist 2003 <https://academic.oup.com/mnras/article/339/2/289/1003780>`__), stellar evolution and metal enrichment (`Vogelsberger et al. 2014 <https://academic.oup.com/mnras/article/444/2/1518/1749887>`__), galactic winds, as well as supermassive black hole (SMBH) seeding, merging, accretion and feedback (`Di Matteo et al. 2005 <https://arxiv.org/abs/astro-ph/0502199>`__). The details of ASTRID subgrid model are described in `Bird et al. 2022 <https://academic.oup.com/mnras/article/512/3/3703/6546174>`__ and  `Ni et al. 2022 <https://academic.oup.com/mnras/article/513/1/670/6533522>`__.

The video below shows an example of a CAMELS-Astrid simulation:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/oahCUZMRJZU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   <br><br>
   

Magneticum
~~~~~~~~~~

The simulations in the Magneticum suite have been run with the parallel cosmological Tree-PM code `OpenGadget3 <https://arxiv.org/abs/2301.03612>`__. The code uses an entropy-conserving formulation of Smoothed Particle Hydrodynamics (SPH) `(Springel & Hernquist 2002) <https://academic.oup.com/mnras/article/333/3/649/1002394>`__, with SPH modifications according to `Dolag et al. (2004) <https://arxiv.org/abs/astro-ph/0401470>`__, `Dolag et al. (2005) <https://arxiv.org/abs/astro-ph/0507480>`__, and `Dolag et al. (2006) <https://arxiv.org/abs/astro-ph/0511357>`__. It includes also prescriptions for multiphase interstellar medium based on the model by `Springel & Hernquist (2003) <https://academic.oup.com/mnras/article/339/2/289/1003780>`__ as well as `Tornatore et al. (2007) <https://academic.oup.com/mnras/article/382/3/1050/1008452>`__ for the metal enrichment prescription. The model follows the growth and evolution of BHs and their associated AGN feedback based on the model presented by `Springel et al. (2005) <https://academic.oup.com/mnras/article/364/4/1105/1042826>`__ and `Di Matteo et al. (2005) <https://arxiv.org/abs/astro-ph/0502199>`__, but includes modifications based on `Fabjan et al. (2011) <https://academic.oup.com/mnras/article/416/2/801/1054051>`__, `Hirschmann et al. (2014b) <https://academic.oup.com/mnras/article/442/3/2304/1039443>`__, and `Steinborn et al. (2016) <https://academic.oup.com/mnras/article/458/1/1013/2622553>`__. 

The video below shows an example of a CAMELS-Magneticum simulation:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/rE6V8Tx8438" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   <br><br>


Swift-EAGLE
~~~~~~~~~~~

The simulations in the Swift-EAGLE suite have been run with the smoothed particle hydrodynamics and gravity code `Swift <https://arxiv.org/abs/2305.13380>`__. Swift is a parallel, open-source, versatile and modular code, with a range of hydrodynamics solvers, gravity solvers, and sub-grid models for galaxy formation (see `Swift website <https://swift.strw.leidenuniv.nl/>`__). In this suite we use the `SPHENIX <https://academic.oup.com/mnras/article/511/2/2367/6423434?login=true>`__  flavour of SPH, coupled with a modified version of the Evolution and Assembly of GaLaxies and their Environments (`EAGLE <https://virgo.dur.ac.uk/2014/11/11/EAGLE/index.html>`__) subgrid model for galaxy formation and evolution (see `Schaye et al. 2015 <https://academic.oup.com/mnras/article/446/1/521/1316115?login=true>`__ and `Crain et al. 2015 <https://academic.oup.com/mnras/article/450/2/1937/984366?login=true>`__). This includes element-by-element radiative cooling and heating rates from `Ploeckinger & Schaye 2020 <https://academic.oup.com/mnras/article/497/4/4857/5876367?login=true>`__, stellar evolution and enrichment from `Wiersma  et al. 2009 <https://academic.oup.com/mnras/article/399/2/574/1059162?login=true>`__, and single thermal-mode feedback from massive stars and accreting AGN (see `Schaye & Dalla Vecchia <https://academic.oup.com/mnras/article/383/3/1210/1037943>`__, `Booth & Schaye 2009 <https://academic.oup.com/mnras/article/398/1/53/1092579?login=true>`__, `Rosas-Guevara et al. 2015 <https://academic.oup.com/mnras/article/454/1/1038/1143767?login=true>`__).


Ramses
~~~~~~

The simulations in the RAMSES suite have been run with the `RAMSES code <https://bitbucket.org/rteyssie/ramses/src/master/>`__ using the same subgrid physics as in `Kretschmer & Teyssier (2021) <https://arxiv.org/abs/1906.11836>`__ and `Teyssier et al. (2011) <https://arxiv.org/abs/1003.4744>`__. RAMSES uses Adaptive Particle Mesh to solve for gravity and the Godunov Finite Volume Constrained Transport method to solve for ideal magnetohydrodynamics (MHD). The galaxy formation physics implementation includes a multi-freefall sub-grid model for star-formation and supernovae momentum feedback as in `Kretschmer and Teyssier (2021) <https://arxiv.org/abs/1906.11836>`__, as well as supermassive black hole (SMBH) seeding, merging, accretion and feedback as in `Teyssier et al. (2011) <https://arxiv.org/abs/1003.4744>`__ and `Pellissier et al. (2023) <https://arxiv.org/abs/2301.02684>`__. RAMSES also models metallicity dependent radiative cooling, as well as radiation heating from a self-shielded UV background consistent with standard reionization models.

The video below shows an example of a CAMELS-Ramses simulation:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/WnNfkok9sJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   <br><br>
	 

Enzo
~~~~

The simulations in the Enzo suite have been run with the Enzo code.


N-body
~~~~~~

All the N-body simulations hve been run with the Gadget-III code.

The video below shows an example of a CAMELS-Nbody simulation:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/w0VPWIyc7Wk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   <br><br>
