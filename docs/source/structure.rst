**************
Data structure
**************

CAMELS data is structured as follows. CAMELS contains 2 simulations suites: IllustrisTNG and SIMBA. Each suite contains 4 different sets: LH, 1P, CV, and EX. Each set contains a different number of (magneto-)hydrodynamic simulations. Furthermore, for each (magneto-)hydrodynamic simulation CAMELS contains its N-body counterpart.

The scheme below shows the general structure of CAMELS data:

.. image:: Sims_scheme.pdf

Each simulation follows the evolution of :math:`256^3` dark matter particles and :math:`256^3` gas resolution elements (only for the (magneto-)hydrodynamic) within a periodic volume of :math:`(25~h^{-1}{\rm Mpc})^3` from :math:`z=127` down to :math:`z=0`. All simulations share the value of these cosmological parameters:

+-----------------------+-----------+----------------+-----------+---------------+-----------------+
|:math:`\Omega_{\rm b}` |:math:`h`  |:math:`n_s`     |:math:`w`  |:math:`M_\nu`  |:math:`\Omega_k` | 
+=======================+===========+================+===========+===============+=================+
|0.049                  |0.6711     |0.9624          |-1         |0.0 eV         |0.0              |
+-----------------------+-----------+----------------+-----------+---------------+-----------------+
	   
CAMELS has been designed to explore the parameter space of cosmological (by varying :math:`\Omega_{\rm m}` and :math:`\sigma_8`) and astrophysical models (by varying :math:`A_{\rm SN1}`, :math:`A_{\rm SN2}`, :math:`A_{\rm AGN1}`, and :math:`A_{\rm AGN2}`). The physical meaning of these parameters is given in this table:

+-----------------------+----------------------------------+----------------------------+
|Parameter              |IllustrisTNG suite                | SIMBA suite                |
+=======================+==================================+============================+
|:math:`\Omega_{\rm m}` |Fraction of energy density in matter (dark matter + baryons)   |
+-----------------------+----------------------------------+----------------------------+
|:math:`\sigma_8`       |Variance of the linear field on :math:`8~h^{-1}{\rm Mpc}`      |
|                       |at :math:`z=0`                                                 |
+-----------------------+----------------------------------+----------------------------+
|:math:`A_{\rm SN1}`    |Galactic winds:                   |Galactics winds:            |
|                       |Energy per unit SFR               |mass loading                |
+-----------------------+----------------------------------+----------------------------+
|:math:`A_{\rm SN2}`    |Galactic winds: wind speed                                     |
+-----------------------+----------------------------------+----------------------------+
|:math:`A_{\rm AGN1}`   |Kinetic mode BH feedback:         |QSO & jet-mode BH feedback: | 
|                       |energy per unit BH accretion rate |momentum flux               | 
+-----------------------+----------------------------------+----------------------------+
|:math:`A_{\rm AGN2}`   |Kinetic mode BH feedback          |Jet-mode BH feedback:       |
|                       |ejection speed/burstiness         |jet speed                   | 
+-----------------------+----------------------------------+----------------------------+


Suites
~~~~~~

CAMELS contains two different suites. The name of each suite reflects the code and subgrid model used to run all the simulations in the suite. 

- | **IllustrisTNG suite**. All the simulations in this suite have been run using the AREPO code and employing the IllustrisTNG subgrid model. See :ref:`IllustrisTNG_params` for the value of the cosmological, astrophysical, and initial random seed for all simulations in this suite. 
- | **SIMBA suite**. All the simulations in this suite have been run using the GIZMO code and employing the SIMBA subgrid model. See :ref:`SIMBA_params` for the value of the cosmological, astrophysical, and initial random seed for all simulations in this suite. 

Each suite contains 4 sets and a total of 1,092 simulations.
  

Sets
~~~~

Each suite contains four different sets, that differ on how the value of the cosmological and astrophysical parameters in each of their simulations are organized, together with the treatment of the initial random seed.

