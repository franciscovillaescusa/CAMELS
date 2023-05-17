.. _Codes:

*****************
Simulations codes
*****************

As discussed in :ref:`suites_sets`, the CAMELS simulations can be classified into different suites depending on the code and subgrid model used to run them. Below we provide some details on the codes, physics, and subgrid models employed.

IllustrisTNG
~~~~~~~~~~~~

The simulations in the IllustrisTNG suite have been run with the Arepo code using the same subgrid physics as the IllustrisTNG simulation. Arepo uses TreePM to solve for gravity and a moving Voronoi mesh to solve for ideal magnetohydrodynamics (MHD). The IllustrisTNG galaxy formation physics implementation includes sub-grid models for star-formation, stellar evolution and galactic winds, as well as supermassive black hole (SMBH) seeding, merging, accretion and feedback. The latter operates in two modes, selected based on SMBH mass and Eddington ratio, where the high-accretion mode is thermal and the low accretion mode is kinetic and is the more efficient one in ejecting gas and quenching massive galaxies. The galactic winds feedback is kinetic, implemented via briefly hydrodynamically decoupled wind particles, with energy and mass loading factors that are prescribed based on local velocity dispersion and metallicity.

SIMBA
~~~~~

The simulations in the SIMBA suite have been run with GIZMO code using the same subgrid physics as the SIMBA simulation.

Astrid
~~~~~~

The simulations in the Astrid suite have been run with the MP-Gadget code using the same subgrid physics as the Astrid simulation.

Magneticum
~~~~~~~~~~

The simulations in the Magneticum suite have been run with the OpenGadget code using an updated and improved version of the Magneticum simulation.

SWIFT-EAGLE
~~~~~~~~~~~

The simulations in the SWIFT-EAGLe suite have been run with the SWIFT code using a subgrid model that approximates the one of the EAGLE simulation.

Ramses
~~~~~~

The simulations in the Ramses suite have been run with the Ramses code.

Enzo
~~~~

The simulations in the Enzo suite have been run with the Enzo code.

N-body
~~~~~~

All the N-body simulations hve been run with the Gadget-III code.
