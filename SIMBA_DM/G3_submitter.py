import numpy as np
import sys,os

####################################### INPUT ###########################################
nodes_per_sim = 1
start         = 500     #first realization to do
end           = 1000   #last  realization do do
#########################################################################################

#numbers = np.arange(1500, 1522, 1)
numbers = ['1505_5',  '1505_6',  '1505_7',  '1505_8',  '1505_9', 
           '1505_10', '1505_11', '1505_12', '1505_13', '1505_14',
           '1505_15', '1505_16', '1505_17', '1505_18', '1505_19', 
           '1505_20', '1505_21', '1505_22', '1505_23', '1505_24',
           '1505_25', '1505_26', '1505_EX']

# do a loop over the different jobs
for i in numbers: #xrange(start,end,1):
    
    script="""#!/bin/bash
#SBATCH --job-name=%s
#SBATCH -o OUTPUT.o%s
#SBATCH -e OUTPUT.e%s  
#SBATCH --partition=general
#####SBATCH --partition=preempt
#SBATCH --nodes=%d
#SBATCH --ntasks-per-node=48
#SBATCH --export=ALL
#SBATCH -t 1-00:00    

module purge
module load slurm
module load gcc
module load openmpi
module load lib/fftw2/2.1.5-openmpi1
module load lib/gsl
module load lib/hdf5

LPT_code="/simons/scratch/fvillaescusa/CAMELS/Codes/2lpt/2LPTic"
G3="/simons/scratch/fvillaescusa/CAMELS/Codes/Gadget_III/P-Gadget3"
root="/simons/scratch/fvillaescusa/CAMELS/Sims/SIMBA_DM/"

folder=$root"%s"
cd $folder

if [ ! -f snap_033.hdf5 ]; then
    if [ ! -f restartfiles/restart.0 ]; then
        cd ICs
        mpirun -n 8 $LPT_code 2LPT.param >> logIC
        cd ..
        mpirun -n %d $G3 G3.param >> logfile    
    else
        mpirun -n %d $G3 G3.param 1 >> logfile    
    fi
fi
    """%(i, i, i, nodes_per_sim, i, nodes_per_sim*48, nodes_per_sim*48)

    # write the submission script inside each folder
    f = open('/simons/scratch/fvillaescusa/CAMELS/Sims/SIMBA_DM/%s/script.sh'%i, 'w')
    f.write(script);  f.close()
    os.chdir('/simons/scratch/fvillaescusa/CAMELS/Sims/SIMBA_DM/%s/'%i)

    os.system('sbatch script.sh')
