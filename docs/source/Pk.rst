Power spectra
=============

For each simulation we have computed the power spectrum of the total matter at all available redshifts. For the hydrodynamic simulations we have also compute power spectra for the gas, dark matter, stars, and black-holes components at all redshifts.

The data is organized as follows:

- **IllustrisTNG**: This folder contains the power spectra of all the simulations of the IllustrisTNG suite.

- **IllustrisTNG_DM**: Each simulation in the IllustrisTNG suite has an N-body counterpart. This folder contains the power spectra of those simulations.

- **SIMBA**: This folder contains the power spectra of all the simulations of the SIMBA suite.

- **SIMBA_DM**: Each simulation in the SIMBA suite has an N-body counterpart. This folder contains the power spectra of those simulations.

- **Number_of_modes.txt**. This file contains the number of modes in each k-bin. See below.  

The files containing the power spectra are named as:

``Pk_type_z=Z.ZZ.txt``

where ``type`` can be ``m`` (for total matter), ``g`` (for gas), ``c`` (for dark matter), ``s`` (for stars), or ``bh`` (for black-holes). ``Z.ZZ`` is the redshift of the snapshot.

The data, a simple txt file, can be read as follows

.. code::  python 

   import numpy as np

   # get the name of the file with the power spectrum
   f_Pk = 'CAMELS/Pk/SIMBA/LH_456/Pk_g_z=0.00.txt'

   # read the data
   k, Pk = np.loadtxt(f_Pk, unpack=True)

   # k  contains the wavenumbers in h/Mpc
   # Pk contains the power spectra measurements in (Mpc/h)^3

Sometimes it is useful to know the number of modes in each k-bin (e.g. if one wants to rebin the measured power spectrum). The file ``Number_of_modes.txt`` contains that information:

.. code:: python

   import numpy as np

   # get the name of the file containing the number of modes
   f_in = 'CAMELS/Pk/Number_of_modes.txt'

   # read the file
   k, Nmodes = np.loadtxt(f_in, unpack=True)

   # k      contains the wavenumbers in h/Mpc
   # Nmodes contains the number of modes in each k-bin

   
