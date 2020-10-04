import numpy as np
import sys,os

root = '/mnt/ceph/users/camels/Sims/IllustrisTNG'
fin  = 'latin_hypercube_params.txt'

params = np.loadtxt(fin)

for i in range(1000):
    fout = '%s/LH_%d/CosmoAstro_params.txt'%(root,i)
    if not(os.path.exists(fout)):  
        print(fout)
        f = open(fout, 'w')
        f.write('%.5f %.5f %.5f %.5f %.5f %.5f'\
                %(params[i][0], params[i][1], params[i][2], 
                  params[i][3], params[i][4], params[i][5]))
