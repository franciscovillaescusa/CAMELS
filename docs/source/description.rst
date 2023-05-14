*******************
General description
*******************

As of May 15th 2023, CAMELS contains 10,680 cosmological simulations: 5,164 N-body and 5,516 hydrodynamic simulations.

All simulations follow the evolution of :math:`256^3` dark matter particles and :math:`256^3` gas resolution elements (only for the (magneto-)hydrodynamic) within a periodic comoving volume of :math:`(25~h^{-1}{\rm Mpc})^3` from :math:`z=127` down to :math:`z=0`. We store multiple snapshots and also multiple post-processed data such as halo catalogs, power spectra...etc; see :ref:`organization`.

All N-body simulations have been run with the Gadget-III code, while the hydrodynamic simulations have been run with different codes: AREPO, GIZMO, MP-Gadget, OpenGadget, SWIFT, Ramses, and Enzo. The simulations can be classified into suites and sets, depending on the code used to run them and how their parameters are organized. See :ref:`suites_sets` for details. See :ref:`Codes` for details on the different codes and subgrid physics models available in CAMELS.

See :ref:`sims_chart` to see how many simulations are available as a function of suite and set. The value of the cosmological, astrophysical, and initial random seed of the different simulations can be found :ref:`params`. The redshifts associated to the different simulations snapshots can be found here :ref:`redshifts`.


