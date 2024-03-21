.. _caesar:

***************
CAESAR catalogs
***************

The folder ``Caesar`` contains the CAESAR halo and galaxy catalogs. The data is organized following the general hierarchical structure described in :ref:`suite_folders`.


CAESAR computes a large number of properties for each halo and galaxy, including physical properties such as masses and sizes of each component, dynamical properties such as velocity dispersions, and photometric properties using the `FSPS <https://dfm.io/python-fsps>`_ package. The structure of the data is the generic one outlined in :ref:`organization`. There is one CAESAR catalog for each snapshot of each hydrodynamic simulation in CAMELS.

For each snapshot CAESAR generates two files:

- ``fof6d_newsnaps_0XX``. This file contains the galaxies identified using the 6D Friends-of-Friends (FoF) algorithm. ``XX`` represents the snapshot number (from 00 to 33).
- ``caesar_newsnaps_0XX.hdf5``. This file is the actual CAESAR catalog. ``XX`` represents the snapshot number (from 00 to 90).

The user can find details on how to read and manipulate CAESAR catalogs in the `CAESAR documentation <https://caesar.readthedocs.io>`_. 
  
