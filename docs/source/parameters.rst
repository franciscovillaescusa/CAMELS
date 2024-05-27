.. _params:   

**********
Parameters
**********

As discussed in :ref:`suites_sets`, the CAMELS simulations can be classified into different sets, depending on how their parameters (cosmological, astrophysical, and initial random seed) are organized. Here we provide details about this.

+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   Suite          | Set                                                                                                                                                                                                                                                                   |
+------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+
|                  | CV                                        | 1P                                        | EX                                        | LH                                        | BE                                        | SB                                        |
+==================+===========================================+===========================================+===========================================+===========================================+===========================================+===========================================+
| **IllustrisTNG** | `params <https://tinyurl.com/29352aub>`__ | `params <https://tinyurl.com/mr53zfe7>`__ | `params <https://tinyurl.com/4mdac2hk>`__ | `params <https://tinyurl.com/2u844n46>`__ | `params <https://tinyurl.com/2v3eanmh>`__ | `params <https://tinyurl.com/mwwkkxj2>`__ |
|                  |                                           |                                           |                                           |                                           |                                           |                                           |
|                  | `info <https://tinyurl.com/mvtsf833>`__   | `info <https://tinyurl.com/bdfpc5zr>`__   | `info <https://tinyurl.com/mvtsf833>`__   | `info <https://tinyurl.com/mvtsf833>`__   | `info <https://tinyurl.com/mvtsf833>`__   | `info <https://tinyurl.com/bdfpc5zr>`__   |
+------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+
| **SIMBA**        | `params <https://tinyurl.com/2x8ksft3>`__ | `params <https://tinyurl.com/44ycz423>`__ | `params <https://tinyurl.com/wuz32k54>`__ | `params <https://tinyurl.com/mrbtut8w>`__ | `params <https://tinyurl.com/5ccpjxr7>`__ |                                           |
|                  |                                           |                                           |                                           |                                           |                                           |                                           |
|                  | `info <https://tinyurl.com/299tr2ky>`__   | `info <https://tinyurl.com/bdczbarm>`__   | `info <https://tinyurl.com/299tr2ky>`__   | `info <https://tinyurl.com/299tr2ky>`__   | `info <https://tinyurl.com/299tr2ky>`__   |                                           |
+------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+
| **Astrid**       | `params <https://tinyurl.com/4r4nx4dh>`__ | `params <https://tinyurl.com/25d45vv6>`__ | `params <https://tinyurl.com/4xxv3778>`__ | `params <https://tinyurl.com/56zajcxz>`__ | `params <https://tinyurl.com/yn7734yz>`__ | `params <https://tinyurl.com/mua4z5ve>`__ |
|                  |                                           |                                           |                                           |                                           |                                           |                                           |
|                  | `info <https://tinyurl.com/mrxjy3vj>`__   | `info <https://tinyurl.com/yc5cj87v>`__   | `info <https://tinyurl.com/mrxjy3vj>`__   | `info <https://tinyurl.com/mrxjy3vj>`__   | `info <https://tinyurl.com/mrxjy3vj>`__   | `info <https://tinyurl.com/yc5cj87v>`__   |
+------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+
| **Magneticum**   | `params <https://tinyurl.com/yeypjbmk>`__ |                                           |                                           | `params <https://tinyurl.com/2ucc4v4d>`__ |                                           |                                           |
|                  |                                           |                                           |                                           |                                           |                                           |                                           |
|                  | `info <https://tinyurl.com/ybsvt3yy>`__   |                                           |                                           | `info <https://tinyurl.com/ybsvt3yy>`__   |                                           |                                           |
+------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+
| **Swift-EAGLE**  | `params <https://tinyurl.com/mr2t5psr>`__ | `params <https://tinyurl.com/3ys5bdxx>`__ |                                           | `params <https://tinyurl.com/3sy8bn8r>`__ |                                           |                                           |
|                  |                                           |                                           |                                           |                                           |                                           |                                           |
|                  | `info <https://tinyurl.com/33estf6d>`__   | `info <https://tinyurl.com/33estf6d>`__   |                                           | `info <https://tinyurl.com/33estf6d>`__   |                                           |                                           |
+------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+
| **Ramses**       | `params <https://tinyurl.com/muecmrsm>`__ | `params <https://tinyurl.com/7c2et66r>`__ |                                           |                                           |                                           | `params <https://tinyurl.com/2kcd7yhc>`__ |
|                  |                                           |                                           |                                           |                                           |                                           |                                           |
|                  | `info <https://tinyurl.com/t3ma6ch8>`__   | `info <https://tinyurl.com/t3ma6ch8>`__   |                                           |                                           |                                           | `info <https://tinyurl.com/t3ma6ch8>`__   |
+------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+
| **Enzo**         |                                           |                                           |                                           |                                           |                                           |                                           |
+------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+-------------------------------------------+



