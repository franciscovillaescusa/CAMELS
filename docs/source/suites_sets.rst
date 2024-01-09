.. _suites_sets:

************
Organization
************

.. include:: sims.txt

The CAMELS simulations are organized into different suites, volumes, and sets depending on the code used to run them, their volume, and how the values of the cosmological parameters, the astrophysical parameters, and the initial random seeds are arranged. We refer the reader to :ref:`sims_description` for details on the number of simulations available per suite, volume, and set. The following scheme shows the way data is organized:

 .. image:: Sims_Scheme.png
    :alt: CAMELS Data structure


Knowing this structure is important to know where the data is located and which data to use for different tasks. For instance, the 25 Mpc/h IllustrisTNG simulations of the CV set are located in ``/Sims/IllustrisTNG/L25n256/CV``. 


Suites
~~~~~~

The CAMELS simulations are organized in different `suites`:

- | **IllustrisTNG**. This suite contains all hydrodynamic simulations that have been run with the `AREPO code <https://arxiv.org/abs/1909.04667>`_ employing the same subgrid physics as the original `IllustrisTNG <https://www.tng-project.org>`_ simulations. 
- | **SIMBA**. This suite contains all hydrodynamic simulations that have been run with the `GIZMO code <https://arxiv.org/abs/1409.7395>`_ employing the same subgrid physics as the original `SIMBA <http://simba.roe.ac.uk>`_ simulation.
- | **Astrid**. This suite contains all hydrodynamics simulations that have been run with the `MP-Gadget code <https://github.com/MP-Gadget/MP-Gadget>`_ employing the same subgrid physics as the original Astrid simulation (see `Ni et al. 2022 <https://ui.adsabs.harvard.edu/abs/2022MNRAS.513..670N/abstract>`__ and `Bird et al. 2022 <https://ui.adsabs.harvard.edu/abs/2022MNRAS.512.3703B/abstract>`__).
- | **Magneticum**. This suite contains all hydrodynamic simulations that have been run with the `Open-Gadget code <https://arxiv.org/abs/2301.03612>`_ using an updated version of the `Magneticum <http://www.magneticum.org/>`_ subgrid model. 
- | **Swift-EAGLE**. This suite contains all hydrodynamic simulations that have been run with the `Swift code <https://arxiv.org/abs/2305.13380>`_ using the `EAGLE subgrid physics model <https://eagle.strw.leidenuniv.nl/>`_ (see `Schaye et al. 2015 <https://arxiv.org/abs/1407.7040>`__ and `Crain et al. 2015 <https://arxiv.org/abs/1501.01311>`__). 
- | **Ramses**. This suite contains all hydrodynamic simulations that have been run with the `Ramses code <https://arxiv.org/abs/astro-ph/0111367>`_ using an state-of-the-art subgrid physics.
- | **Enzo**. This suite contains all hydrodynamic simulations that have been run with the `Enzo code <https://arxiv.org/abs/1307.2265>`_ using an state-of-the-art subgrid physics model.

We refer the reader to :ref:`Codes` for more details on the codes and subgrid physics models of the different suites.
  
.. Note::
  
   For every of the above suites, there is an collection of N-body simulations that represent the dark matter only counterparts of the above hydrodynamic simulations. For instance, **IllustrisTNG_DM** represents the N-body counterpart of the simulations in the **IllustrisTNG** suite.

   
Volumes
~~~~~~~

Each suite contains simulations run at different volumes and number of particles:

- | **L25n256**. All simulations follow the evolution of :math:`256^3` dark matter particles plus :math:`256^3` initial gas elements in a periodic comoving volume of :math:`(25~h^{-1}{\rm Mpc})^3`.
- | **L50n512**. All simulations follow the evolution of :math:`512^3` dark matter particles plus :math:`512^3` initial gas elements in a periodic comoving volume of :math:`(50~h^{-1}{\rm Mpc})^3`.
- | **L100n1024**. All simulations follow the evolution of :math:`1024^3` dark matter particles plus :math:`1024^3` initial gas elements in a periodic comoving volume of :math:`(100~h^{-1}{\rm Mpc})^3`.

.. Note::

   As of December 2023, most of the simulations belong to the ``L25n256`` category. As the CAMELS project matures and expands it will incorporate simulations at larger volumes. If there is no *volume* folder present, then the data should be considered to belong to the ``L25n256`` category.

  
   
Sets
~~~~

Each volume of each suite contains various simulation `sets`:

- | **SB**. This set contains at least 128 simulations. For instance, the Ramses suite contains 128 simulations while the IllustrisTNG suite contains 2048 simulations. Each simulation has a different value of the cosmological and astrophysical parameters, that are arranged in a Sobol sequence with :math:`2^N` elements, where :math:`N` is an integer number. Besides, each simulation has a different value of the initial random seed. This set will be named as ``SBX``, where is the number of dimensions; for the instance, the ``SB28`` set of the IllustrisTNG suite. SB stands for Sobol sequence. 
- | **LH**. This set contains 1,000 simulations. Each simulation has a different value of the cosmological and astrophysical parameters, that are arranged in a latin-hypercube. Each simulation has a different value of the random seed used to generate the initial conditions. LH stands for Latin-Hypercube.
- | **1P**. This set contains 4 simulations per parameter plus one fiducial. For example, in the IllustrisTNG suite we vary 28 parameters, so there are 113 simulations. For Ramses, where we only vary 5 parameters, we have 21 simulations. In this set, the value of the cosmological and astrophysical parameters in the simulations is varied only one at a time. The value of the random seed used to generate the initial conditions is the same in all simulations. This set is typically used to study the change induced by cosmology and astrophysics in a given quantity. 1P stands for 1-parameter at-a-time.
- | **CV**. This set contains 27 simulations. All the simulations share the value of the cosmological and astrophysical parameters (that are set to their fiducial values), and they only differ in the value of their initial conditions random seed. This set is typically used to study the effect of cosmic variance. CV stands for Cosmic Variance.
- | **EX**. This set contains 4 simulations. All simulations share the value of the cosmological parameters, but differ in the value of the astrophysical parameters. One simulation has fiducial values; the other three represent extreme cases with 1) very efficient AGN feedback, 2) very efficient supernova feedback, and 3) no feedback. All simulations share the value of the initial conditions random seed. This set can be used to study the maximum effect astrophysics can have on a given quantity. EX stands for Extreme.
- | **BE**. This set contains 27 simulations and is currently available only for the IllustrisTNG suite. All of these simulations share the exact same initial conditions with the 1P set and all are run with the fiducial model, but they use different random number sequences for the evolution of the simulation (not to be confused with the random seed that is used to generate the initial conditions). Hence, the differences between them represent the intrinsic randomness of the simulation results, which can serve as a benchmark for the performance of various predictive models. BE stands for Butterfly Effect.

We refer the reader to :ref:`params` for further details on the value and meaning of the varied parameters in the different sets.
  
.. Note::

   The SB and LH sets are very simular. The main difference is that SB uses a Sobol sequence to sample the parameter space while LH uses a Latin-hypercube. Given the fact that Sobol sequences have better properties to sample the parameter space than latin-hypercubes (e.g. it is very easy to expand the number of simulations, they sample the parameter space more uniformingly...etc), all new CAMELS simulations will use Sobol sequences instead of Latin-hypercubes. We keep the LH set for historical reasons, and while they are very useful for many things we encourage users to use SB sets (if available) instead of LH sets. 
   
