from pylab import *
import numpy as np
from matplotlib.ticker import ScalarFormatter
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from matplotlib.ticker import AutoMinorLocator
from matplotlib.colors import LogNorm
from matplotlib.patches import Ellipse
rcParams["mathtext.fontset"]='cm'


################################## INPUT #######################################
root  = '/mnt/ceph/users/camels/Results'
f_out = 'different_seed_CV.pdf'

# Pk m
f11 = '%s/Pk/IllustrisTNG/mean_CV_Pk_m_z=0.00.txt'%root
f12 = '%s/Pk/SIMBA/mean_CV_Pk_m_z=0.00.txt'%root
#f12 = '%s/Pk/SIMBA_OLD/mean_Pk_m_z=0.00.txt'%root
f13 = '%s/Pk/IllustrisTNG/extreme_0/Pk_m_z=0.00.txt'%root
f14 = '%s/Pk/IllustrisTNG/extremestellar_0/Pk_m_z=0.00.txt'%root
f15 = '%s/Pk/IllustrisTNG/noFB_0/Pk_m_z=0.00.txt'%root

# Pk g
f21 = '%s/Pk/IllustrisTNG/mean_CV_Pk_g_z=0.00.txt'%root
f22 = '%s/Pk/SIMBA/mean_CV_Pk_g_z=0.00.txt'%root
#f22 = '%s/Pk/SIMBA_OLD/mean_Pk_g_z=0.00.txt'%root
f23 = '%s/Pk/IllustrisTNG/extreme_0/Pk_g_z=0.00.txt'%root
f24 = '%s/Pk/IllustrisTNG/extremestellar_0/Pk_g_z=0.00.txt'%root
f25 = '%s/Pk/IllustrisTNG/noFB_0/Pk_g_z=0.00.txt'%root

# ratio Pk m
f31 = '%s/Pk_ratio/IllustrisTNG/mean_CV_Pk_ratio_m_z=0.00.txt'%root
f32 = '%s/Pk_ratio/SIMBA/mean_CV_Pk_ratio_m_z=0.00.txt'%root
#f32 = '%s/Pk_ratio/SIMBA_OLD/mean_Pk_ratio_m_z=0.00.txt'%root
#f33 = '%s/Pk/IllustrisTNG/extreme_0/Pk_g_z=0.00.txt'%root
#f34 = '%s/Pk/IllustrisTNG/extremestellar_0/Pk_g_z=0.00.txt'%root
#f35 = '%s/Pk/IllustrisTNG/noFB_0/Pk_g_z=0.00.txt'%root

# HMF
f41 = '%s/HMF/IllustrisTNG/mean_CV_mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f42 = '%s/HMF/SIMBA/mean_CV_mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root
#f42 = '%s/HMF/SIMBA_OLD/mean_mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f43 = '%s/HMF/IllustrisTNG/extreme_0/mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f44 = '%s/HMF/IllustrisTNG/extremestellar_0/mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f45 = '%s/HMF/IllustrisTNG/noFB_0/mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root

# SFRH
f51 = '%s/SFRH/IllustrisTNG/mean_CV_SFRH_0.00_10.00_10000.txt'%root
f52 = '%s/SFRH/SIMBA/mean_CV_SFRH_0.00_10.00_10000.txt'%root
#f52 = '%s/SFRH/SIMBA_OLD/mean_SFRH_0.00_10.00_10000.txt'%root
f53 = '%s/SFRH/IllustrisTNG/extreme_0/SFRH_0.00_10.00_10000.txt'%root
f54 = '%s/SFRH/IllustrisTNG/extremestellar_0/SFRH_0.00_10.00_10000.txt'%root
f55 = '%s/SFRH/IllustrisTNG/noFB_0/SFRH_0.00_10.00_10000.txt'%root

# SMF
f61 = '%s/SMF/IllustrisTNG/mean_CV_SMF_1.00e+09_5e+11_10_z=0.00.txt'%root
f62 = '%s/SMF/SIMBA/mean_CV_SMF_1.00e+09_5e+11_10_z=0.00.txt'%root
#f62 = '%s/SMF/SIMBA_OLD/mean_SMF_1.00e+09_5e+11_10_z=0.00.txt'%root
f63 = '%s/SMF/IllustrisTNG/extreme_0/SMF_1.00e+09_5e+11_10_z=0.00.txt'%root
f64 = '%s/SMF/IllustrisTNG/extremestellar_0/SMF_1.00e+09_5e+11_10_z=0.00.txt'%root
f65 = '%s/SMF/IllustrisTNG/noFB_0/SMF_1.00e+09_5e+11_10_z=0.00.txt'%root

