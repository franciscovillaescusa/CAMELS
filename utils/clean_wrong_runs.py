# There were some problems with some simulations. We use this script to delete the data
# products of them, so we can rerun the pipeline cleanly
import numpy as np
import sys,os

#################################### INPUT ###########################################
root = '/mnt/ceph/users/camels/Results'
sim  = 'IllustrisTNG' 
wrong_realizations = ['LH_118', 'LH_142', 'LH_147', 'LH_185', 'LH_260', 'LH_261',
                      'LH_263', 'LH_291', 'LH_547', 'LH_563', 'LH_579', 'LH_596']
folders = ['baryon_fraction', 'baryon_fraction_SO', 'BH', 'HMF', 'Pk', 'Pk_ratio', 
           'Radii', 'SFR', 'SFRH', 'SMF', 'SO', 'Vmax']
######################################################################################

# do a loop over all the realizations that went wrong
for wr in wrong_realizations:

    # do a loop over the different folders
    for folder in folders:

        # get the name of the folder with the results
        fin = '%s/%s/%s/%s'%(root,folder,sim,wr)
        os.system('rm -rf %s'%fin)
