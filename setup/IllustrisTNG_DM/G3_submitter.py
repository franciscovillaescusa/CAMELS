import numpy as np
import sys,os

####################################### INPUT ###########################################
nodes_per_sim = 1
start         = 800   #first realization to do
end           = 1000   #last  realization do do
#########################################################################################

# do a loop over the different jobs
for i in xrange(start,end,1):
    
    script="""#!/bin/bash
#SBATCH --job-name=%d
#SBATCH -o OUTPUT.o%d
#SBATCH -e OUTPUT.e%d  
#SBATCH --partition=general
#####SBATCH --partition=preempt
#SBATCH --nodes=%d
#SBATCH --ntasks-per-node=48
#SBATCH --export=ALL
#SBATCH -t 7-00:00    

module purge
module load slurm
module load gcc
module load openmpi
module load lib/fftw2/2.1.5-openmpi1
module load lib/gsl
module load lib/hdf5

LPT_code="/simons/scratch/fvillaescusa/CAMEL/Software/2lpt/2LPTic"
G3="/simons/scratch/fvillaescusa/CAMEL/Codes/Gadget_III/P-Gadget3"
root="/simons/scratch/fvillaescusa/CAMEL/Sims/IllustrisTNG_DM/"

folder=$root"%d"
cd $folder

if [ ! -f snap_033.hdf5 ]; then

    if [ ! -f sim_stopped ]; then

        if [ ! -f restartfiles/restart.0 ]; then

           cd ICs
           mpirun -n 8 $LPT_code 2LPT.param >> logIC
           cd ..
           mpirun -n %d $G3 G3.param >> logfile    

        else

           mpirun -n %d $G3 G3.param 1 >> logfile    

        fi
    fi
fi
    """%(i, i, i, nodes_per_sim, i, nodes_per_sim*48, nodes_per_sim*48)

    # write the submission script inside each folder
    f = open('/simons/scratch/fvillaescusa/CAMEL/Sims/IllustrisTNG_DM/%d/script.sh'%i, 'w')
    f.write(script);  f.close()
    os.chdir('/simons/scratch/fvillaescusa/CAMEL/Sims/IllustrisTNG_DM/%d/'%i)
    os.system('sbatch script.sh')
