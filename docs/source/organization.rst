*****************
Data organization
*****************

CAMELS data is organized as follows.

CAMELS folder
~~~~~~~~~~~~~

The main CAMELS simulation folder contains different folders:

.. code-block:: bash

   >> ls
   IllustrisTNG     SIMBA     times.txt
   IllustrisTNG_DM  SIMBA_DM

- ``IllustrisTNG`` is the folder containing the IllustrisTNG suite.
- ``IllustrisTNG_DM`` is the folder containing the N-body simulations of the IllustrisTNG suite.
- ``SIMBA`` is the folder containing the SIMBA suite.
- ``SIMBA_DM`` is the folder containing the N-body simulations of the SIMBA suite.
- ``times.txt``. This file contains the scale factors of the simulations (with the exception of the last snapshot at :math:`z=0`). This file is used by both the GIZMO and AREPO codes to write snapshots at these times.

Suite folder
~~~~~~~~~~~~
  
Inside each folder suite there are the simulations from the different sets:

.. code-block:: bash

   >> ls IllustrisTNG
   EX_1    LH_146  LH_197  LH_247  LH_298  LH_348  LH_399  LH_449  LH_5    LH_55   LH_60   LH_650  LH_700  LH_751  LH_801  LH_852  LH_902  LH_953
   EX_2    LH_147  LH_198  LH_248  LH_299  LH_349  LH_4    LH_45   LH_50   LH_550  LH_600  LH_651  LH_701  LH_752  LH_802  LH_853  LH_903  LH_954
   EX_3    LH_148  LH_199  LH_249  LH_3    LH_35   LH_40   LH_450  LH_500  LH_551  LH_601  LH_652  LH_702  LH_753  LH_803  LH_854  LH_904  LH_955
   LH_0    LH_149  LH_2    LH_25   LH_30   LH_350  LH_400  LH_451  LH_501  LH_552  LH_602  LH_653  LH_703  LH_754  LH_804  LH_855  LH_905  LH_956
   LH_1    LH_15   LH_20   LH_250  LH_300  LH_351  LH_401  LH_452  LH_502  LH_553  LH_603  LH_654  LH_704  LH_755  LH_805  LH_856  LH_906  LH_957
   LH_10   LH_150  LH_200  LH_251  LH_301  LH_352  LH_402  LH_453  LH_503  LH_554  LH_604  LH_655  LH_705  LH_756  LH_806  LH_857  LH_907  LH_958
   LH_100  LH_151  LH_201  LH_252  LH_302  LH_353  LH_403  LH_454  LH_504  LH_555  LH_605  LH_656  LH_706  LH_757  LH_807  LH_858  LH_908  LH_959
   LH_101  LH_152  LH_202  LH_253  LH_303  LH_354  LH_404  LH_455  LH_505  LH_556  LH_606  LH_657  LH_707  LH_758  LH_808  LH_859  LH_909  LH_96
   LH_102  LH_153  LH_203  LH_254  LH_304  LH_355  LH_405  LH_456  LH_506  LH_557  LH_607  LH_658  LH_708  LH_759  LH_809  LH_86   LH_91   LH_960
   LH_103  LH_154  LH_204  LH_255  LH_305  LH_356  LH_406  LH_457  LH_507  LH_558  LH_608  LH_659  LH_709  LH_76   LH_81   LH_860  LH_910  LH_961
   LH_104  LH_155  LH_205  LH_256  LH_306  LH_357  LH_407  LH_458  LH_508  LH_559  LH_609  LH_66   LH_71   LH_760  LH_810  LH_861  LH_911  LH_962
   LH_105  LH_156  LH_206  LH_257  LH_307  LH_358  LH_408  LH_459  LH_509  LH_56   LH_61   LH_660  LH_710  LH_761  LH_811  LH_862  LH_912  LH_963
   LH_106  LH_157  LH_207  LH_258  LH_308  LH_359  LH_409  LH_46   LH_51   LH_560  LH_610  LH_661  LH_711  LH_762  LH_812  LH_863  LH_913  LH_964
   ...

- ``1P_X``. These folders contain the simulations of the 1P set. X goes from 0 to 65.
- ``CV_X``. These folders contain the simulations of the CV set. X goes from 0 to 26.
- ``EX_X``. These folders contain the simulations of the EX set. X goes from 0 to 3.
- ``LH_X``. These folders contain the simulations of the LH set. X goes from 0 to 999.
- ``CosmoAstroSeed_params.txt``. This file contains the value of the cosmological and astrophysical parameter, together with the value of the random seed, for each simulation in the suite. The format of the file is: simulation_name :math:`\Omega_{\rm m}`  :math:`\sigma_8`  :math:`A_{\rm SN1}`  :math:`A_{\rm SN2}`  :math:`A_{\rm AGN1}`  :math:`A_{\rm AGN2}` seed.

.. Note::

   The structure and organization of the different folders inside the ``IllustrisTNG_DM`` and ``SIMBA_DM`` is the same as in the ``IllustrisTNG`` and ``SIMBA`` folders.

Simulation folder
~~~~~~~~~~~~~~~~~
   
Inside each simulation folder there are different files and folders, e.g.:

