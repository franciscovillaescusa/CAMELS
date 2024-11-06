CAMELS
======

**CAMELS** stands for **C**\osmology and **A**\strophysics with **M**\achin\ **E** **L**\earning **S**\imulations, and it is a project that aims at building bridges between cosmology and astrophysics through numerical simulations and machine learning. CAMELS contains 14,091 cosmological simulations --6,163 N-body and 7,928 state-of-the-art (magneto-)hydrodynamic-- and more than 1 Petabyte of data. CAMELS is the largest set of cosmological hydrodynamic simulations ever run.

+--------------+---------------+---------------+-------------+
| Type         | Code          | Subgrid model | Simulations |
+==============+===============+===============+=============+
| Hydrodynamic | Arepo         |  IllustrisTNG |    3,219    |
|              +---------------+---------------+-------------+
|              | Gizmo         |  SIMBA        |    1,171    |
|              +---------------+---------------+-------------+
|              | MP-Gadget     |  Astrid       |    2,080    |
|              +---------------+---------------+-------------+
|              | OpenGadget    |  Magneticum   |    77       |
|              +---------------+---------------+-------------+
|              | Swift         |  EAGLE        |    1,052    |
|              +---------------+---------------+-------------+
|              | Ramses        |               |    296      |
|              +---------------+---------------+-------------+
|              | Enzo          |               |    6        |
|              +---------------+---------------+-------------+
|              | Gadget4-Osaka | CROCODILE     |    27       |
|              +---------------+---------------+-------------+
|              | Gizmo         | Obsidian      |    27       |
+--------------+---------------+---------------+-------------+
| N-body       | Gadget-III    |      ---      |    6,136    |
+--------------+---------------+---------------+-------------+

.. raw:: html

   <p>Introductory video to the CAMELS project:</p>
	 
   <iframe width="560" height="315" src="https://www.youtube.com/embed/0ntjD7PDWG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   <br><br><br>

.. raw:: html

   <p>The video below shows an example of a CAMELS hydrodynamic simulation run with the Ramses code. Gas density and gas temperature are shown in blue and red, respectively as a function of time. CAMELS contains thousands of simulations like this one.</p>
	 
   <iframe width="560" height="315" src="https://www.youtube.com/embed/WnNfkok9sJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
      <br><br><br>

.. raw:: html

   <p>The video below illustrates the differences between different hydrodynamic simulations. All simulations share the same cosmology, initial conditions, and have fiducial astrophysics values. Differences in the different fields shown are due to the intrinsic differences between the subgrid models employed in the simulatons.</p>

   <iframe width="560" height="315" src="https://www.youtube.com/embed/XVvarp6bJHU?si=7JVECFHm-2sANgWa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
	
      <br><br><br>


   
	 
.. toctree::
   :maxdepth: 2
   :caption: CAMELS

   news
   goals
   publications
   data_access
   citation

.. toctree::
   :maxdepth: 2
   :caption: Simulations

   description
   suites_sets
   codes
   parameters

.. toctree::
   :maxdepth: 2
   :caption: Data products

   organization
   snapshots
   subfind
   SubLink
   rockstar
   ahf
   caesar
   Pk
   Bk
   pdf
   VIDE
   Lya
   Xrays
   Profiles
   CMD
   SAM
   zoomGZ

.. toctree::
   :maxdepth: 2
   :caption: Useful

   tutorials
   images
   camels_library
   pylians3

.. toctree::
   :maxdepth: 2
   :caption: Other

   team
   contact
   logo
