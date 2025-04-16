.. _SubLink:

****************
SubLink catalogs
****************

The folders ``SubLink`` and ``SubLink_gal`` contain merger trees constructed using the SUBFIND-based SubLink algorithm. The data is organized following the general hierarchical structure described in :ref:`suite_folders`. Both SubLink and SubLink_gal follow the standard SubLink format, and we refer users to the official `SubLink documentation <https://www.tng-project.org/data/docs/specifications/#sec4a>`_ for further technical details.


We provide two versions -- SubLink and SubLink_gal -- generated with the SubLink algorithm. The SubLink trees use only dark matter (DM) particles to determine the connections between subhalos across snapshots, which corresponds exactly to the method used in the public data release of the IllustrisTNG project. In contrast, SubLink_gal uses baryonic particles to define links between subhalos, providing a galaxy-centric view of merger histories.


The differences between SubLink and SubLink_gal are generally modest because, in most cases, progenitor and descendant subhalos share the majority of their DM particles, as well as most of their stellar and gas particles. In other words, significant baryon–DM detachment during mergers is rare. Further, the physical properties of the subhalos (e.g., stellar mass, gas content) are the same in both versions, as they are adopted from the SUBFIND catalogs.





