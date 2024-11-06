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

The simulations in the SIMBA suite have been run with the `GIZMO code <https://bitbucket.org/phopkins/gizmo-public/src/master/>`__ using the same subgrid physics as the original SIMBA simulation, presented in `Davé et al. 2019 <https://ui.adsabs.harvard.edu/abs/2019MNRAS.486.2827D/abstract>`__. SIMBA builds on the MUFASA model (`Davé et al. 2016 <https://ui.adsabs.harvard.edu/abs/2016MNRAS.462.3265D/abstract>`__) and the gravitational torque accretion and kinetic AGN feedback implementation of `Anglés-Alcázar et al. 2017a. <https://ui.adsabs.harvard.edu/abs/2017MNRAS.464.2840A/abstract>`__ SIMBA uses the “Meshless Finite Mass” hydrodynamics mode of GIZMO (`Hopkins 2015 <https://ui.adsabs.harvard.edu/abs/2015MNRAS.450...53H/abstract>`__) and computes gravitational forces using a modified version of the TreePM algorithm of `Springel 2005 <https://ui.adsabs.harvard.edu/abs/2005MNRAS.364.1105S/abstract>`__, including adaptive gravitational softenings.  Radiative cooling and photoionization are implemented using Grackle-3.1 (`Smith et al. 2017 <https://ui.adsabs.harvard.edu/abs/2017MNRAS.466.2217S/abstract>`__), stars form from molecular gas following `Krumholz & Gnedin (2011) <https://ui.adsabs.harvard.edu/abs/2011ApJ...729...36K/abstract>`__, and dust formation and evolution is modelled on-the-fly (`Li et al. 2019 <https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.1425L/abstract>`__). Stellar feedback includes two-phase galactic winds with their mass loading factor and velocity taken from the FIRE simulations (`Muratov et al. 2015 <https://ui.adsabs.harvard.edu/abs/2015MNRAS.454.2691M/abstract>`__; `Anglés-Alcázar et al. 2017b <https://ui.adsabs.harvard.edu/abs/2017MNRAS.470.4698A/abstract>`__).  SMBHs grow through cold gas accretion driven by gravitational torques (`Hopkins & Quataert 2011 <https://ui.adsabs.harvard.edu/abs/2011MNRAS.415.1027H/abstract>`__; `Anglés-Alcázar et al. 2017a <https://ui.adsabs.harvard.edu/abs/2017MNRAS.464.2840A/abstract>`__) and hot gas accretion following `Bondi 1952 <https://ui.adsabs.harvard.edu/abs/1952MNRAS.112..195B/abstract>`__.  Kinetic AGN feedback follows a two-mode approach with quasar winds transitioning into high-speed collimated jets at low Eddington accretion rates, and X-ray radiative feedback follows `Choi et al. (2012) <https://ui.adsabs.harvard.edu/abs/2012ApJ...754..125C/abstract>`__.

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

The simulations in the Swift-EAGLE suite have been run with the smoothed particle hydrodynamics and gravity code `Swift <https://arxiv.org/abs/2305.13380>`__. Swift is a parallel, open-source, versatile and modular code, with a range of hydrodynamics solvers, gravity solvers, and sub-grid models for galaxy formation (see `Swift website <https://swift.strw.leidenuniv.nl/>`__). In this suite we use the `SPHENIX <https://academic.oup.com/mnras/article/511/2/2367/6423434?login=true>`__  flavour of SPH, coupled with a modified version of the Evolution and Assembly of GaLaxies and their Environments (`EAGLE <https://virgo.dur.ac.uk/2014/11/11/EAGLE/index.html>`__) subgrid model for galaxy formation and evolution (see `Schaye et al. 2015 <https://academic.oup.com/mnras/article/446/1/521/1316115?login=true>`__ and `Crain et al. 2015 <https://academic.oup.com/mnras/article/450/2/1937/984366?login=true>`__). This includes element-by-element radiative cooling and heating rates from `Ploeckinger & Schaye 2020 <https://academic.oup.com/mnras/article/497/4/4857/5876367?login=true>`__, star formation (`Schaye & Dalla Vecchia 2008 <https://ui.adsabs.harvard.edu/abs/2008MNRAS.383.1210S/abstract>`__), stellar evolution and enrichment from `Wiersma  et al. 2009 <https://academic.oup.com/mnras/article/399/2/574/1059162?login=true>`__, and single thermal-mode feedback from massive stars and accreting AGN (see `Dalla Vecchia & Schaye 2012 <https://ui.adsabs.harvard.edu/abs/2012MNRAS.426..140D/abstract>`__, `Booth & Schaye 2009 <https://academic.oup.com/mnras/article/398/1/53/1092579?login=true>`__, `Rosas-Guevara et al. 2015 <https://academic.oup.com/mnras/article/454/1/1038/1143767?login=true>`__).

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/XDpBT6JwRAE?si=9-crxJZT31CEKei_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
   <br><br>
   


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

