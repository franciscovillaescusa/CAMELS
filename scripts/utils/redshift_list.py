import numpy as np

z_min = 0.0
z_max = 3.0
bins  = 30

z = np.zeros(bins+4, dtype=np.float64)
z[0], z[1], z[2], z[3] = 6.0, 5.0, 4.0, 3.5
z[4:] = np.logspace(np.log10(1.0+z_max), np.log10(1.0+z_min), bins) - 1.0
a = 1.0/(1.0+z)

np.savetxt('../times.txt', a[:-1])