Cosmological parameters
-----------------------

All simulations share the value of these cosmological parameters:

+-----------+---------------+-----------------+
|:math:`w`  |:math:`M_\nu`  |:math:`\Omega_k` | 
+===========+===============+=================+
|-1         |0.0 eV         |0.0              |
+-----------+---------------+-----------------+

For the other cosmological parameters, the different sets vary them differently:

+----+-----------------------+------------------+-----------------------+----------------+----------------+
|    |:math:`\Omega_{\rm m}` |:math:`\sigma_8`  |:math:`\Omega_{\rm b}` |:math:`h`       |:math:`n_s`     |
+====+=======================+==================+=======================+================+================+
| CV | 0.3                   | 0.8              |0.049                  |0.6711          |0.9624          |
+----+-----------------------+------------------+-----------------------+----------------+----------------+
| BE | 0.3                   | 0.8              |0.049                  |0.6711          |0.9624          |
+----+-----------------------+------------------+-----------------------+----------------+----------------+
| EX | 0.3                   | 0.8              |0.049                  |0.6711          |0.9624          |
+----+-----------------------+------------------+-----------------------+----------------+----------------+
| LH | 0.1 - 0.5             | 0.6 - 1.0        |0.049                  |0.6711          |0.9624          |
+----+-----------------------+------------------+-----------------------+----------------+----------------+
| 1P | 0.1 - 0.5             | 0.6 - 1.0        |0.029 - 0.069          |0.4711 - 0.8711 |0.7624 - 1.1624 |
+----+-----------------------+------------------+-----------------------+----------------+----------------+
| SB | 0.1 - 0.5             | 0.6 - 1.0        |0.029 - 0.069          |0.4711 - 0.8711 |0.7624 - 1.1624 |
+----+-----------------------+------------------+-----------------------+----------------+----------------+

.. attention::

   In the case of the Astrid SB7 set, :math:`\Omega_{\rm b}` is varied from 0.01 to 0.09.


Astrophysical parameters
------------------------

We emphasize that every subgrid physics model is different, and the parameters of one model does not mean anything in another one. Thus, we will describe these parameters for each suite and what is varied.

IllustrisTNG
~~~~~~~~~~~~

The IllustrisTNG suite contains all sets: 1P, CV, LH, EX, BE, and SB. This table shows which parameters are varied in each set:

+-------+-------------------------------------------+
|       | Astrophysical parameters                  |
+=======+===========================================+
| CV    | *fiducial* IllustrisTNG                   |
+-------+-------------------------------------------+
| BE    | *fiducial* IllustrisTNG                   |
+-------+-------------------------------------------+
| LH    | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+
| EX    | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+
| 1P    | *extended* 23 astrophysical parameters    |
+-------+-------------------------------------------+
| SB28  | *extended* 23 astrophysical parameters    |
+-------+-------------------------------------------+

The meaning and range of variation of the 4 *standard* IllustrisTNG parameters are these:

- :math:`A_{\rm SN1}`: it represents the energy per unit SFR of the galactic winds. It can vary from 0.25 to 4. Fiducial value is 1.
- :math:`A_{\rm SN2}`: it represents the wind speed of the galactic winds. It can vary from 0.5 to 2. Fiducial value is 1.
- :math:`A_{\rm AGN1}`: it represents the energy per unit blach-hole accretion rate. It can vary from 0.25 to 4. Fiducial value is 1.
- :math:`A_{\rm AGN2}`: it represents the ejection speed/burstiness of the kinetic mode of the black-hole feedback. It can vary from 0.5 to 2. Fiducial value is 1.

