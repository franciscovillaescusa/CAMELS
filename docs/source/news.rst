News
====

**March 2024** A reorganization of the data has been performed in order to enhance its uniformity and simplicity. This will require slight changes to existing codes that access the data.

- Folders in the 1P sets are now named ``1P_pX_Y`` and each parameter only has 4 variations, rather than 10, such that ``X`` ranges from n2 to 2.
- Snapshot numbers in the IllustrisTNG and SIMBA suites, where simulations have only 34 snapshots, have been updated to match the numbering in the Astrid suite (and some TNG simulations) that have 91 snapshots. For example, where 33 used to be the z=0 snapshot, now it is 90 uniformly for all suites.
- Snapshot files have been renamed from ``snap_###.hdf5`` to ``snapshot_###.hdf5`` and fof/subfind files from ``fof_subhalo_tab_###.hdf5`` to ``groups_###.hdf5``.

**March 2024** A new simulation set, SB28, has been added to the CAMELS-TNG suite. This set comprises of 2,048 new simulations that sample a 28-dimensional parameter space of the IllustrisTNG galaxy formation model, including 5 cosmological parameters and 23 sub-grid physics parameters, which facilitates more comprehensive and robust studies of our uncertainties about cosmological modeling of galaxies and baryons. These simulations have the same volume and resolution as other CAMELS simulations. 91 snapshots were generated for each simulation, and group catalogs and merger trees are available as well. Associated new 1P simulations that sample the additional 22 parameters are also released, in this case both for the IllustrisTNG and SIMBA suites.

**March 2024** A new suite, "GZ28," of 768 massive hydrodynamical zoom-in simulations spanning the IllustrisTNG parameter space has been added. GZ28 employs a novel parameter space sampling method, "CARPoolGP," that leverages correlations between the initial conditions of simulations. See :ref:`zoomGZ` for more details.

**May 2023** The snapshots of the N-body simulations have been compressed. In order to read those snapshots with python, you need to use ``import hdf5`` and ``import hdf5plugin``. See :ref:`snapshots` for details.

**April 2023** All simulations in the Astrid suite are now publicly available. The CAMELS Multifield Dataset has also been updated and now incorporates 2D maps and 3D grids from the Astrid simulations. Halo and galaxy catalogues from both Subfind and Rockstar are also publicly available together with merger trees from SubLink and Consistent trees.

**March 2023:** A new set has been added to the IllustrisTNG suite: the BE set, for "Butterfly Effect". These 27 simulations all have the exact same initial conditions and are run with the fiducial TNG model, while capturing the intrinsic randomness of the simulation results.

**March 2023:** SubLink merger trees have been added for the IllustrisTNG suite.

**August 2022:** The CAMELS binder now has Pylians3 and the CAMELS library preinstalled.

**July 2022:** CAMELS has grown! The Astrid suite  --  containing 1,092 state-of-the-art hydrodynamic simulations run with the MP-Gadget code employing the same subgrid model as the Astrid simulation  -- has been added to CAMELS. The N-body counterparts of these simulations are also available.


