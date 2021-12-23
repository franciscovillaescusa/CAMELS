Profiles
=============

For each snapshots, we provide three-dimensional spherically-averaged profiles of gas density, thermal pressure, gas mass-weighted temperature, and gas mass-weighted metallicity for the 1P, LH, and CV runs for both IllustrisTNG and SIMBA.  

Specifically, we use `illstack_CAMELS <https://github.com/emilymmoser/illstack_CAMELS>`_, a CAMELS-specific version  of the original, more general code `illstack <https://github.com/marcelo-alvarez/illstack>`_ to generate the three-dimensional profiles, extending radially from 0.01-10 comoving Mpc in 25 log_{10} bins. The profiles are stored in hdf5 format which can be read with the python script provided in the repository.

The profiles are located in

``Profiles/suite/sim/suite_sim_#.hdf5``

where ``suite`` is either ``IllustrisTNG`` or ``SIMBA``, ``sim`` is the simulation of interest, and ``#`` is the snapshot number.  

.. code::  python

  
