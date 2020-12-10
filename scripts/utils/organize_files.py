import numpy as np
import sys,os,glob

##################################### INPUT ############################################
root  = '/simons/scratch/fvillaescusa/CAMELS/Sims'
sim   = 'SIMBA'
#files = ['info.txt','logfile','memory_*','OUTPUT.*','parameters-usedvalues',
#         'PIDs.txt', 'processes_*','ps_*','balance.txt','cpu.txt','energy.txt',
#         'ewald_*','free_*','G3.param-usedvalues','Timebin.txt','timings.txt',
#         'script.sh']
files = ['AGB*', 'balance.txt', 'blackhole*', 'cpu.txt', 'dust.txt', 'energy.txt',
         'ewald_spc_table_64_dbl.dat', 'fofrad_*', 'GIZMO.param-usedvalues',
         'GRACKLE_INFO', 'info.txt', 'logfile', 'OUTPUT*', 'parameter-usedvalues',
         'script.sh', 'spcool_tables', 'timebin.txt', 'timing.txt', 'TREECOOL']
########################################################################################

numbers = np.arange(1000)
#numbers = np.hstack([numbers, np.arange(1500, 1522)])
#numbers = np.hstack([numbers, ['1505_0', '1505_1', '1505_2', '1505_3', '1505_4',
#                               '1505_5', '1505_6', '1505_7', '1505_8', '1505_9',
#                               '1505_10', '1505_11', '1505_12', '1505_13', '1505_14',
#                               '1505_15', '1505_16', '1505_17', '1505_18', '1505_19',
#                               '1505_20', '1505_21', '1505_22', '1505_23', '1505_24',
#                               '1505_25', '1505_26']])

# do a loop over all realizations
for i in numbers:

    folder = '%s/%s/%s/'%(root,sim,i)

    # create extra folder if it doesnt exists
    folder_extra = '%s/extra_files/'%folder
    if not(os.path.exists(folder_extra)):
        os.system('mkdir %s'%folder_extra)
    
    for f in files:
        if len(glob.glob('%s/%s'%(folder,f)))>0:
            os.system('mv %s/%s %s/'%(folder,f,folder_extra))
    
