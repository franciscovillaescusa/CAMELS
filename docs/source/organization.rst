.. _organization:

*****************
Data organization
*****************

CAMELS data is organized into different `type folders`:

- ``Sims``. This folder contains the raw output from the simulations.
- ``FOF_Subfind``. This folder contains the Subfind halo and subhalo catalogues.
- ``Rockstar``. This folder contains the Rockstar halo and subhalo catalogues.
- ``Pk``. This folder contains the power spectra measurements.
- ``Bk``. This folder contains the bispectra measurements.
- ``PDF``. This folder contains the PDF measurements.
- ``VIDE_Voids``. This folder contains the void catalogues.
- ``Lya``. This folder contains the Lyman-:math:`\alpha` spectra.
- ``X-rays``. This folder contains the X-rays files.
- ``Profiles``. This folder contains the halo radial profiles.
- ``CMD``. This folder contains the CAMELS Multifield Dataset (CMD).
- ``SCSAM``. This folder contains the data from CAMELS-SAM.

When possible, we have tried to organize the data inside the `type folders` in a self-similar way. Inside the `type folders`, there are typically four different `suite folders`:

- **IllustrisTNG**. This folder contains the data generated from the simulations of the IllustrisTNG suite
- **IllustrisTNG_DM**. This folder contains the data generated from the N-body counterparts of the simulations in the IllustrisTNG suite.
- **SIMBA**. This folder contains the data generated from the simulations of the SIMBA suite
- **SIMBA_DM**. This folder contains the data generated from the N-body counterparts of the simulations in the SIMBA suite.

.. Note::

   For some data products some `suite folders` may be missing. For instance, Lyman-:math:`\alpha` spectra can not be generated from N-body simulations. Thus, in that case, only the IllustrisTNG and SIMBA `suite folders` are present.

Inside a `suite folder` there are typically many `simulation folders`, that identify the simulation set and number associated to that particular simulation.
   
- ``1P_X``. These folders contain the data from 1P simulations. X ranges from 0 to 65.
- ``CV_X``. These folders contain the data from CV simulations. X ranges from 0 to 26.
- ``EX_X``. These folders contain the data from EX simulations. X ranges from 0 to 3.
- ``LH_X``. These folders contain the data from LX simulations. X ranges from 0 to 999.

Finally, inside a `simulation folder` the user can find the associated data for that particular simulation. We note that these folders can contain multiple files, e.g. the power spectra of the considered simulations at all redshifts.

The image below shows an scheme with the above generic data structure.
  
.. image:: Scheme_data_release.pdf
   :alt: Generic data structure

.. Warning::

   There are some data products that are organized in a different way to the one outlined above. For instance, the CAMELS Multifield Dataset (CMD) follows a different data structure. In these cases we describe in detail the structure of those data products.