# baryon fraction
f71 = '%s/baryon_fraction/IllustrisTNG/mean_CV_bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f72 = '%s/baryon_fraction/SIMBA/mean_CV_bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root
#f72 = '%s/baryon_fraction/SIMBA_OLD/mean_bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f73 = '%s/baryon_fraction/IllustrisTNG/extreme_0/bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f74 = '%s/baryon_fraction/IllustrisTNG/extremestellar_0/bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f75 = '%s/baryon_fraction/IllustrisTNG/noFB_0/bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root

# halos temperature
f81 = '%s/SO/IllustrisTNG/mean_T_CV_1.00e+12_1.00e+14_10_z=0.00.txt'%root
f82 = '%s/SO/SIMBA/mean_T_CV_1.00e+12_1.00e+14_10_z=0.00.txt'%root
#f82 = '%s/SO/SIMBA_OLD/mean_T_1.00e+12_1.00e+14_10_z=0.00.txt'%root
f83 = '%s/SO/IllustrisTNG/extreme_0/SO_z=0.00.txt'%root
f84 = '%s/SO/IllustrisTNG/extremestellar_0/SO_z=0.00.txt'%root
f85 = '%s/SO/IllustrisTNG/noFB_0/SO_z=0.00.txt'%root

# galaxies radius
f91 = '%s/Radii/IllustrisTNG/mean_R_vs_SM_CV_z=0.00.txt'%root
f92 = '%s/Radii/SIMBA/mean_R_vs_SM_CV_z=0.00.txt'%root
#f92 = '%s/Radii/SIMBA_OLD/mean_R_vs_SM_z=0.00.txt'%root
f93 = '%s/Radii/IllustrisTNG/extreme_0/R_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root
f94 = '%s/Radii/IllustrisTNG/extremestellar_0/R_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root
f95 = '%s/Radii/IllustrisTNG/noFB_0/R_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root

# Black hole masses
f101 = '%s/BH/IllustrisTNG/mean_BH_vs_SM_CV_z=0.00.txt'%root
f102 = '%s/BH/SIMBA/mean_BH_vs_SM_CV_z=0.00.txt'%root
#f102 = '%s/BH/SIMBA_OLD/mean_BH_vs_SM_z=0.00.txt'%root
f103 = '%s/BH/IllustrisTNG/extreme_0/BH_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root
f104 = '%s/BH/IllustrisTNG/extremestellar_0/BH_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root
f105 = '%s/BH/IllustrisTNG/noFB_0/BH_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root

# Vmax
f111 = '%s/Vmax/IllustrisTNG/mean_V_vs_SM_CV_z=0.00.txt'%root
f112 = '%s/Vmax/SIMBA/mean_V_vs_SM_CV_z=0.00.txt'%root
#f112 = '%s/Vmax/SIMBA_OLD/mean_V_vs_SM_z=0.00.txt'%root
f113 = '%s/Vmax/IllustrisTNG/extreme_0/Vmax_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root
f114 = '%s/Vmax/IllustrisTNG/extremestellar_0/Vmax_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root
f115 = '%s/Vmax/IllustrisTNG/noFB_0/Vmax_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root

# SFR
f121 = '%s/SFR/IllustrisTNG/mean_SFR_vs_SM_CV_z=0.00.txt'%root
f122 = '%s/SFR/SIMBA/mean_SFR_vs_SM_CV_z=0.00.txt'%root
#f122 = '%s/SFR/SIMBA_OLD/mean_SFR_vs_SM_z=0.00.txt'%root
f123 = '%s/SFR/IllustrisTNG/extreme_0/SFR_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root
f124 = '%s/SFR/IllustrisTNG/extremestellar_0/SFR_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root
f125 = '%s/SFR/IllustrisTNG/noFB_0/SFR_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root
################################################################################

fig  = figure(figsize=(20,22)) 
gs   = gridspec.GridSpec(4,3)
ax1  = plt.subplot(gs[0])
ax2  = plt.subplot(gs[1])
ax3  = plt.subplot(gs[2])
ax4  = plt.subplot(gs[3])
ax5  = plt.subplot(gs[4])
ax6  = plt.subplot(gs[5])
ax7  = plt.subplot(gs[6])
ax8  = plt.subplot(gs[7])
ax9  = plt.subplot(gs[8])
ax10 = plt.subplot(gs[9])
ax11 = plt.subplot(gs[10])
ax12 = plt.subplot(gs[11])
subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.2)

