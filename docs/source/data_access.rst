************
Instructions
************

CAMELS data is stored at the Rusty cluster of the Flatiron Institute in New York City and its data can be access through five different ways. A subset of the data is also stored at the Tiger cluster at Princeton University.


Binder
~~~~~~

Binder is a system that allows users to read and manipulate data that is hosted at the Flatiron Institute through either a Jupyter notebook or a unix shell. Some basic documentation can be found `here <https://docs.simonsfoundation.org/index.php/Public:Binder>`_. All CAMELS data can be accessed, read, and manipulated through Binder. 

.. warning::

   Please note that the Binder environment is ephemeral - after a few days of inactivity its contents are deleted, so one has to be vigilant about downloading any analysis results in time.

.. warning::
​
   Binder is not designed to carry out long and heavy calculations. In this case we recommend the user to download the data and work with it locally.

`Link to Binder <https://binder.flatironinstitute.org/~sgenel/CAMELS_PUBLIC>`_


Globus
~~~~~~~

The full CAMELS data can be downloaded via globus, an online system designed to efficiently transfer large amounts of data. This is the method we recommend to transfer the data.

url
~~~

We provide access to the full CAMELS data via a simple uniform resource locator (url). We do not recommend downloading large amounts of data through this system, as can be slow and unstable. However, for small or individual files it may be convenient.


FlatHUB
~~~~~~~

FlatHUB is a platform that allows users to explore and compare data from different simulations by browsing and filtering the data, making simple preview plots, and downloading sub-samples of the data. We provide access to the SUBFIND halo and subhalo catalogues of the IllustrisTNG and SIMBA suites through this platform.

`Link to FlatHUB <http://flathub.flatironinstitute.org/group/cosmo-hydro/camels/>`_


Rusty
~~~~~

Users with an account on the Flatiron Institute Rusty cluster, can find all CAMELS data in ``/mnt/ceph/users/camels/PUBLIC_RELEASE``.


Tiger
~~~~~

A partial copy of the data is located at the Tiger cluster of Princeton University. Users with an account in Tiger can find the data in: ``/projects/QUIJOTE/CAMELS``.



​
