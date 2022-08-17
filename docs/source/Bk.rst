Bispectra
===========

The ``Bk`` folder contains the bispectra measurements. The data is organized following the general hierarchical structure described in :ref:`suite_folders`.

For each simulation of the latin hypercube sets we have computed the bispectrum of the total matter at redshift zero. For the hydrodynamic simulations we have also compute bispectra for the gas and dark matter at redshift zero. We do not compute bispectra of the stellar or black-hole components, due to the small number of particles in those datasets, hence the low signal-to-noise.

Bispectra are computed using two approaches. At low-k, the spectra are computed using an FFT-based approach, as implemented in the `Pylians <https://github.com/franciscovillaescusa/Pylians/>`_ code. This estimates B(k1, k2, mu), where mu is the angle between k1 and k2. Data are assigned to a 128 x 128 x 128 grid, using triangular-shaped-cloud interpolation, before the bispectra are computed for a range of k values up to k = 5 h/Mpc.

At high-k, the FFT-based approach is inefficient, since it requires a large FFT grid. In this case, we compute bispectra using the `HIPSTER <https://github.com/oliverphilox/HIPSTER/>`_ code, which uses a configuration-space estimator to extend to small scales without computational penalties (strictly via a convolution with a smooth window which is of negligible importance on small scales). This estimates the Legendre multipoles of the bispectrum, B_ell(k1, k2), for a range of ell up to ell = 5 and k from 0 to 50 h/Mpc. Additional details of the method hyperparameters can be found in the bispectrum headers.

The files containing the power spectra are named as:

``Pk_type_method_rsd_z=0.00.txt``

where ``type`` can be ``m`` (for total matter), ``g`` (for gas), or ``c`` (for dark matter). ``method'' is either ``lowk`` or ``highk``, indicating the two regimes given above, and ``rsd`` specifies the treatment of redshift-space distortions, either unspecified (real-space), or ``RSDX`` for distortions added along axis X. The file headers contain a variety of useful information about the sample.

The data is simply given as a set of text files. For the low-k spectra:

.. code::  python 

   import numpy as np

   # get the name of the file with the low-k bispectrum (here for CDM in real-space)
   f_Bk = 'CAMELS/Bk/IllustrisTNG/LH_456/Bk_c_lowk_z=0.00.txt'

   # read the angular bins
   mu_arr =  np.loadtxt(f_Bk,max_rows=1)  
   # read the bispectrum
   data = np.loadtxt(f_Bk,skiprows=15)
   k1, k2, Bk = data[:,0], data[:,1], data[:,2:]

   # k1, k2  contain the wavenumbers in h/Mpc
   # Bk contains the bispectrum measurements in (Mpc/h)^6 for each k1, k2 pair (row) and mu bin (column)

Whilst for the high-k spectra:

.. code::  python 

   import numpy as np

   # get the name of the file with the low-k bispectrum (here for gas using redshift-space axis 2)
   f_Bk = 'CAMELS/Bk/IllustrisTNG/LH_456/Bk_g_lowk_RS2_z=0.00.txt'

   # read the bispectrum
   data = np.loadtxt(f_Bk)
   k1, k2, Bk = data[:,0], data[:,1], data[:,2:]   
   # load the angular multipoles
   ells = np.arange(len(Bk[0]))

   # k1, k2  contain the wavenumbers in h/Mpc
   # Bk contains the bispectrum multipole measurements in (Mpc/h)^6 for each k1, k2 pair (row) and multipole ell (column).