- | **LH**. This set contains 1,000 simulations. Each simulation has a different value of the cosmological and astrophysical parameters, that are arranged in a latin-hypercube. Each simulation has a different value of the initial random seed. This set represents the main CAMELS dataset. LH stands for Latin-Hypercube.
- | **1P**. This set contains 61 simulations. In this set, the value of the cosmological and astrophysical parameters in the simulations is varied only one at a time. The value of the random seed is the same in all simulations. This set is typically used to study the change induced by cosmology and astrophysics in a given quantity. 1P stands for 1-parameter at a time.
- | **CV**. This set contains 27 simulations. All the simulations share the value of the cosmological and astrophysical parameters, and they only differ in the value of their initial random seed. This set is typically used to study the effect of cosmic variance. CV stands for Cosmic Variance.
- | **EX**. This set contains 4 simulations. All simulations share the value of the cosmological parameters, but differ in the value of the astrophysical parameters. One simulation has fiducial values; the other three represent extreme cases with 1) very efficient supernova feedback, 2) very efficient AGN feedback, and 3) no feedback. All simulations share the value of the initial random seed. This set can be used to study the maximum effect astrophysics can have on a given quantity. EX stands for Extreme.


Simulations
~~~~~~~~~~~

Each CAMELS simulation contains 34 snapshots, corresponding to different redshifts. The relation between the snapshot number and the redshift is this:

+---------------+--------+------------+
|Snapshot number|Redshift|Scale Factor|
+===============+========+============+
|000            |6.00000 |0.14286     |
+---------------+--------+------------+
|001            |5.00000 |0.16667     |
+---------------+--------+------------+
|002            |4.00000 |0.20000     |
+---------------+--------+------------+
|003            |3.50000 |0.22222     |
+---------------+--------+------------+
|004            |3.00000 |0.25000     |
+---------------+--------+------------+
|005            |2.81329 |0.26224     |
+---------------+--------+------------+
|006            |2.63529 |0.27508     |
+---------------+--------+------------+
|007            |2.46560 |0.28855     |
+---------------+--------+------------+
|008            |2.30383 |0.30268     |
+---------------+--------+------------+
|009            |2.14961 |0.31750     |
+---------------+--------+------------+
|010            |2.00259 |0.33305     |
+---------------+--------+------------+
|011            |1.86243 |0.34935     |
+---------------+--------+------------+
|012            |1.72882 |0.36646     |
+---------------+--------+------------+
|013            |1.60144 |0.38440     |
+---------------+--------+------------+
|014            |1.48001 |0.40322     |
+---------------+--------+------------+
|015            |1.36424 |0.42297     |
+---------------+--------+------------+
|016            |1.25388 |0.44368     |
+---------------+--------+------------+
|017            |1.14868 |0.46540     |
+---------------+--------+------------+
|018            |1.04838 |0.48819     |
+---------------+--------+------------+
|019            |0.95276 |0.51209     |
+---------------+--------+------------+
|020            |0.86161 |0.53717     |
+---------------+--------+------------+
|021            |0.77471 |0.56347     |
+---------------+--------+------------+
|022            |0.69187 |0.59106     |
+---------------+--------+------------+
|023            |0.61290 |0.62000     |
+---------------+--------+------------+
|024            |0.53761 |0.65036     |
+---------------+--------+------------+
|025            |0.46584 |0.68220     |
+---------------+--------+------------+
|026            |0.39741 |0.71561     |
+---------------+--------+------------+
|027            |0.33218 |0.75065     |
+---------------+--------+------------+
|028            |0.27000 |0.78740     |
+---------------+--------+------------+
|029            |0.21072 |0.82596     |
+---------------+--------+------------+
|030            |0.15420 |0.86640     |
+---------------+--------+------------+
|031            |0.10033 |0.90882     |
+---------------+--------+------------+
|032            |0.04896 |0.95332     |
+---------------+--------+------------+
|033            |0.00000 |1.00000     |
+---------------+--------+------------+

.. Note::

   While the above table gives the exact redshifts and scale factors for the simulations in the SIMBA suite and all N-body simulations, for the simulations in the IllustrisTNG suite these numbers can be slightly different. This is because AREPO can only write snapshots in the highest time steps in the hierarchy.

CAMELS stores the halo/galaxy catalogue extracted from each snapshot obtained by running the SUBFIND code.

N-body simulations
~~~~~~~~~~~~~~~~~~

For each (magneto-)hydrodynamic simulation, CAMELS also contains its N-body counterpart. The N-body simulations have been run with the Gadget-III code. For each snapshot, CAMELS contains the associated halo/subhalo catalogue generated with the SUBFIND code.

.. Note::

   Although the number of (magneto-)hydrodynamic simulations is 2,184, the number of N-body simulations is slightly smaller: 2,049. This is because many simulations in the 1P set, and all in the EX set, only exhibit differences in the value of the astrophysical parameters. Thus, a single simulation is enough for their N-body counterpart.