###### Pk m plot ######
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlim([0.3,35])
ax1.set_ylim([1e-1,1e3])
ax1.set_xlabel(r'$k\,[h{\rm Mpc}^{-1}]$',fontsize=18)
ax1.set_ylabel(r'$P_{\rm m}(k)\,[h^{-3}{\rm Mpc}^3]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f11, unpack=True)
ax1.fill_between(X, dYp, dYm, color='blue')
p1,=ax1.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f12, unpack=True)
ax1.fill_between(X, dYp, dYm, color='red', alpha=0.6)
p2,=ax1.plot(X,Ym,c='k',linestyle='--')

X,Y = np.loadtxt(f13, unpack=True)
#p3,=ax1.plot(X,Y,c='g',linestyle='-')

X,Y = np.loadtxt(f14, unpack=True)
#p3,=ax1.plot(X,Y,c='g',linestyle='--')

X,Y = np.loadtxt(f15, unpack=True)
#p3,=ax1.plot(X,Y,c='g',linestyle='dotted')
#######################

###### Pk g plot ######
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlim([0.3,35])
ax2.set_ylim([1e-2,1e3])
ax2.set_xlabel(r'$k\,[h{\rm Mpc}^{-1}]$',fontsize=18)
ax2.set_ylabel(r'$P_{\rm g}(k)\,[h^{-3}{\rm Mpc}^3]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f21, unpack=True)
ax2.fill_between(X, dYp, dYm, color='blue')
ax2.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f22, unpack=True)
ax2.fill_between(X, dYp, dYm, color='red', alpha=0.6)
ax2.plot(X,Ym,c='k',linestyle='--')

X,Y = np.loadtxt(f23, unpack=True)
#p3,=ax2.plot(X,Y,c='g',linestyle='-')

X,Y = np.loadtxt(f24, unpack=True)
#p3,=ax2.plot(X,Y,c='g',linestyle='--')

X,Y = np.loadtxt(f25, unpack=True)
#p3,=ax2.plot(X,Y,c='g',linestyle='dotted')
#######################

###### ratio Pk m plot ######
ax3.set_xscale('log')
ax3.set_xlim([0.3,35])
ax3.set_ylim([0.5,1.05])
ax3.set_xlabel(r'$k\,[h{\rm Mpc}^{-1}]$',fontsize=18)
ax3.set_ylabel(r'$P_{\rm hydro}(k)/P_{\rm Nbody}(k)$',fontsize=18)

X,Y,dY,dYp,dYm,Ym= np.loadtxt(f31, unpack=True)
ax3.fill_between(X, dYp, dYm, color='blue')
ax3.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f32, unpack=True)
ax3.fill_between(X, dYp, dYm, color='red', alpha=0.6)
ax3.plot(X,Ym,c='k',linestyle='--')
#######################

######### HMF #########
ax4.set_xscale('log')
ax4.set_yscale('log')
ax4.set_xlabel(r'$M_{\rm halo}/\Omega_{\rm m}\,[h^{-1}M_\odot]$',fontsize=18)
ax4.set_ylabel(r'${\rm HMF}\,[h^{4}{\rm Mpc}^{-3}M_\odot^{-1}]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f41, unpack=True)
ax4.fill_between(X, dYp, dYm, color='blue')
ax4.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f42, unpack=True)
ax4.fill_between(X, dYp, dYm, color='red', alpha=0.6)
ax4.plot(X,Ym,c='k',linestyle='--')

dumb,X,Y = np.loadtxt(f43, unpack=True)
#p3,=ax4.plot(X,Y,c='g',linestyle='-')

dumb,X,Y = np.loadtxt(f44, unpack=True)
#p3,=ax4.plot(X,Y,c='g',linestyle='--')

dumb,X,Y = np.loadtxt(f45, unpack=True)
#p3,=ax4.plot(X,Y,c='g',linestyle='dotted')
#######################

###### SFRH ######
ax5.set_yscale('log')
ax5.set_xlim([0.0,7.0])
ax5.set_ylim([5e-4,0.2])
ax5.set_xlabel(r'$z$',fontsize=18)
ax5.set_ylabel(r'${\rm SFRH}\,[M_\odot{\rm yr}^{-1}{\rm Mpc}^{-3}]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f51, unpack=True)
ax5.fill_between(X, dYp, dYm, color='blue')
ax5.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f52, unpack=True)
ax5.fill_between(X, dYp, dYm, color='red', alpha=0.6)
ax5.plot(X,Ym,c='k',linestyle='--')

X,Y = np.loadtxt(f53, unpack=True)
#p3,=ax5.plot(X,Y,c='g',linestyle='-')

