CAMELS
======

**CAMELS** stands for **C**\osmology and **A**\strophysics with **M**\achin\ **E** **L**\earning **S**\imulations, and it is a project that aims at building bridges between cosmology and astrophysics through numerical simulations and machine learning.

.. include:: sims.txt

+--------------+---------------+---------------+------------------------------+
| Type         | Code          | Subgrid model | Simulations / Generation     |
|              |               |               +----------+---------+---------+
|              |               |               | First    | Second  | Third   |
+==============+===============+===============+==========+=========+=========+
| Hydrodynamic | Arepo         | IllustrisTNG  |  3,219   | 1,192   |         |
+              +---------------+---------------+----------+---------+---------+
|              | Gizmo         | SIMBA         |  1,171   |         |         |
+              +---------------+---------------+----------+---------+---------+
|              | MP-Gadget     | Astrid        |  2,080   |         |         |
+              +---------------+---------------+----------+---------+---------+
|              | OpenGadget    | Magneticum    |    77    |         |         |
+              +---------------+---------------+----------+---------+---------+
|              | Swift         | EAGLE         |  1,052   |         |         |
+              +---------------+---------------+----------+---------+---------+
|              | Ramses        |               |   552    | 48      |         |
+              +---------------+---------------+----------+---------+---------+
|              | Enzo          |               |     6    |         |         |
+              +---------------+---------------+----------+---------+---------+
|              | Gadget4-Osaka | CROCODILE     |   260    | 148     |         |
+              +---------------+---------------+----------+---------+---------+
|              | Gizmo         | Obsidian      |    27    |         |         |
+--------------+---------------+---------------+----------+---------+---------+
| N-body       | Gadget-III    | ---           |  6,136   | 1,072   |         |
+--------------+---------------+---------------+----------+---------+---------+



.. raw:: html

   <figure>
	 <iframe width="560" height="315" src="https://www.youtube.com/embed/0ntjD7PDWG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
	 <figcaption><p>Introductory video to the CAMELS project</p></figcaption>
   </figure>
   <br>

   <figure>
	 <iframe width="560" height="315" src="https://www.youtube.com/embed/WnNfkok9sJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
	 <figcaption><p>The video below shows an example of a CAMELS hydrodynamic simulation run with the Ramses code. Gas density and gas temperature are shown in blue and red, respectively as a function of time. CAMELS contains thousands of simulations like this one.</p></figcaption>
   </figure>
   <br>

   <figure>
	 <iframe width="560" height="315" src="https://www.youtube.com/embed/XVvarp6bJHU?si=7JVECFHm-2sANgWa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
	 <figcaption><p>The video below illustrates the differences between different hydrodynamic simulations. All simulations share the same cosmology, initial conditions, and have fiducial astrophysics values. Differences in the different fields shown are due to the intrinsic differences between the subgrid models employed in the simulatons.</p></figcaption>
   </figure>
   <br>

   <figure>
	 <iframe width="560" height="315" src="https://www.youtube.com/embed/NUq2UIg9RDM?si=hnBT16qrjlTqac1d" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
	 <figcaption><p>The video shows a comparison between a first- and second-generation CAMELS simulation. Both simulations have the same mass and spatial resolution, but the second-generation one, has a volume 8x larger than its first-generation one.</p></figcaption>
   </figure>
   <br>

   <figure>
     <figcaption><b>Do you want to play a game?</b><br>
     See how well you can distinguish between different physical fields created from CAMELS.</figcaption>
     
     <script type="module"
             src="https://gradio.s3-us-west-2.amazonaws.com/5.6.0/gradio.js"></script>
     
     <gradio-app src="https://fvillaescusa-camels-fields.hf.space"></gradio-app>
   </figure>
   <br>

   <figure>
   <figcaption>
	 CAMELS have AI agents to help you with data, paper, coding...etc.
	 Click on the image to use them!
	 </figcaption>
	 <a href="https://camels-agents.streamlit.app/" target="_blank">
	 <img src="_images/logo3.png" alt="CAMELS Agent Logo" style="width:100%; height:auto;">
   </a>
   </figure>

   
	 
.. toctree::
   :maxdepth: 2
   :caption: CAMELS

   news
   goals
   publications
   data_access
   agents
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
   photometry
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
