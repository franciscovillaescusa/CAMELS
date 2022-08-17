.. _Xrays:

******
X-Rays
******

The ``X-rays`` folder contains the X-rays data. The data is organized following the general hierarchical structure described in :ref:`suite_folders`.

We provide X-ray SIMPUT files for every halo above 10^12 M_solar for the 032 snapshot at z=0.05. Within each subdirectory containing a single simulation (e.g. ``LH_100``) is a directory for the snapshot, of which there is currently only one ``snap_032``.  For every FoF halo above 10^12 M_solar, there is a SIMPUT fits file of the form:

``IllustrisTNG.LH_100.snap_032.halo_010.100ks.z0.05.z_simput.fits``

in the directory structure:

``IllustrisTNG/LH_100/snap_032/``

within which halos are ordered by the FoF group ID in the group finder catalogue (e.g. ``halo_010``).

There exist a total of 160,693 halos:

-    5,939 IllustrisTNG_1P
-    2,003 IllustrisTNG_CV
-     342 IllustrisTNG_EX
-   75,340 IllustrisTNG_LH
-    5,157 SIMBA_1P
-    1,706 SIMBA_CV
-   70,206 SIMBA_LH
-  160,693 total

Each halo SIMPUT file consists of the main *simput* file, which is always the same size 11,520 bytes and represents the fits header, and a *phlist* file, which holds the photons and represents the fits data file:

``IllustrisTNG.LH_100.snap_032.halo_010.100ks.z0.05.z_simput.fits``

and

``IllustrisTNG.LH_100.snap_032.halo_010.100ks.z0.05.z_phlist.fits``

The pair of files, referred to as SIMPUT files, hold a Monte-Carlo-generated sample of photons produced by the `pyXSIM <https://hea-www.cfa.harvard.edu/~jzuhone/pyxsim/>`_ software package that would be collected in an aperture of 3,000 cm^2 over 100,000 seconds for the object placed at z=0.05. The SIMPUT file format is the standard file format used in simulations of X-ray observations, and serves as the input into other software that generates mock observations for a specific telescope, such as `SOXS <https://hea-www.cfa.harvard.edu/soxs/>`_ and `SIXTE <https://www.sternwarte.uni-erlangen.de/research/sixte/>`_.

It is helpful to have a background in X-ray simulation software to use these files.  The limited collecting aperture in exposure time (3,000 x 100,000 = 3e+08 cm^2 s) means that mock observation software cannot simulate longer observations, but it is very rare for a telescope to observe deeper than this (e.g. eROSITA has an effective area of 2000 cm^2 and scans the sky to an average exposure of 2,000 seconds).  While projected at z=0.05, it should be possible to scale the observation to be closer in the low redshift regime where received flux scales as z^-2.  Note that the cosmology sets the angular size and luminosity distances, which in this case is affected by the Omega_M parameter.

Because the analysis of the SIMPUT files is rather complex, we also provide a reduced data format in the form of a single file in the base X-rays directory:

``CAMELS.Xray.hdf5``

This file has hold projected soft X-ray (0.5-2.0 keV) surface brightness profiles in units of ergs s^-1 kpc^-2 in 7 logarithmic radial bins ranging from 10-1,280 kpc.  Each halo is in a hierarchical directory structure.
