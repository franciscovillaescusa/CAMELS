.. _subfind:

*******************
Photometry catalogs
*******************

Photometric catalogues for a number of simulations in the CAMELS suite have been produced using the `Synthesizer <https://flaresimulations.github.io/synthesizer/>`_ code.

The data is organized following the general hierarchical structure described in :ref:`suite_folders`. CAMELS provides a photometric catalogue for each simulation. Each catalog is stored as an hdf5 file; ``h5py`` is needed in order to read these files using python. 

Full details on the forward modelling procedure used to produce the photometry is provided in *Lovell et al. in prep.*. In short, the star formation and metal enrichment history represented by the star particle data is coupled with a stellar population synthesis model to produce the *intrinsic* spectra. A fixed screen dust model is then applied, which applies additional attenuation to young stellar populations, to produce the *attenuated* spectra. These are then convolved with observer- and rest-frame filters to produce the photometric luminosities and observed fluxes.  The integrated photometry is generated for each subhalo (identified through SUBFIND) containing more than 10 star particles.

Each catalog file has the following hierarchical structure:

``{snapshot}/{sps_model}/{format}/{emission}/{spectra_type}/{filter}``

Where each property is defined as follows:

- ``snapshot``: Snapshot of the simulation
- ``sps_model``: stellar population synthesis model, currently either ``BC03`` or ``BPASS``.
- ``format``: format of the emission output, currently only ``photometry`` available.
- ``emission``: specify whether we want rest-frame ``luminosity``, or observer-frame ``flux``.
- ``spectra_type``: the form of the spectra, currently only ``intrinsic`` for pure stellar emission, or ``attenuated`` for dust attenuated emission.
- ``filter``: filter code, as specified by the `SVO database <http://svo2.cab.inta-csic.es/theory/fps/>`_.


For example, to view the rest-frame filters available at $z = 0.1$ (snapshot 086) using the dust attenuated BC03 model:

.. code-block:: bash

   >> h5ls Photometry/IllustrisTNG/L25n256/LH/IllustrisTNG_LH_0_photometry.hdf5/snap_086/BC03/photometry/luminosity/attenuated
    GALEX\ FUV               Dataset {529}
    GALEX\ NUV               Dataset {529}
    Generic                  Group
    HST                      Group
    JWST                     Group
    SLOAN                    Group
    UKIRT                    Group
    UV1500                   Dataset {529}
    UV2800                   Dataset {529}

.. Note::
   
      The full list of filters provided are as so:
      
      - GALEX FUV & NUV bands
      - Top-hat filters centred at 1500 Å and 2800 Å
      - SDSS ugriz
      - UKIRT UKIDSS YJHK
      - Johnson UBVJ
      - HST ACS F435W, F606W, F775W, F814W, and F850LP
      - HST WFC3 F098M, F105W, F110W, F125W, F140W and F160W
      - JWST NIRCam F070W, F090W, F115W, F150W, F200W, F277W, F356W and F444W

Additionally, under each ``snapshot`` group there is a dataset called ``SubhaloIndex`` which specifies the integer index of the object in the original subfind tables.


.. Note::

   These files are structured identically for all simulations run so far. These include IllustrisTNG, Simaba, Swift-EAGLE and Astrid.


Reading these files with python is straightforward. Below we show an example of reading the photometric catalogue and some subfind properties, and using the ``SubhaloIndex`` to match them.

.. code-block:: python

   import numpy as np
   import h5py

   # Snapshot number
   snap = '090'

   # Subfind catalog name
   group_catalog = f'IllustrisTNG/L25n256/LH/groups_{snap}.hdf5'
  
   # Photometric catalog name
   photo_catalog = 'IllustrisTNG/L25n256/LH/IllustrisTNG_LH_0_photometry.hdf5'

   # Value of the scale factor
   scale_factor = 1.0
   
   # open the catalogue
   with h5py.File(photo_catalog, "r") as hf:

       # Get the subhalo index
       subhalo_index = np.array(hf[f"snap_{snap}/SubhaloIndex"][:], dtype=int)

       # Get the g-band magnitude
       g_band = hf[f"snap_{snap}/BC03/photometry/luminosity/attenuated/SLOAN/SDSS.g"][:]

   # Read the stellar masses of the subhalos/galaxies
   with h5py.File(group_catalog, "r") as hf:
      M_star = hf['Subhalo/SubhaloMassType'][:,4]*1e10 # Stellar masses in Msun/h

   # Filter stellar masses using the subhalo index
   M_star = M_star[subhalo_index]  