X,Y = np.loadtxt(f54, unpack=True)
#p3,=ax5.plot(X,Y,c='g',linestyle='--')

X,Y = np.loadtxt(f55, unpack=True)
#p3,=ax5.plot(X,Y,c='g',linestyle='dotted')
#######################

###### SMF ######
ax6.set_xscale('log')
ax6.set_yscale('log')
ax6.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax6.set_ylabel(r'${\rm SMF}\,[h^4{\rm Mpc}^{-3}M_\odot^{-1}]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f61, unpack=True)
ax6.fill_between(X, dYp, dYm, color='blue')
ax6.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f62, unpack=True)
ax6.fill_between(X, dYp, dYm, color='red', alpha=0.6)
ax6.plot(X,Ym,c='k',linestyle='--')

X,Y = np.loadtxt(f63, unpack=True)
#p3,=ax6.plot(X,Y,c='g',linestyle='-')

X,Y = np.loadtxt(f64, unpack=True)
#p3,=ax6.plot(X,Y,c='g',linestyle='--')

X,Y = np.loadtxt(f65, unpack=True)
#p3,=ax6.plot(X,Y,c='g',linestyle='dotted')
#######################

###### baryon fraction ######
ax7.set_xscale('log')
ax7.set_xlabel(r'$M_{\rm halo}/\Omega_{\rm m}\,[h^{-1}M_\odot]$',fontsize=18)
ax7.set_ylabel(r'$M_{\rm b}/M_{\rm halo}/(\Omega_{\rm b}/\Omega_{\rm m})$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f71, unpack=True)
ax7.fill_between(X, dYp, dYm, color='blue')
ax7.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f72, unpack=True)
ax7.fill_between(X, dYp, dYm, color='red', alpha=0.6)
ax7.plot(X,Ym,c='k',linestyle='--')

X,Y = np.loadtxt(f73, unpack=True)
#p3,=ax7.plot(X,Y,c='g',linestyle='-')

X,Y = np.loadtxt(f74, unpack=True)
#p3,=ax7.plot(X,Y,c='g',linestyle='--')

X,Y = np.loadtxt(f75, unpack=True)
#p3,=ax7.plot(X,Y,c='g',linestyle='dotted')
#######################

######## halos temperature #######
ax8.set_xscale('log')
ax8.set_yscale('log')
ax8.set_xlabel(r'$M_{\rm halo}\,[h^{-1}M_\odot]$',fontsize=18)
ax8.set_ylabel(r'$T_{\rm halo}\,[K]$',fontsize=18)

#X,Y,dY,N = np.loadtxt(f81, unpack=True)
#ax8.fill_between(X, Y+dY, Y-dY, color='blue')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f81, unpack=True)
ax8.fill_between(X, dYp, dYm, color='blue')
ax8.plot(X,Ym,c='k',linestyle='-')

#X,Y,dY,N = np.loadtxt(f82, unpack=True)
#ax8.fill_between(X, Y+dY, Y-dY, color='red', alpha=0.6)
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f82, unpack=True)
ax8.fill_between(X, dYp, dYm, color='red', alpha=0.6)
ax8.plot(X,Ym,c='k',linestyle='--')

#data = np.loadtxt(f83)
#ax8.plot(data[:,0], data[:,9],c='k',linestyle='--')

#data = np.loadtxt(f84)
#ax8.plot(data[:,0], data[:,9],c='k',linestyle='--')

#data = np.loadtxt(f85)
#ax8.plot(data[:,0], data[:,9],c='k',linestyle='--')
##################################

############# Radii ##############
ax9.set_xscale('log')
ax9.set_yscale('log')
ax9.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax9.set_ylabel(r'$R_{1/2}\,[h^{-1}{\rm kpc}]$',fontsize=18)

#X,Y,dY,N = np.loadtxt(f91, unpack=True)
#ax9.fill_between(X, Y+dY, Y-dY, color='blue')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f91, unpack=True)
ax9.fill_between(X, dYp, dYm, color='blue')
ax9.plot(X,Ym,c='k',linestyle='-')

#X,Y,dY,N = np.loadtxt(f92, unpack=True)
#ax9.fill_between(X, Y+dY, Y-dY, color='red', alpha=0.6)
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f92, unpack=True)
ax9.fill_between(X, dYp, dYm, color='red', alpha=0.6)
ax9.plot(X,Ym,c='k',linestyle='--')

X,Y,dY = np.loadtxt(f93, unpack=True)
#p3,=ax9.plot(X,Y,c='g',linestyle='-')

X,Y,dY = np.loadtxt(f94, unpack=True)
#p3,=ax9.plot(X,Y,c='g',linestyle='--')

