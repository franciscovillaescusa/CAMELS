Lyman-alpha spectra
===================

The ``Lya`` folder contains the mock Lyman-:math:`\alpha` spectra. The data is organized following the general hierarchical structure described in :ref:`suite_folders`.


For each simulation snapshot we provide Lyman-alpha spectra for 5,000 random sightlines. These spectral lines are contained within an hdf5 file and can be read using the same code they were generated with.

The data is organized such that the spectra corresponding to a snapshot resides in an appropriately named folder within the simulation folder. The spectra files are located at

``suite/sim/SPECTRA_0##/Lya-spectra.hdf5``

where ``suite`` can be either ``IllustrisTNG`` or ``SIMBA``, ``sim`` is the simulation of interest, and ``##`` is the snapshot number (for snapshot numbers 0 through 9, a 0 must pad the front). For example ``IllustrisTNG/1P_1_n5/SPECTRA_001/Lya-spectra.hdf5`` is the Lyman-alpha spectra for the IllustrisTNG suite ``1P_1_n5`` simulation at redshift 5.

The easiest way to read the data is using the same code that generated the spectra; see the `Fake Spectra <https://github.com/sbird/fake_spectra>`_ GitHub for instructions on how to install it. The data can then be read as follows:

.. code::  python

   from fake_spectra.plot_spectra import PlottingSpectra

   # We use their plotting routine to read in the data.
   fs = PlottingSpectra(num=1, base="suite/sim", savefile="Lya-spectra.hdf5", label="My label")

   # num       the simulation snapshot number as an integer (you should not pad numbers 0 through 9 for num)
   # base      the directory that the SPECTRA_0## directory is located in
   # savefile  the name of the spectra file (they are all "Lya-spectra.hdf5")
   # label     an identifier for your spectra (this is usually unimportant)

It is important to note that when given the information above, the code is looking for ``base/SPECTRA_0num/savefile`` (where ``num`` is padded automatically with a 0 by the code if num is 0 through 9). Because of this the user is cautioned to ensure that the spectra file remains in a directory called ``SPECTRA_0num``. This will not be a problem unless you restructure the snapshot data after download or downloaded just the spectra file.

Once the data is loaded in, the user can retrieve optical depths for one or all of the spectral lines in the file:

.. code::  python

   from fake_spectra.plot_spectra import PlottingSpectra
   import numpy as np

   # Loading in spectra for the IllustrisTNG suite, 1P_4_3 simulation, and snapshot 001.
   fs = PlottingSpectra(num=1, base="IllustrisTNG/1P_4_3", savefile="Lya-spectra.hdf5", label="My label")

   # To retrieve optical depths for all 5000 spectral lines:
   taus = fs.get_tau("H", 1, 1215)
   # The arguments entered above correspond to hydrogen Lyman-alpha. Changing these would result in errors.

   # To retrieve optical depths for a single spectral line:
   tau = fs.get_tau("H", 1, 1215, 0)
   # The last argument indicates which line you want tau for. This can be anywhere from 0 to 4999.

   # Flux is proportional to e^-tau:
   flux = np.exp(-tau)

  # To plot flux as a function of relative velocity, calculate the relative velocity array:
   rel_v = ( np.arange(0, np.size(tau)) ) * fs.dvbin

The spectra is available for both the IllustrisTNG and SIMBA suites for all the simulation sets at all redshifts. See the CAMELS data structure documentation for details on available simulations.

Additional spectra samples can be calculated for the simulations using the `Fake Spectra <https://github.com/sbird/fake_spectra>`_ code; the code also has an assortment of useful plotting methods, see the documentation for further details.
