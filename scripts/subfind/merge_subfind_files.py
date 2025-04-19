from camels_library.subfind import merge_subfind


root    = '/mnt/ceph/users/camels/Sims/IllustrisTNG_extras/fNL/L50n512/1P'
snapnum = 90
for folder in ['1P_LC_0_50',
               '1P_LC_200_50',     '1P_LC_n200_50',
               '1P_EQ_200_50',     '1P_EQ_n200_50',
               '1P_OR_CMB_200_50', '1P_OR_CMB_n200_50',
               '1P_OR_LSS_200_50', '1P_OR_LSS_n200_50']:
    
    path = f"{root}/{folder}"
    f_out = f'/mnt/home/fvillaescusa/public_www/fNL_Boris/{folder}/groups_{snapnum:03d}.hdf5'    
    merge_subfind(path, snapnum, f_out, f"logfile_{folder}.log")
