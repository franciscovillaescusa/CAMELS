import numpy as np
import sys,os

##################################### INPUT ########################################
root = '/mnt/ceph/users/camels/Sims'
sims = ['SIMBA', 'IllustrisTNG']
####################################################################################

# get the names of the simulations
names = []
for i in range(1000):  names.append('LH_%d'%i)
for i in range(66):    names.append('1P_%d'%i)
for i in range(27):    names.append('CV_%d'%i)
for i in range(4):     names.append('EX_%d'%i)

# do a loop over the different simulations
for sim in sims:

    # open output file
    g = open('../%s/CosmoAstroSeed_params.txt'%sim, 'w')
    
    # do a loop over all the simulations
    for i in names:

        # read Cosmo+Astro params file
        f1 = '%s/%s/%s/CosmoAstro_params.txt'%(root,sim,i)
        Om,s8,A_SN1,A_AGN1,A_SN2,A_AGN2 = np.loadtxt(f1, unpack=True)

        # read initial random seed
        f2 = '%s/%s/%s/ICs/2LPT.param'%(root,sim,i)
        f = open(f2, 'r')
        for line in f.readlines():
            fields = line.split()
            if len(fields)==0:     continue
            if fields[0]=='Seed':  seed = int(fields[1])
        print('%6s %.5f %.5f %.5f %.5f %.5f %.5f %d'\
              %(i,Om,s8,A_SN1,A_AGN1,A_SN2,A_AGN2,seed))
        g.write('%6s %.5f %.5f %.5f %.5f %.5f %.5f %d\n'\
              %(i,Om,s8,A_SN1,A_AGN1,A_SN2,A_AGN2,seed))

    g.close()