CROCODILE
~~~~~~~~~

The simulations in the CROCODILE suite have been run with the GADGET4-Osaka code (`Romano et al. 2022a <https://ui.adsabs.harvard.edu/abs/2022MNRAS.514.1441R/abstract>`_, `2022b <https://ui.adsabs.harvard.edu/abs/2022MNRAS.514.1461R/abstract>`_; `Oku & Nagamine 2024 <https://ui.adsabs.harvard.edu/abs/2024arXiv240106324O/abstract>`_), a proprietary modified version of the public GADGET-4 code (`Springel et al. 2021 <https://ui.adsabs.harvard.edu/abs/2021MNRAS.506.2871S/abstract>`_). GADGET4-Osaka uses TreePM to solve for gravity and the pressure-based entropy-conserving formulation of smoothed particle hydrodynamics (SPH) to solve for hydrodynamics. The SPH implementation includes artificial viscosity using velocity field reconstruction, artificial conduction, and a wake-up timestep limiter to ensure capturing subgrid physics effects in hydrodynamics. The CROCODILE implementation of galaxy formation physics includes radiative cooling and photoionization, star formation, stellar evolution considering a metallicity-dependent stellar initial mass function and hypernova fraction, dust evolution, stellar feedback, and supermassive black hole (SMBH) formation and feedback. Radiative gas cooling is implemented using the Grackle cooling library (`Smith et al. 2017 <https://ui.adsabs.harvard.edu/abs/2017MNRAS.466.2217S/abstract>`_) with the ultraviolet background radiation of `Haardt & Madau (2012) <https://ui.adsabs.harvard.edu/abs/2012ApJ...746..125H/abstract>`_. A non-thermal pressure floor is applied to prevent unphysical fragmentation. Dust production and destruction are modeled on-the-fly with 30 dust-size bins considering the diffusion of dust and metals (`Hirashita & Aoyama 2019 <https://ui.adsabs.harvard.edu/abs/2019MNRAS.482.2555H/abstract>`_; `Aoyama et al. 2020 <https://ui.adsabs.harvard.edu/abs/2020MNRAS.491.3844A/abstract>`_; `Romano et al. 2022a <https://ui.adsabs.harvard.edu/abs/2022MNRAS.514.1441R/abstract>`_). The stellar feedback includes supernova momentum input and galactic wind, which are modeled based on high-resolution simulations of superbubbles (`Oku et al. 2022 <https://ui.adsabs.harvard.edu/abs/2022ApJS..262....9O/abstract>`_; `Oku & Nagamine 2024 <https://ui.adsabs.harvard.edu/abs/2024arXiv240106324O/abstract>`_), as well as enrichment of 12 metal elements due to type-II and Ia supernovae and AGB stars implemented using the CELib chemical evolution library (`Saitoh 2017 <https://ui.adsabs.harvard.edu/abs/2017AJ....153...85S/abstract>`_). The mass, energy, and metal loading factors of the galactic wind are taken from the TIGRESS simulation (`Kim et al. 2020 <https://ui.adsabs.harvard.edu/abs/2020ApJ...903L..34K/abstract>`_). The SMBH growth rate is based on the torque- and Eddington-limited Bondi rate, and the associated AGN feedback is modeled as a stochastic thermal energy dump (`Rosas-Guevara et al. 2015 <https://ui.adsabs.harvard.edu/abs/2015MNRAS.454.1038R/abstract>`_; `Schaye et al. 2015 <https://ui.adsabs.harvard.edu/abs/2015MNRAS.446..521S/abstract>`_; `Crain et al. 2015 <https://ui.adsabs.harvard.edu/abs/2015MNRAS.450.1937C/abstract>`_) similarly to EAGLE simulations, but with varying parameters. The details of the CROCODILE subgrid model are described in the original paper by `Oku & Nagamine (2024) <https://ui.adsabs.harvard.edu/abs/2024arXiv240106324O/abstract>`_, which introduces a simulation set with varying combinations of both SN and AGN feedback.

