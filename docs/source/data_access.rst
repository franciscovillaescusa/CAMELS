************
Instructions
************

CAMELS data is stored at the Rusty cluster of the Flatiron Institute in New York City, and its data can be access through the Binder system. A partial copy of the data is also stored at the Tiger cluster at Princeton University.

We provide instructions on how to access the data below.

.. _contact us: camel.simulations@gmail.com

Data access policy
~~~~~~~~~~~~~~~~~~

CAMELS data is not publicly available yet. Its usage is regulated by the CAMELS data usage policy. If you would like to make use of this data for your research, please fill up this `form <https://docs.google.com/forms/d/1LMVUmCr_uWdPYTUXyw-C3gntam5BMLiBfzogu66QLbs/edit>`_.

We are working hard to make all the data publicly available as soon as possible.


Binder
~~~~~~

The `Flatiron Institute's Binder environment <https://binder.flatironinstitute.org/v2/user/sgenel/CAMELS/>`_ provides access to the CAMELS data and some basic computing resources for analysis. Some basic documentation can be found `here <https://docs.simonsfoundation.org/index.php/Public:Binder>`_.

.. warning::

   Please note that the Binder environment is ephemeral - after a few days of inactivity its contents are deleted, so one has to be vigilant about downloading any analysis results in time.
   
If you are interested in getting access this way, please `contact us`_, and let us know the Google account with which you've logged in, and we will grant you access.
​

Rusty
~~~~~

If you have an account on the Flatiron Institute's Rusty cluster, the data is located on: ``/mnt/ceph/users/camels/Sims``

.. code-block:: bash
		
   >> ls /mnt/ceph/users/camels/Sims
   CosmoAstroSeed_params_IllustrisTNG.txt  IllustrisTNG_SBI
   CosmoAstroSeed_params_SIMBA.txt         SCSAM
   data_products                           SIMBA
   IllustrisTNG                            SIMBA_DM
   IllustrisTNG_DM                         times.txt


Tiger
~~~~~

A partial copy of the data is located at the Tiger cluster of Princeton University. If you need access to the GPUs, please reach out to us to see if we can provide you an account on Tiger.
​
If you already have an account on Tiger, the data is located on: ``/projects/QUIJOTE/CAMELS``.

.. code-block::  bash

   >> ls /projects/QUIJOTE/CAMELS
   Analysis  Data_products  Documentation  Halos  Sims

​