X,Y,dY = np.loadtxt(f95, unpack=True)
#p3,=ax9.plot(X,Y,c='g',linestyle='dotted')
##################################

############# BH masses ##############
ax10.set_xscale('log')
ax10.set_yscale('log')
ax10.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax10.set_ylabel(r'$M_{\rm black-holes}\,[h^{-1}M_\odot]$',fontsize=18)

#X,Y,dY,N = np.loadtxt(f101, unpack=True)
#ax10.fill_between(X, Y+dY, Y-dY, color='blue')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f101, unpack=True)
ax10.fill_between(X, dYp, dYm, color='blue')
ax10.plot(X,Ym,c='k',linestyle='-')

#X,Y,dY,N = np.loadtxt(f102, unpack=True)
#ax10.fill_between(X, Y+dY, Y-dY, color='red', alpha=0.6)
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f102, unpack=True)
ax10.fill_between(X, dYp, dYm, color='red', alpha=0.6)
ax10.plot(X,Ym,c='k',linestyle='--')

X,Y,dY = np.loadtxt(f103, unpack=True)
#p3,=ax10.plot(X,Y,c='g',linestyle='-')

X,Y,dY = np.loadtxt(f104, unpack=True)
#p3,=ax10.plot(X,Y,c='g',linestyle='--')

X,Y,dY = np.loadtxt(f105, unpack=True)
#p3,=ax10.plot(X,Y,c='g',linestyle='dotted')
##################################

############# Vmax ##############
ax11.set_xscale('log')
ax11.set_yscale('log')
ax11.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax11.set_ylabel(r'$V_{\rm max}\,[{\rm km/s}]$',fontsize=18)

#X,Y,dY,N = np.loadtxt(f111, unpack=True)
#ax11.fill_between(X, Y+dY, Y-dY, color='blue')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f111, unpack=True)
ax11.fill_between(X, dYp, dYm, color='blue')
ax11.plot(X,Ym,c='k',linestyle='-')

#X,Y,dY,N = np.loadtxt(f112, unpack=True)
#ax11.fill_between(X, Y+dY, Y-dY, color='red', alpha=0.6)
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f112, unpack=True)
ax11.fill_between(X, dYp, dYm, color='red', alpha=0.6)
ax11.plot(X,Ym,c='k',linestyle='--')

X,Y,dY = np.loadtxt(f113, unpack=True)
#p3,=ax11.plot(X,Y,c='g',linestyle='-')

X,Y,dY = np.loadtxt(f114, unpack=True)
#p3,=ax11.plot(X,Y,c='g',linestyle='--')

X,Y,dY = np.loadtxt(f115, unpack=True)
#p3,=ax11.plot(X,Y,c='g',linestyle='dotted')
##################################

############# SFR ##############
ax12.set_xscale('log')
ax12.set_yscale('log')
ax12.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax12.set_ylabel(r'${\rm SFR}\,[M_\odot{\rm yr}^{-1}]$',fontsize=18)

#X,Y,dY,N = np.loadtxt(f121, unpack=True)
#ax12.fill_between(X, Y+dY, Y-dY, color='blue')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f121, unpack=True)
ax12.fill_between(X, dYp, dYm, color='blue')
ax12.plot(X,Ym,c='k',linestyle='-')

#X,Y,dY,N = np.loadtxt(f122, unpack=True)
#ax12.fill_between(X, Y+dY, Y-dY, color='red', alpha=0.6)
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f122, unpack=True)
ax12.fill_between(X, dYp, dYm, color='red', alpha=0.6)
ax12.plot(X,Ym,c='k',linestyle='--')

X,Y,dY = np.loadtxt(f123, unpack=True)
#p3,=ax12.plot(X,Y,c='g',linestyle='-')

X,Y,dY = np.loadtxt(f124, unpack=True)
#p3,=ax12.plot(X,Y,c='g',linestyle='--')

X,Y,dY = np.loadtxt(f125, unpack=True)
#p3,=ax12.plot(X,Y,c='g',linestyle='dotted')
##################################

#legend
ax1.legend([p1,p2],
           [r"${\rm IllustrisTNG}$",
            r"${\rm SIMBA}$"],
           loc=0,prop={'size':18},ncol=1,frameon=True)

#ax1.set_title(r'$\sum m_\nu=0.0\/{\rm eV}$',position=(0.5,1.02),size=18)
#title('About as simple as it gets, folks')
#suptitle('About as simple as it gets, folks')  #for title with several panels
#grid(True)
#show()
savefig(f_out, bbox_inches='tight')
close(fig)





