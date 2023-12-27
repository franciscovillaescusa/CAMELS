*******************
General description
*******************

.. include:: sims.txt

All simulations follow the evolution of :math:`256^3` dark matter particles and :math:`256^3` gas resolution elements (only for the hydrodynamic) within a periodic comoving volume of :math:`(25~h^{-1}{\rm Mpc})^3` from :math:`z=127` down to :math:`z=0`.

.. Note::

   CAMELS is expanding and will soon contain simulations with :math:`512^3` dark matter particles and :math:`512^3` gas resolution elements in periodic boxes of :math:`(50~h^{-1}{\rm Mpc})^3`. 

For each simulation, we store multiple snapshots. We also keep a variety of post-processed data such as halo catalogs, power spectra...etc; see :ref:`organization`.

All N-body simulations have been run with the Gadget-III code, while the hydrodynamic simulations have been run with different codes: AREPO, GIZMO, MP-Gadget, OpenGadget, SWIFT, Ramses, and Enzo. See :ref:`Codes` for details on the different codes and subgrid physics models available in CAMELS.

The simulations can be classified into suites and sets, depending on the code used to run them, their volume, and how their parameters are organized. See :ref:`suites_sets` for details. 

See :ref:`sims_chart` to see how many simulations are available as a function of suite and set. The value of the cosmological, astrophysical, and initial random seed of the different simulations can be found :ref:`params`. The redshifts associated to the different simulations snapshots can be found here :ref:`redshifts`.