.. code-block:: bash

   >> ls SIMBA/LH_24
   AGBcyield_v2.tab            fofrad_004.txt  fofrad_019.txt  fof_subhalo_tab_000.hdf5  fof_subhalo_tab_015.hdf5  fof_subhalo_tab_030.hdf5  OUTPUT.err             snap_009.hdf5  snap_024.hdf5
   AGBmdot.tab                 fofrad_005.txt  fofrad_020.txt  fof_subhalo_tab_001.hdf5  fof_subhalo_tab_016.hdf5  fof_subhalo_tab_031.hdf5  OUTPUT.o24             snap_010.hdf5  snap_025.hdf5
   AGBoyield_v2.tab            fofrad_006.txt  fofrad_021.txt  fof_subhalo_tab_002.hdf5  fof_subhalo_tab_017.hdf5  fof_subhalo_tab_032.hdf5  OUTPUT.o632254         snap_011.hdf5  snap_026.hdf5
   balance.txt                 fofrad_007.txt  fofrad_022.txt  fof_subhalo_tab_003.hdf5  fof_subhalo_tab_018.hdf5  fof_subhalo_tab_033.hdf5  parameters-usedvalues  snap_012.hdf5  snap_027.hdf5
   blackhole_details           fofrad_008.txt  fofrad_023.txt  fof_subhalo_tab_004.hdf5  fof_subhalo_tab_019.hdf5  GIZMO.param               script.sh              snap_013.hdf5  snap_028.hdf5
   blackholes.txt              fofrad_009.txt  fofrad_024.txt  fof_subhalo_tab_005.hdf5  fof_subhalo_tab_020.hdf5  GIZMO.param-usedvalues    sfr.txt                snap_014.hdf5  snap_029.hdf5
   CosmoAstro_params.txt       fofrad_010.txt  fofrad_025.txt  fof_subhalo_tab_006.hdf5  fof_subhalo_tab_021.hdf5  gizmo-simba               snap_000.hdf5          snap_015.hdf5  snap_030.hdf5
   cpu.txt                     fofrad_011.txt  fofrad_026.txt  fof_subhalo_tab_007.hdf5  fof_subhalo_tab_022.hdf5  GRACKLE_INFO              snap_001.hdf5          snap_016.hdf5  snap_031.hdf5
   dust.txt                    fofrad_012.txt  fofrad_027.txt  fof_subhalo_tab_008.hdf5  fof_subhalo_tab_023.hdf5  grids                     snap_002.hdf5          snap_017.hdf5  snap_032.hdf5
   energy.txt                  fofrad_013.txt  fofrad_028.txt  fof_subhalo_tab_009.hdf5  fof_subhalo_tab_024.hdf5  ICs                       snap_003.hdf5          snap_018.hdf5  snap_033.hdf5
   ewald_spc_table_64_dbl.dat  fofrad_014.txt  fofrad_029.txt  fof_subhalo_tab_010.hdf5  fof_subhalo_tab_025.hdf5  info.txt                  snap_004.hdf5          snap_019.hdf5  spcool_tables
   fofrad_000.txt              fofrad_015.txt  fofrad_030.txt  fof_subhalo_tab_011.hdf5  fof_subhalo_tab_026.hdf5  logfile                   snap_005.hdf5          snap_020.hdf5  timebin.txt
   fofrad_001.txt              fofrad_016.txt  fofrad_031.txt  fof_subhalo_tab_012.hdf5  fof_subhalo_tab_027.hdf5  OUTPUT                    snap_006.hdf5          snap_021.hdf5  timings.txt
   fofrad_002.txt              fofrad_017.txt  fofrad_032.txt  fof_subhalo_tab_013.hdf5  fof_subhalo_tab_028.hdf5  OUTPUT.e24                snap_007.hdf5          snap_022.hdf5  TREECOOL
   fofrad_003.txt              fofrad_018.txt  fofrad_033.txt  fof_subhalo_tab_014.hdf5  fof_subhalo_tab_029.hdf5  OUTPUT.e632254            snap_008.hdf5          snap_023.hdf5  variable_wind_scaling.txt

The most relevant ones are these:

- ``ICs``. This folder contains the initial conditions of the simulations. See :ref:`ICs` for further details.

- ``snap_0XY.hdf5``. These are the simulation snapshots. Numbers go from 000 (corresponding to :math:`z=6`) to 033 (corresponding to :math:`z=0`). These files contain the positions, velocities, IDs and other properties of the particles and resolution elements of the simulation. See :ref:`snapshots` to see how to read these files.
  
- ``fof_subhalo_tab_0XY.hdf5``. These files contain the halo/galaxy catalogues. Numbers go from 000 (corresponding to :math:`z=6`) to 033 (corresponding to :math:`z=0`). These files contain the properties of the halos and subhalos identified by SUBFIND. See :ref:`halos` to see how to read these files.

- ``CosmoAstro_params.txt``. This file contains the value of the cosmological and astrophysical parameter of the simulation. Format is: :math:`\Omega_{\rm m}`  :math:`\sigma_8`  :math:`A_{\rm SN1}`  :math:`A_{\rm SN2}`   :math:`A_{\rm AGN1}`   :math:`A_{\rm AGN2}`.

.. _Reach out to us: camel.simulations@gmail.com
  
There are many other files in a simulation folder that we do not describe as they are barely used. `Reach out to us`_ if you need help with those.