.. Note::
   
   A value of 1 in the astrophysical parameters :math:`A_{\rm SN1}`, :math:`A_{\rm SN2}`, :math:`A_{\rm AGN1}`, :math:`A_{\rm AGN2}`, represents the value chosen in the original flagship simulation of each suite. For instance, the original IllustrisTNG simulation has :math:`A_{\rm SN1}=1`, :math:`A_{\rm SN2}=1`, :math:`A_{\rm AGN1}=1`, :math:`A_{\rm AGN2}=1`.

The *extended* 23 IllustrisTNG parameters represent an almost-complete set of the IllustrisTNG model, i.e. it contains almost all parameters in the subgrid physics model. The range of the parameters was chosen to cover a very wide range of effects. For SB28, the user can find the list of parameters, their range, and meaning `here <https://github.com/franciscovillaescusa/CAMELS/blob/master/docs/params/IllustrisTNG_SB28_param_minmax.csv>`_.
  
  

SIMBA
~~~~~

The SIMBA suite contains 4 different sets: 1P, CV, LH, and EX. This table shows which parameters are varied in each set:

+-------+-------------------------------------------+
|       | Astrophysical parameters                  |
+=======+===========================================+
| CV    | *fiducial* SIMBA                          |
+-------+-------------------------------------------+
| BE    | *fiducial* SIMBA                          |
+-------+-------------------------------------------+
| LH    | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+
| EX    | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+
| 1P    | *extended* 23 astrophysical parameters    |
+-------+-------------------------------------------+

The meaning and range of variation of the 4 *standard* SIMBA parameters are these:

- :math:`A_{\rm SN1}`: it represents the mass loading of the galactic winds. It can vary from 0.25 to 4. Fiducial value is 1.
- :math:`A_{\rm SN2}`: it represents the wind speed of the galactic winds. It can vary from 0.5 to 2. Fiducial value is 1.
- :math:`A_{\rm AGN1}`: it represents the momentum flux of the QSO & jet-mode black-hole feedback. It can vary from 0.25 to 4. Fiducial value is 1.
- :math:`A_{\rm AGN2}`: it represents the jet speed of the jet-mode black-hole feedback. It can vary from 0.5 to 2. Fiducial value is 1.

.. Note::
   
   A value of 1 in the astrophysical parameters :math:`A_{\rm SN1}`, :math:`A_{\rm SN2}`, :math:`A_{\rm AGN1}`, :math:`A_{\rm AGN2}`, represents the value chosen in the original flagship simulation of each suite. For instance, the original SIMBA simulation has :math:`A_{\rm SN1}=1`, :math:`A_{\rm SN2}=1`, :math:`A_{\rm AGN1}=1`, :math:`A_{\rm AGN2}=1`.
  

.. Important::

   While we call these parameters in the same way as the ones of IllustrisTNG, we emphasize that they are completely independent of each other. For instance, a neural network trained to predict :math:`A_{\rm SN1}` from IllustrisTNG simulation should fail if tested on SIMBA.


Astrid
~~~~~~

The Astrid suite contains 5 different sets: 1P, CV, LH, EX, and SB. This table shows which parameters are varied in each set:

+-------+-------------------------------------------+
|       | Astrophysical parameters                  |
+=======+===========================================+
| CV    | *fiducial* Astrid                         |
+-------+-------------------------------------------+
| LH    | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+
| EX    | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+
| 1P    | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+
| SB7   | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+

The meaning and range of variation of the 4 *standard* Astrid parameters are these:

- :math:`A_{\rm SN1}`: it represents the energy per SFR of the galactic winds. It can vary from 0.25 to 4. Fiducial value is 1.
- :math:`A_{\rm SN2}`: it represents the wind speed of the galactic winds. It can vary from 0.5 to 2. Fiducial value is 1.
- :math:`A_{\rm AGN1}`: it represents the energy per black-hole accretion rate of the kinetic black-hole feedback. It can vary from 0.25 to 4. Fiducial value is 1.
- :math:`A_{\rm AGN2}`: it represents the energy per unit black-hole accretion rate of the thermal model of the black-hole feedback. It can vary from 0.25 to 4. Fiducial value is 1.

