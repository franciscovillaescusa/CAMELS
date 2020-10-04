import numpy as np
import sys,os

####################################### INPUT ###########################################
nodes_per_sim = 1
start         = 0   #350   #first realization to do
end           = 87 #400   #last  realization do do
#########################################################################################
# 0-10
#11-21
#22-32
#33-43
#44-54
#55-65

#numbers = np.array([1501, 1503, 1505, 1507, 1509,
#                    1512, 1514,       1518, 1520,
#                    1523, 1525,       1529, 1531,
#                    1534, 1536,       1540, 1542,
#                    1545, 1547,       1551, 1553,
#                    1556, 1558,       1562, 1564])
numbers = np.array(['1505_0', '1505_1', '1505_2', '1505_3', '1505_4'])

# do a loop over the different jobs
for i in numbers:
    
    script="""#!/bin/bash
#SBATCH --job-name=%s
#SBATCH -o OUTPUT.o%s
#SBATCH -e OUTPUT.e%s  
#SBATCH --partition=general
#####SBATCH --partition=preempt
#SBATCH --nodes=%d
#SBATCH --ntasks-per-node=48
#SBATCH --export=ALL
#SBATCH -t 7-00:00    
#####SBATCH --mail-type=ALL
#####SBATCH --mail-user=villaescusa.francisco@gmail.com

module purge
module load slurm
module load gcc
module load openmpi
module load lib/fftw2/2.1.5-openmpi1
module load lib/gsl
module load lib/hdf5
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/dangles/local/grackle_popeye/lib
LPT_code="/simons/scratch/fvillaescusa/hydro_DL/Software/2lpt/2LPTic"

root="/simons/scratch/fvillaescusa/hydro_DL/SIMBA/"

folder=$root"%s"
cd $folder

if [ ! -f snap_033.hdf5 ]; then

    #if [ ! -f restartfiles/restart.0 ]; then

        cd ICs
        mpirun -n 8 $LPT_code 2LPT.param >> logIC
        cd ..
        mpirun -n %d ./gizmo-mufasa/GIZMO GIZMO.param >> logfile    

        #else

        #mpirun -n %d ./gizmo-mufasa/GIZMO GIZMO.param 1 >> logfile    

    #fi
fi
    """%(i, i, i, nodes_per_sim, i, nodes_per_sim*48, nodes_per_sim*48)

    # write the submission script inside each folder
    f = open('/simons/scratch/fvillaescusa/hydro_DL/SIMBA/%s/script.sh'%i, 'w')
    f.write(script);  f.close()
    os.chdir('/simons/scratch/fvillaescusa/hydro_DL/SIMBA/%s/'%i)
    os.system('sbatch script.sh')
