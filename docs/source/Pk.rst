Power spectra
=============

The ``Pk`` folder contains the power spectra. The data is organized following the general hierarchical structure described in :ref:`suite_folders`.


For each simulation we povide the power spectrum of the total matter at all available redshifts. For the hydrodynamic simulations we have also provide power spectra for the gas, dark matter, stars, and black-holes components at all redshifts. The files containing the power spectra are named as:

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

For snapshots at redshift zero, we additionally compute the power spectrum on all scales up to k = 1000 h/Mpc, with the small-computations performed using the `HIPSTER <https://github.com/oliverphilox/HIPSTER/>`_ code. This computes the Legendre multipoles of the power spectrum, P_ell(k), with a linear binning for k < 25 h/Mpc, and a logarithmic binning beyond. 

All-scale spectra are computed for each LH simulation from the IllustrisTNG, IllustrisTNG_DM and SIMBA suites in both real- and redshift-space and take the form ``Pk_type_allk_rsd_z=Z.ZZ.txt``, where ``rsd`` specifies the treatment of redshift-space distortions, either unspecified (real-space), or ``RSDX`` for distortions added along axis X. The file headers contain a variety of useful information about the sample and method hyperparameters.

As an example, the all-scale power spectrum of gas from simulation 42 in redshift-space is read in as follows:

.. code:: python

   import numpy as np

   # get the name of the file with the power spectrum
   f_Pk = 'CAMELS/Pk/IllustrisTNG/LH_42/Pk_g_allk_RS2_z=0.00.txt'

   # read the data
   k, Pk0, Pk2, Pk4 = np.loadtxt(f_Pk, unpack=True)

   # k  contains the wavenumbers in h/Mpc
   # Pk0 contains the power spectra monopole measurements in (Mpc/h)^3
   # Pk2 contains the power spectra quadrupole measurements in (Mpc/h)^3
   # Pk4 contains the power spectra hexadecapolef measurements in (Mpc/h)^3

All scale spectra can be computed for additional samples upon request.