.. Note::
   
   A value of 1 in the astrophysical parameters :math:`A_{\rm SN1}`, :math:`A_{\rm SN2}`, :math:`A_{\rm AGN1}`, :math:`A_{\rm AGN2}`, represents the value chosen in the original flagship simulation of each suite. For instance, the original Astrid simulation has :math:`A_{\rm SN1}=1`, :math:`A_{\rm SN2}=1`, :math:`A_{\rm AGN1}=1`, :math:`A_{\rm AGN2}=1`.

.. Note::

   The SB7 suite of Astrid varies :math:`\Omega_{\rm m}`, :math:`\sigma_8`, the above four standard astrophysical parameters and :math:`\Omega_{\rm b}`, that varies from 0.01 to 0.09.

.. Important::

   While we call these parameters in the same way as the ones of IllustrisTNG and SIMBA, we emphasize that they are completely independent of each other. For instance, a neural network trained to predict :math:`A_{\rm SN1}` from IllustrisTNG simulation should fail if tested on Astrid.



Magneticum
~~~~~~~~~~

This table shows which parameters are varied in each set:

+-------+-------------------------------------------+
|       | Astrophysical parameters                  |
+=======+===========================================+
| CV    | *fiducial* Magneticum                     |
+-------+-------------------------------------------+
| LH    | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+


The meaning and range of variation of the 4 *standard* Magneticum parameters are these:

- :math:`A_{\rm SN1}` represents the energy per unit of SFR of the galactic winds. It can vary from 0.25 to 4.
- :math:`A_{\rm SN2}` represents the wind speed of the galactic winds. It can vary from 0.5 to 2.
- :math:`A_{\rm AGN1}` represents the rate of energy injection from AGN into the ISM,. It can vary from 0.25 to 4.
- :math:`A_{\rm AGN2}` represents the threshold for switching to radio mode. It can vary from 0.5 to 2.

.. Attention::

   What we call here *fiducial* Magneticum does not correspond exactly with the original Magneticum simulation, but with its updated model. See :ref:`Codes` for more details.


Swift-EAGLE
~~~~~~~~~~~

The Swift-EAGLE suite contains 3 different sets: CV, 1P, and LH. This table shows which parameters are varied in each set:

+-------+-------------------------------------------+
|       | Astrophysical parameters                  |
+=======+===========================================+
| CV    | *fiducial* Ramses                         |
+-------+-------------------------------------------+
| 1P    | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+
| LH    | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+

The meaning and range of variation of the 4 *standard* EAGLE parameters are these:

- :math:`A_{\rm SN1}` represents the thermal energy injected in each SNII event. It can vary from 0.25 to 4.
- :math:`A_{\rm SN2}` represents the metallicity dependence of the stellar feedback fraction per unit stellar mass. It can vary from 0.5 to 2.
- :math:`A_{\rm AGN1}` represents the scaling of the black hole Bondi accretion rate. It can vary from 0.25 to 4.
- :math:`A_{\rm AGN2}` represents the temperature jump of gas particles in AGN feedback events. It can vary from 0.5 to 2.


Ramses
~~~~~~

The Ramses suite contains 3 different sets: CV, 1P, and SB. This table shows which parameters are varied in each set:

+-------+-------------------------------------------+
|       | Astrophysical parameters                  |
+=======+===========================================+
| CV    | *fiducial* Ramses                         |
+-------+-------------------------------------------+
| 1P    | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+
| SB5   | *standard* 4 astrophysical parameters     |
+-------+-------------------------------------------+

The meaning and range of variation of the 4 *standard* Ramses parameters are these:

- :math:`A_{\rm SN1}`: this parameter controls the amplitude of the supernovae mechanical energy. It can vary from 0.1 to 10. Fiducial value is 1.
- :math:`A_{\rm SN2}`: this parameter controls the amplitude of the star-formation efficiency of the Ramses multi-free-fall subgrid model. It can vary from 0.05 to 5. Fiducial value is 0.5.
- :math:`A_{\rm AGN1}`: this parameter represents the size of the accretion and feedback region around the sink particles (representing SMBH in Ramses). Sizes are in units of the cell size (usually held quasi-constant in physical scale). It can vary from 2 to 8. Fiducial value is 4.
- :math:`A_{\rm AGN2}`: this parameter represents the gravitational softening of the sink particles (representing SMBH in Ramses). Sizes are in units of the cell size (usually held quasi-constant in physical scale). It can vary from 1 to 4. Fiducial value is 2.

