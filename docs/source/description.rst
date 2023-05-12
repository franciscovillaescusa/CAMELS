***************
Suites and sets
***************

CAMELS contains 10,421 simulations: 5,097 N-body simulations and 5,324 hydrodynamic simulations. The simulations can be classified into different suites and sets depending on the code used to run them and how the values of the cosmological parameters, the astrophysical parameters, and the initial random seeds are arranged. The following scheme shows the way data is organized:

 .. image:: Sims_Scheme.png
    :alt: CAMELS Data structure



Suites
~~~~~~

The CAMELS simulations are organized in different `suites`:

- **IllustrisTNG**. This suite contains 1,092 hydrodynamic simulations that have been run with the AREPO code employing the same subgrid physics as the original `IllustrisTNG <https://www.tng-project.org>`_ simulations. 
- **SIMBA**. This suite contains 1,092 hydrodynamic simulations that have been run with the GIZMO code employing the same subgrid physics as the original `SIMBA <http://simba.roe.ac.uk>`_ simulation.
- **Astrid**. This suite contains 1,092 hydrodynamics simulations have that been run with the MP-Gadget code employing the same subgrid physics as the original Astrid simulation (see `this paper <https://ui.adsabs.harvard.edu/abs/2022MNRAS.513..670N/abstract>`__ and `this paper <https://ui.adsabs.harvard.edu/abs/2022MNRAS.512.3703B/abstract>`__).
- **N-body**. This suite contains 3,049 N-body simulations. For each CAMELS hydrodynamic simulation there is an N-body simulation with the same cosmology and value of the initial random seed as its hydrodynamic counterpart.

.. Note::

   All the simulations in the IllustrisTNG, SIMBA, and N-body suites are publicly available (see :ref:`data_access`). To access the data from the Astrid suite please fill up `this form <https://forms.gle/XMVwuzhCMvnhFiaHA>`_.

   
Sets
~~~~

Each simulation suite contains various simulation `sets`:

- | **LH**. This set contains 1,000 simulations. Each simulation has a different value of the cosmological and astrophysical parameters, that are arranged in a latin-hypercube. Each simulation has a different value of the random seed used to generate the initial conditions. This set represents the main CAMELS dataset. LH stands for Latin-Hypercube.
- | **1P**. This set contains 61 simulations. In this set, the value of the cosmological and astrophysical parameters in the simulations is varied only one at a time. The value of the random seed used to generate the initial conditions is the same in all simulations. This set is typically used to study the change induced by cosmology and astrophysics in a given quantity. 1P stands for 1-parameter at a time.
- | **CV**. This set contains 27 simulations. All the simulations share the value of the cosmological and astrophysical parameters, and they only differ in the value of their initial conditions random seed. This set is typically used to study the effect of cosmic variance. CV stands for Cosmic Variance.
- | **EX**. This set contains 4 simulations. All simulations share the value of the cosmological parameters, but differ in the value of the astrophysical parameters. One simulation has fiducial values; the other three represent extreme cases with 1) very efficient supernova feedback, 2) very efficient AGN feedback, and 3) no feedback. All simulations share the value of the initial conditions random seed. This set can be used to study the maximum effect astrophysics can have on a given quantity. EX stands for Extreme.
- | **BE**. This set contains 27 simulations and is currently available only for the IllustrisTNG suite. All of these simulations share the exact same initial conditions with the 1P set and all are run with the fiducial model, but they use different random number sequences for the evolution of the simulation (not to be confused with the random seed that is used to generate the initial conditions). Hence, the differences between them represent the intrinsic randomness of the simulation results, which can serve as a benchmark for the performance of various predictive models. BE stands for Butterfly Effect.

	  
Characteristics
~~~~~~~~~~~~~~~
	  
All simulations follows the evolution of :math:`256^3` dark matter particles and :math:`256^3` gas resolution elements (only for the (magneto-)hydrodynamic) within a periodic comoving volume of :math:`(25~h^{-1}{\rm Mpc})^3` from :math:`z=127` down to :math:`z=0`. 

