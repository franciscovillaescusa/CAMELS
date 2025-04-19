# A set of routines to combine several subfind files into a single one
import numpy as np
import sys,os,h5py
from tqdm import trange
import tempfile, pathlib
import logging


def merge_datasets(source_group, target_group, log):
    """
    Merge or append datasets from source_group into target_group.
    Assumes datasets can be concatenated along axis 0.
    """
    for dataset_name in source_group.keys():
        data = source_group[dataset_name][...]  # Read full dataset

        if dataset_name not in target_group:
            # Create dataset with extendable shape and optional compression
            target_group.create_dataset(dataset_name, data=data,
                                        maxshape=(None,) + data.shape[1:],
                                        chunks=True, compression="gzip",
                                        compression_opts=4)
        else:
            existing  = target_group[dataset_name]
            old_shape = existing.shape
            new_shape = (old_shape[0] + data.shape[0],) + old_shape[1:]

            existing.resize(new_shape)
            existing[old_shape[0]:] = data

            
def merge_attributes(source_attrs, target_attrs, group_name, counters, log):
    """
    Merge or validate attributes from source_attrs into target_attrs.

    Updates counters for Nids, Nsubgroups, and Ngroups, and reports any mismatches.
    """
    for attr_name, attr_value in source_attrs.items():
        if attr_name == 'Nids_ThisFile':
            counters['Nids_ThisFile'] += attr_value
        elif attr_name == 'Nsubgroups_ThisFile':
            counters['Nsubgroups_ThisFile'] += attr_value
        elif attr_name == 'Ngroups_ThisFile':
            counters['Ngroups_ThisFile'] += attr_value

        if attr_name not in target_attrs:
            target_attrs[attr_name] = attr_value
        else:
            existing_value = target_attrs[attr_name]
            if not np.array_equal(existing_value, attr_value):
                log.warning(f"""⚠️  Attribute mismatch in group '{group_name}' for '{attr_name}':
Existing: {existing_value}
New:      {attr_value}""")

                
def write_final_output(temp_file, output_file, counters, log):
    """
    This function takes the temporary file and copies it to the final output.
    Mostly done to avoid inf in the .hdf5 file
    """
    with h5py.File(temp_file, 'r') as f_in, h5py.File(output_file, 'w') as f_out:
        for group_name in f_in:
            f_in_group  = f_in[group_name]
            f_out_group = f_out.create_group(group_name)

            # Copy attributes
            for attr_name, attr_value in f_in_group.attrs.items():
                if attr_name in counters:
                    f_out_group.attrs[attr_name] = counters[attr_name]
                else:
                    f_out_group.attrs[attr_name] = attr_value

            # Copy datasets
            for dataset_name in f_in_group:
                data = f_in_group[dataset_name][...]
                f_out_dset = f_out_group.create_dataset(dataset_name, data=data)
                for attr_name, attr_value in f_in_group[dataset_name].attrs.items():
                    f_out_dset.attrs[attr_name] = attr_value

                    
def validate_merged_subfind(hdf5_file, log):
    """
    Validate that the number of groups and subhalos in the datasets
    match the Ngroups_ThisFile and Nsubgroups_ThisFile attributes in Header.

    Args:
        hdf5_file (str): Path to the merged HDF5 file
    """

    with h5py.File(hdf5_file, 'r') as f:
        # Read lengths from datasets
        n_groups   = len(f["Group"]["GroupPos"])
        n_subhalos = len(f["Subhalo"]["SubhaloPos"])

        # Read header attributes
        header = f["Header"].attrs
        n_groups_attr = header["Ngroups_ThisFile"]
        n_subhalos_attr = header["Nsubgroups_ThisFile"]

        if n_groups != n_groups_attr:
            log.error(f"""❌ Mismatch: Group count does not match header attribute!
Groups in dataset:  {n_groups}
Groups in header:   {n_groups_attr}""")
            raise Exception('Check group lengths!')
        else:
            log.info("✅ Group count matches.")
            
        if n_subhalos != n_subhalos_attr:
            log.error(f"""❌ Mismatch: Subhalo count does not match header attribute!
Subhalos in dataset: {n_subhalos}")
Subhalos in header:  {n_subhalos_attr}""")
            raise Exception('Check subhalo lengths!')
        else:
            log.info("✅ Subhalo count matches.") 

        # for non-TNG snapshots, we should also add a validation about number of IDs
        # but for TNG, the subfind files do not have IDs


def merge_subfind(path, snapnum, output_file, logfile='merge_subfind.log'):
    """
    This function will merge several subfind files into a single one

    Args:
       path: location of the subfind catalogs, e.g. '/mnt/ceph/users/camels/Sims/IllustrisTNG_extras/fNL/L50n512/1P/1P_LC_200_50'
       snapnum: the number of the considered catalog, e.g. 90 (z=0 for CAMELS)
       f_out: name of output file
       logfile: name of logfile
    """

    # Configure the logger
    logging.basicConfig(level=logging.INFO,  # Set default level
                        format="%(asctime)s [%(levelname)s] %(message)s", 
                        handlers=[logging.StreamHandler(sys.stdout),
                                  logging.FileHandler(logfile, mode='w')])
    log = logging.getLogger(__name__)

    # get the catalog root name
    root = f"{path}/groups_{snapnum:03d}/fof_subhalo_tab_{snapnum:03d}"

    # get the number of subfiles
    with h5py.File(f'{root}.0.hdf5', 'r') as f:
        Nfiles = f['Header'].attrs['NumFiles']

    # temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".hdf5", delete=False).name

    # These attributes will be changed in the merged file
    counters = {'Nids_ThisFile': 0, 'Nsubgroups_ThisFile': 0, 'Ngroups_ThisFile': 0}

    # Open the output file in write mode
    with h5py.File(temp_file, 'w') as f_out:

        # Loop over each input file
        for i in trange(Nfiles, desc="Merging files"):

            input_file = f'{root}.{i}.hdf5'
            with h5py.File(input_file, 'r') as f_in:

                # do a loop over the different groups in the file
                for group_name in f_in.keys():

                    # Create or access the group in the output file
                    if group_name not in f_out:
                        f_out_group = f_out.create_group(group_name)
                    else:
                        f_out_group = f_out[group_name]

                    # Merge or validate attributes in the group
                    merge_attributes(f_in[group_name].attrs, f_out_group.attrs,
                                     group_name, counters, log)

                    # Merge or concatenate datasets in the group
                    merge_datasets(f_in[group_name], f_out_group, log)
                    

    # move content from temporary file to output file (done to avoid inf in the temp file)
    try:
        write_final_output(temp_file, output_file, counters, log)
    finally:
        pathlib.Path(temp_file).unlink(missing_ok=True)

    validate_merged_subfind(output_file, log)
    log.info("Files merged successfully!")
