.. _PDF:

**********************************
Probability distribution functions
**********************************

The ``PDF`` folder contains the estimated probability distribution functions (PDFs). The data is organized following the general hierarchical structure described in :ref:`suite_folders`.

We provide PDFs for all the 3D grid files in the CAMELS Multifield Dataset (CMD) (See :ref:`CMD`), each containing 1,000 grids from the LH set.

The PDFs are stored as ``.npy`` files and they are named as ``hist_Grids_prefix_sim_LH_grid_z=redshift.npy``, where ``prefix`` is the word identifying
each field (``HI``, ``Vgas``, etc.), ``sim`` can be ``IllustrisTNG``, ``SIMBA``, ``Nbody_IllustrisTNG``, or ``Nbody_SIMBA``, ``grid`` can be 
``128``, ``256``, or ``512`` and ``redshift`` can be 0, 0.5, 1, 1.5 or 2. These files can be read with numpy as follows:

.. code:: python

   import numpy as np

   # name of the pdf file
   pdfgrids = 'hist_Grids_HI_SIMBA_LH_128_z=0.00.npy'

   # read the data
   pdf = np.load(pdfgrids) #--shape of pdf is (1000,500)
   
   # get the bin counts for the 4th grid
   print(pdf[3])
   
   
The file contains 1,000 entries with 500 values per entry denoting the number of counts in 500 bins for that entry. See the CAMELS data release for more details on how the PDFs are calculated.
