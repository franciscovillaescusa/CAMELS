import numpy as np
import sys,os






scale_factors = np.loadtxt('times_extended.txt')
scale_factors2 = np.loadtxt('times.txt')
zs  = 1.0/scale_factors-1
zs2 = 1.0/scale_factors2-1

f = open('redshift_table.txt', 'w')
f.write('+----------+--------------+--------------+---------+--------+\n')
f.write('| Redshift | Scale Factor | IllustrisTNG | SIMBA   | Astrid |\n')
f.write('+==========+==============+==============+=========+========+\n')

i,j = 0, 0
for z in zs:
    if np.absolute(scale_factors[i]/scale_factors2[j]-1)<1e-2:
        symbol = '%03d'%j
        j+=1
    else:
        symbol = '---'
    
    if z>10.0:
        f.write('| %.2f    |  %.3f       |    %s       |  %s    |   %03d  |\n'%(z,1.0/(z+1),symbol,symbol,i))
    else: 
        f.write('| %.2f     |  %.3f       |    %s       |  %s    |   %03d  |\n'%(z,1.0/(z+1),symbol,symbol,i))
    f.write('+----------+--------------+--------------+---------+--------+\n')
    i+=1
