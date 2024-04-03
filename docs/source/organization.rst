.. _organization:

*****************
Data organization
*****************

CAMELS data is organized in a hierarchical way.

Type folders
~~~~~~~~~~~~

At the highest level, CAMELS contains different `type folders`:

- ``Sims``. This folder contains the raw output from the simulations.
- ``FOF_Subfind``. This folder contains the Subfind halo and subhalo catalogues.
- ``Rockstar``. This folder contains the Rockstar halo and subhalo catalogues.
- ``Caesar``. This folder contains the CAESAR halo and subhalo catalogues.
- ``AHF``. This folder contains the AMIGA Halo Finder (AHF) halo and subhalo catalogues.
- ``Pk``. This folder contains the power spectra measurements.
- ``Bk``. This folder contains the bispectra measurements.
- ``PDF``. This folder contains the PDF measurements.
- ``VIDE_Voids``. This folder contains the void catalogues.
- ``Lya``. This folder contains the Lyman-:math:`\alpha` spectra.
- ``X-rays``. This folder contains the X-rays files.
- ``Profiles``. This folder contains the halo radial profiles.
- ``CMD``. This folder contains the CAMELS Multifield Dataset (CMD).
- ``SCSAM``. This folder contains the data from CAMELS-SAM.

When possible, we have tried to organize the data inside the `type folders` in a self-similar way.


.. _suite_folders:

Suite folders
~~~~~~~~~~~~~

Inside the considered `type folder`, there are different `suite folders`:

- ``IllustrisTNG``. This folder contains the data generated from the simulations of the IllustrisTNG suite
- ``IllustrisTNG_DM``. This folder contains the data generated from the N-body counterparts of the simulations in the IllustrisTNG suite.
- ``SIMBA``. This folder contains the data generated from the simulations of the SIMBA suite
- ``SIMBA_DM``. This folder contains the data generated from the N-body counterparts of the simulations in the SIMBA suite.
- ``Astrid``. This folder contains the data generated from the simulations of the Astrid suite.
- ``Astrid_DM``. This folder contains the data generated from the N-body counterparts of the simulations in the Astrid suite.
- ``Magneticum``. This folder contains the data generated from the simulations of the Magneticum suite.
- ``Magneticum_DM``. This folder contains the data generated from the N-body counterparts of the simulations in the Magneticum suite.
- ``EAGLE``. This folder contains the data generated from the simulations of the Swift-EAGLE suite.
- ``EAGLE_DM``. This folder contains the data generated from the N-body counterparts of the simulations in the Swift-EAGLE suite.
- ``Ramses``. This folder contains the data generated from the simulations of the Ramses suite.
- ``Ramses_DM``. This folder contains the data generated from the N-body counterparts of the simulations in the Ramses suite.
- ``Enzo``. This folder contains the data generated from the simulations of the Enzo suite.
- ``Enzo_DM``. This folder contains the data generated from the N-body counterparts of the simulations in the Enzo suite.

.. Note::

   For some data products some `suite folders` may be missing. For instance, Lyman-:math:`\alpha` spectra are not generated from N-body simulations. Thus, in that case, only the IllustrisTNG and SIMBA `suite folders` are present.

.. _volume_folders:

Volume folders
~~~~~~~~~~~~~~

Inside a `suite folder` there three different `volume folders`:

- ``L25n256``. This folder contains the data from the simulations with :math:`256^3` dark matter particles (plus :math:`256^3` initial gas elements if hydrodynamic) in a periodic box of :math:`25~h^{-1}{\rm Mpc}` side.
- ``L50n512``. This folder contains the data from the simulations with :math:`512^3` dark matter particles (plus :math:`512^3` initial gas elements if hydrodynamic) in a periodic box of :math:`50~h^{-1}{\rm Mpc}` side.
- ``L100n1024``. This folder contains the data from the simulations with :math:`1024^3` dark matter particles (plus :math:`1024^3` initial gas elements if hydrodynamic) in a periodic box of :math:`100~h^{-1}{\rm Mpc}` side.


.. Note::

   Note that not all simulations, and its associated data, are available. For instance, as of April 2024, for most of the suites, ``L25n256`` is pretty complete, while ``L50n512`` only contains IllustrisTNG simulations and there are no simulations in the ``L100n1024`` volume for any suite.

   
   
.. _set_folders:
   
Set folders
~~~~~~~~~~~
   
Inside a `volume folder` there are several `set folders`:

- ``SB``. This folder contains the data from the simulations of the SB set. Typically, we will add a number of this set to identify the number of parameters varied. For instance, ``SB28`` in the case of IllustrisTNG to denote that 28 parameters are varied in a sobol sequence. Inside this folder, there are subfolders named ``SBN_X``, where ``N`` is the number of parameters varied (e.g. 28 in the case of IllustrisTNG), and ``XX`` ranges from ``0`` to a multiple of 2 (e.g. 2048 for IllustrisTNG-SB28, 256 for Ramses-SB5...etc).
- ``LH``. This folder contains the data from the simulations of the LH set. Inside this folder, there are subfolders named ``LH_X``, where where ``X`` ranges from ``0`` to ``999``.
- ``1P``. This folder contains the data from the simulations of the 1P set. Inside this folder, there are subfolders named ``1P_pX_``, where ``X`` ranges from ``1`` to ``N`` while ``Y`` goes from ``n2`` (-2) to ``2``. Where ``N`` is the number of parameters (e.g. 28 in IllustrisTNG, 6 in Astrid...etc).
- ``CV``. This folder contains the data from the simulations of the CV set. Inside this folder, there are subfolders named ``CV_X``, where ``X`` ranges from ``0`` to ``26``.
- ``EX``. This folder contains the data from the simulations of the EX set. Inside this folder, there are subfolders named ``EX_X``, where ``X`` ranges from ``0`` to ``3``.
- ``BE``. This folder contains the data from the simulations of the BE set. Inside this folder, there are subfolders named ``BE_X``, where ``X`` ranges from ``0`` to ``26``.


.. note::
   The IllustrisTNG suite folder contains a new set of zoom-in simulations under the simulation folder ``zoom``. See :ref:`zoomGZ` for more details.

As can be seen, the name of the folder can be used to identify the simulation set and its parameters.
  
.. note::

   The numeric scheme of the 1P set labels was chosen to help the user to identify which parameter and its variation is the one considered. This may be more useful than just listing the simulations from 0 to, e.g., 65. We refer the reader to :ref:`params` for the actual value of the parameters in each simulation.

Actual data
~~~~~~~~~~~
   
Finally, inside a `set folder` the user can find the associated data for that particular simulation. We note that these folders can contain multiple files, e.g. the power spectra of the considered simulations at all redshifts.

The image below shows an scheme with the generic data structure for the case of the power spectra:
  
.. image:: Scheme_data_release.png
   :alt: Generic data structure

.. Warning::

   There are some data products that are organized in a different way to the one outlined above. For instance, the CAMELS Multifield Dataset (CMD) follows a different data structure. In these cases we describe in detail the structure of those data products.


