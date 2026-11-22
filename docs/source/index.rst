CAMELS
======

.. note::

   **New data release!** A new set of 1,192 second-generation IllustrisTNG simulations in :math:`(50~h^{-1}{\rm Mpc})^3` boxes, varying 35 parameters, has been publicly released. See the :doc:`News <news>` page for details.

.. warning::

   A bug was recently identified in the generation of the FOF/Subfind catalogs for SIMBA, SIMBA_DM and Illustris_DM 1P and CV sets, as well as a small number of Astrid_DM 1P simulations and EX simulations. The bug affected mostly global DM and gas properties of FOF/Subfind objects, less so their galaxy-scale properties such as their stellar properties. We believe that in particular some studies using these 1P sets might have been non-negligibly affected by this. A separate bug affected the FOF/Subfind catalogs for all sets (1P, CV, LH) of Swift-EAGLE. We welcome hearing from anyone who is concerned their study might have been affected, so that we can help figure things out. All the data in the public FOF/Subfind directories is now fixed, and the old buggy data are available upon request. Apologies for any inconvenience!
   

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

   <!-- Game hidden until the Hugging Face space fvillaescusa/camels-fields is public again; remove these comment markers to restore it.
   <figure>
     <figcaption><b>Do you want to play a game?</b><br>
     See how well you can distinguish between different physical fields created from CAMELS.</figcaption>
     
     <script type="module"
             src="https://gradio.s3-us-west-2.amazonaws.com/5.6.0/gradio.js"></script>
     
     <gradio-app src="https://fvillaescusa-camels-fields.hf.space"></gradio-app>
   </figure>
   <br>
   -->

   <figure>
   <figcaption>
	 CAMELS have AI agents to help you with data, paper, coding...etc.
	 Click on the image to use them!
	 </figcaption>
	 <a href="https://camels-agents.streamlit.app/" target="_blank">
	 <img src="_images/logo3.png" alt="CAMELS Agent Logo" style="width:100%; height:auto;">
   </a>
   </figure>

   
	 
CAMELS Literature Atlas
-----------------------

Dozens of papers have been written using the CAMELS simulations, covering topics from simulation-based and field-level inference to baryonic feedback, generative models, and galaxy properties. To help navigate this body of work, we have built the **CAMELS Literature Atlas**: an interactive map of all papers that use CAMELS. With it you can explore how the papers relate to each other by topic, follow the citation and co-author networks, and identify connections between research lines as well as gaps that are still open.

.. raw:: html

   <div style="margin: 1.5em 0;">
     <iframe src="https://franciscovillaescusa.github.io/literature-atlas/camels/#topics"
             title="CAMELS Literature Atlas"
             loading="lazy"
             style="width: 100%; height: 800px; border: 1px solid #e1e4e5; border-radius: 6px;"
             allowfullscreen></iframe>
     <p style="text-align: center; margin-top: 0.8em;">
       <a href="https://franciscovillaescusa.github.io/literature-atlas/camels/#topics"
          target="_blank" rel="noopener"
          style="display: inline-block; padding: 0.5em 1.2em; background: #2980b9; color: #fff; border-radius: 4px; text-decoration: none; font-weight: bold;">
         Open the atlas in full screen &#8599;
       </a>
     </p>
   </div>

.. toctree::
   :maxdepth: 2
   :caption: CAMELS

   news
   goals
   publications
   atlas
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
