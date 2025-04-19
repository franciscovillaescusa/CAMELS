from mpi4py import MPI
import os, sys
from camels_library.ramses import ramses_2_hdf5 

# MPI setup
comm   = MPI.COMM_WORLD
rank   = comm.Get_rank()
size   = comm.Get_size()

# Construct the list of folders to process
tasks = []
for p in range(1, 10):  # [1,2,...,9]
    for suffix in ['n2', '0', '2']:
        folder = f"1P_p{p}_{suffix}"
        if os.path.exists(f'../1P/{folder}'):
            tasks.append(folder)

# Distribute tasks across ranks
tasks = sorted(tasks)
tasks_per_rank = tasks[rank::size]  # Round-robin distribution

print(rank, tasks_per_rank)

# Main processing loop
for folder in tasks_per_rank:
    os.makedirs(folder, exist_ok=True)

    snapshot = f'../1P/{folder}/output_00092'
    BoxSize  = 50000  # kpc/h
    fout     = f'{folder}/snap_090.hdf5'

    if os.path.exists(fout):  continue

    print(f"[Rank {rank}] Converting {folder}")
    try:
        R2H = ramses_2_hdf5(snapshot, BoxSize)
        R2H.write_hdf5(fout)
    except Exception as e:
        print(f"[Rank {rank}] ❌ Error in {folder}: {e}")
        raise