.. Important::

   The value of :math:`A_{\rm AGN2}` in Ramses is set to :math:`A_{\rm AGN1}/2` in all Ramses simulations. Thus, in SB5 there are only two free cosmological parameters (:math:`\Omega_{\rm m}` and :math:`\sigma_8`) and three free astrophysical parameters (:math:`A_{\rm SN1}`, :math:`A_{\rm SN2}`, and :math:`A_{\rm AGN1}`).

.. Note::

   There will not be a LH set of Ramses and only Sobol sequences. 

Enzo
~~~~

..
    CAMELS has been designed to sample the parameter space of cosmological (by varying :math:`\Omega_{\rm m}` and :math:`\sigma_8`) and astrophysical models (by varying :math:`A_{\rm SN1}`, :math:`A_{\rm SN2}`, :math:`A_{\rm AGN1}`, and :math:`A_{\rm AGN2}`). The physical meaning of these parameters is given in this table:

    +--------------------+------------------------+----------------------------+---------------------+---------------------+-----------------------------------+-----------------------------------+
    | Suite              | :math:`\Omega_{\rm m}` | :math:`\sigma_8`           | :math:`A_{\rm SN1}` | :math:`A_{\rm SN2}` | :math:`A_{\rm AGN1}`              | :math:`A_{\rm AGN2}`              |
    +====================+========================+============================+=====================+=====================+===================================+===================================+
    | IllustrisTNG       | Fraction of energy     | Variance of the            | Galactic winds:     | Galactic winds:     | Kinetic mode BH feedback:         | Kinetic mode BH feedback:         |
    |                    |                        |                            |                     |                     |                                   |                                   |
    |                    |                        |                            | Energy per unit SFR | wind speed          | energy per unit BH accretion rate | ejection speed/burstiness         |
    +--------------------+                        +                            +---------------------+                     +-----------------------------------+-----------------------------------+
    | SIMBA              | density in matter      | linear field on            | Galactic winds:     |                     | QSO & jet-mode BH feedback:       | Jet-mode BH feedback:             |
    |                    |                        |                            |                     |                     |                                   |                                   |
    |                    |                        |                            | Mass loading        |                     | momentum flux                     | jet speed                         |
    +--------------------+                        + :math:`8~h^{-1}{\rm Mpc}`  +---------------------+                     +-----------------------------------+-----------------------------------+
    | Astrid             | (dark matter+baryons)  |                            | Galactic winds:     |                     | Kinetic mode BH feedback:         | thermal mode BH feedback:         |
    |                    |                        |                            |                     |                     |                                   |                                   |
    |                    |                        | at :math:`z=0`             | Energy per unit SFR |                     | energy per unit BH accretion rate | energy per unit BH accretion rate |
    +--------------------+------------------------+----------------------------+---------------------+---------------------+-----------------------------------+-----------------------------------+

    Each CAMEL simulation has a different value of :math:`\Omega_{\rm m}`, :math:`\sigma_8`, :math:`A_{\rm SN1}`, :math:`A_{\rm SN2}`, :math:`A_{\rm AGN1}`, :math:`A_{\rm AGN2}` and/or the initial random seed. The range of variation for the different parameters is:

    .. math::
       
       0.1 \le & \Omega_{\rm m} & \le 0.5\\
       0.6 \le & \sigma_8 & \le 1.0\\
       0.25 \le & A_{\rm SN1} & \le 4.0\\
       0.50 \le & A_{\rm SN2} & \le 2.0\\
       0.25 \le & A_{\rm AGN1} & \le 4.0\\
       0.50 \le & A_{\rm AGN2} & \le 2.0\\
   

.. Note::

   We remind the user that for each hydrodynamic simulation there is an N-body counterpart with the same value of the cosmological parameters and of the initial random seed. Thus, the value of the cosmological parameters and of the initial random seed for the N-body simulations can be found in the above links. For instance, for the N-body simulation ``Astrid_DM/LH/LH_345`` the value of :math:`\Omega_{\rm m}`, :math:`\sigma_8`, and the initial random seed is 0.4714, 0.689, and 10350, respectively (the same as the simulation ``Astrid/LH/LH_345``).

   