Obsidian
~~~~~~~~

The Obsidian simulation `(Rennehan et al. 2024) <https://arxiv.org/abs/2309.15898>`__ was run with the GIZMO code using the same cooling, star formation, and stellar feedback subgrid physics as the original SIMBA simulation, presented in `Davé et al. 2019 <https://ui.adsabs.harvard.edu/abs/2019MNRAS.486.2827D/abstract>`__. However, Obsidian has a completely redesigned black hole accretion and feedback model, with a particularly unique "three regime" feedback scheme.  Obsidian uses the “Meshless Finite Mass” hydrodynamics mode of GIZMO `(Hopkins 2015) <https://ui.adsabs.harvard.edu/abs/2015MNRAS.450...53H/abstract>`__ and computes gravitational forces using a modified version of the TreePM algorithm of `Springel 2005 <https://ui.adsabs.harvard.edu/abs/2005MNRAS.364.1105S/abstract>`__, including adaptive gravitational softenings. Radiative cooling and photoionization are implemented using Grackle-3.1 (`Smith et al. 2017 <https://ui.adsabs.harvard.edu/abs/2017MNRAS.466.2217S/abstract>`__), stars form from molecular gas following `Krumholz & Gnedin (2011) <https://ui.adsabs.harvard.edu/abs/2011ApJ...729...36K/abstract>`__, and dust formation and evolution is modelled on-the-fly (`Li et al. 2019 <https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.1425L/abstract>`__). SMBHs grow via cold gas accretion with a simple scaling with the cold gas mass in the kernel (`Hopkins & Quataert 2011 <https://ui.adsabs.harvard.edu/abs/2011MNRAS.415.1027H/abstract>`__; `Anglés-Alcázar et al. 2017a <https://ui.adsabs.harvard.edu/abs/2017MNRAS.464.2840A/abstract>`__, `Qiu et al. 2019 <https://arxiv.org/abs/1810.01857>`__, `Wellons et al. 2023 <https://arxiv.org/abs/2203.06201>`__) and hot gas accretion following `Bondi 1952 <https://ui.adsabs.harvard.edu/abs/1952MNRAS.112..195B/abstract>`__. The black hole feedback is spin-dependent, and is split into three regimes: the slim disk regime, quasar regime, and advection dominated accretion flow (ADAF) regime. Each mode activates based on the SMBH accretion rate. The slim disk mode activates when the SMBH accretes above 30% the Eddington rate, the quasar between 3% and 30%, and the ADAF mode below 3% the Eddington rate. The slim disk and quasar modes are bipolar kinetic winds driven by radiation, with variable radiative efficiencies. In the ADAF mode, there is a thermal dump of energy based on the results in `Benson & Babul (2009) <https://arxiv.org/abs/0905.2378>`__, combined with a powerful Blandford-Znajek kinetic jet (`Blandford & Znajek 1977 <https://ui.adsabs.harvard.edu/abs/1977MNRAS.179..433B/abstract>`__, `Talbot et al. 2021 <https://arxiv.org/abs/2011.10580>`__, `Husko et al. 2023 <https://arxiv.org/abs/2206.06402>`__).

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/QD574jPq2qY?si=8py1xjsYXDF59hhX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
   <br><br>


N-body
~~~~~~

All the N-body simulations hve been run with the TreePM code `Gadget-III code <https://ui.adsabs.harvard.edu/abs/2005MNRAS.364.1105S/abstract>`__. The number of voxels in the PM grid is typically set to be 8 times that of the number of particles. The gravitational softening is set to :math:`1/40` of the mean inter-particle distance.  

The video below shows an example of a CAMELS-Nbody simulation:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/w0VPWIyc7Wk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   <br><br>
