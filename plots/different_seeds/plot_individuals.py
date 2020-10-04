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
f_out = 'test_SIMBA.pdf'

linestyles = ['-', '--', '-.', ':']

# Pk m
f1 = ['%s/Pk/SIMBA/0/Pk_m_z=0.00.txt'%root,
      '%s/Pk/SIMBA/0_clean0/Pk_m_z=0.00.txt'%root,
      '%s/Pk/SIMBA/0_clean1/Pk_m_z=0.00.txt'%root,
      '%s/Pk/SIMBA/0_test/Pk_m_z=0.00.txt'%root]

# ratio Pk m
f2 = ['%s/Pk_ratio/SIMBA/0/Pk_ratio_m_z=0.00.txt'%root,
      '%s/Pk_ratio/SIMBA/0_clean0/Pk_ratio_m_z=0.00.txt'%root,
      '%s/Pk_ratio/SIMBA/0_clean1/Pk_ratio_m_z=0.00.txt'%root,
      '%s/Pk_ratio/SIMBA/0_test/Pk_ratio_m_z=0.00.txt'%root]

# Pk g
f3 = ['%s/Pk/SIMBA/0/Pk_g_z=0.00.txt'%root,
      '%s/Pk/SIMBA/0_clean0/Pk_g_z=0.00.txt'%root,
      '%s/Pk/SIMBA/0_clean1/Pk_g_z=0.00.txt'%root,
      '%s/Pk/SIMBA/0_test/Pk_g_z=0.00.txt'%root]

# HMF
f4 = ['%s/HMF/SIMBA/0/mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root,
      '%s/HMF/SIMBA/0_clean0/mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root,
      '%s/HMF/SIMBA/0_clean1/mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root,
      '%s/HMF/SIMBA/0_test/mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root]

# SFRH
f5 = ['%s/SFRH/SIMBA/0/SFRH_0.00_6.00_10000.txt'%root,
      '%s/SFRH/SIMBA/0_clean0/SFRH_0.00_6.00_10000.txt'%root,
      '%s/SFRH/SIMBA/0_clean1/SFRH_0.00_6.00_10000.txt'%root,
      '%s/SFRH/SIMBA/0_test/SFRH_0.00_6.00_10000.txt'%root]
      
# SMF
f6 = ['%s/SMF/SIMBA/0/SMF_1.00e+09_5e+11_10_z=0.00.txt'%root,
      '%s/SMF/SIMBA/0_clean0/SMF_1.00e+09_5e+11_10_z=0.00.txt'%root,
      '%s/SMF/SIMBA/0_clean1/SMF_1.00e+09_5e+11_10_z=0.00.txt'%root,
      '%s/SMF/SIMBA/0_test/SMF_1.00e+09_5e+11_10_z=0.00.txt'%root]

# baryon fraction
f7 = ['%s/baryon_fraction/SIMBA/0/bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root,
      '%s/baryon_fraction/SIMBA/0_clean0/bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root,
      '%s/baryon_fraction/SIMBA/0_clean1/bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root,
      '%s/baryon_fraction/SIMBA/0_test/bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root]

# halos temperature
f8 = ['%s/SO/SIMBA/0/SO_z=0.00.txt'%root,
      '%s/SO/SIMBA/0_clean0/SO_z=0.00.txt'%root,
      '%s/SO/SIMBA/0_clean1/SO_z=0.00.txt'%root,
      '%s/SO/SIMBA/0_test/SO_z=0.00.txt'%root]

# Radii
f9 = ['%s/Radii/SIMBA/0/R_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
      '%s/Radii/SIMBA/0_clean0/R_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
      '%s/Radii/SIMBA/0_clean1/R_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
      '%s/Radii/SIMBA/0_test/R_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root]

# BH masses
f10 = ['%s/BH/SIMBA/0/BH_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
       '%s/BH/SIMBA/0_clean0/BH_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
       '%s/BH/SIMBA/0_clean1/BH_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
       '%s/BH/SIMBA/0_test/BH_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root]

# Vmax
f11 = ['%s/Vmax/SIMBA/0/Vmax_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
       '%s/Vmax/SIMBA/0_clean0/Vmax_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
       '%s/Vmax/SIMBA/0_clean1/Vmax_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
       '%s/Vmax/SIMBA/0_test/Vmax_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root]

# SFR
f12 = ['%s/SFR/SIMBA/0/SFR_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
       '%s/SFR/SIMBA/0_clean0/SFR_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
       '%s/SFR/SIMBA/0_clean1/SFR_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root,
       '%s/SFR/SIMBA/0_test/SFR_vs_SM_1.00e+09_5e+11_10_z=0.00.txt'%root]
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

for f,ls in zip(f1,linestyles):
    X,Y = np.loadtxt(f, unpack=True)
    ax1.plot(X,Y,c='k',linestyle=ls)
#######################

###### ratio Pk m plot ######
ax2.set_xscale('log')
ax2.set_xlim([0.3,35])
ax2.set_ylim([0.5,1.05])
ax2.set_xlabel(r'$k\,[h{\rm Mpc}^{-1}]$',fontsize=18)
ax2.set_ylabel(r'$P_{\rm hydro}(k)/P_{\rm Nbody}(k)$',fontsize=18)

for f,ls in zip(f2,linestyles):
    X,Y = np.loadtxt(f, unpack=True)
    ax2.plot(X,Y,c='k',linestyle=ls)
#######################

###### Pk g plot ######
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.set_xlim([0.3,35])
ax3.set_ylim([1e-2,1e3])
ax3.set_xlabel(r'$k\,[h{\rm Mpc}^{-1}]$',fontsize=18)
ax3.set_ylabel(r'$P_{\rm g}(k)\,[h^{-3}{\rm Mpc}^3]$',fontsize=18)

for f,ls in zip(f3,linestyles):
    X,Y = np.loadtxt(f, unpack=True)
    ax3.plot(X,Y,c='k',linestyle=ls)
#######################

######### HMF #########
ax4.set_xscale('log')
ax4.set_yscale('log')
ax4.set_xlabel(r'$M_{\rm halo}/\Omega_{\rm m}\,[h^{-1}M_\odot]$',fontsize=18)
ax4.set_ylabel(r'${\rm HMF}\,[h^{4}{\rm Mpc}^{-3}M_\odot^{-1}]$',fontsize=18)

for f,ls in zip(f4,linestyles):
    A,X,Y = np.loadtxt(f, unpack=True)
    ax4.plot(X,Y,c='k',linestyle=ls)
#######################

###### SFRH ######
ax5.set_yscale('log')
ax5.set_xlim([0.0,6.0])
ax5.set_ylim([1e-3,1e0])
ax5.set_xlabel(r'$z$',fontsize=18)
ax5.set_ylabel(r'${\rm SFRH}\,[M_\odot{\rm yr}^{-1}{\rm Mpc}^{-3}]$',fontsize=18)

for f,ls in zip(f5,linestyles):
    X,Y = np.loadtxt(f, unpack=True)
    ax5.plot(X,Y,c='k',linestyle=ls)
#######################

###### SMF ######
ax6.set_xscale('log')
ax6.set_yscale('log')
ax6.set_xlabel(r'$z$',fontsize=18)
ax6.set_ylabel(r'${\rm SMF}\,[h^4{\rm Mpc}^{-3}M_\odot^{-1}]$',fontsize=18)

for f,ls in zip(f6,linestyles):
    X,Y = np.loadtxt(f, unpack=True)
    ax6.plot(X,Y,c='k',linestyle=ls)
#######################

###### baryon fraction ######
ax7.set_xscale('log')
ax7.set_xlabel(r'$M_{\rm halo}/\Omega_{\rm m}\,[h^{-1}M_\odot]$',fontsize=18)
ax7.set_ylabel(r'$M_{\rm b}/M_{\rm halo}/(\Omega_{\rm b}/\Omega_{\rm m})$',fontsize=18)

for f,ls in zip(f7,linestyles):
    X,Y = np.loadtxt(f, unpack=True)
    ax7.plot(X,Y,c='k',linestyle=ls)
#######################

###### temperature ######
ax8.set_xscale('log')
ax8.set_yscale('log')
ax8.set_xlabel(r'$M_{\rm halo}/\Omega_{\rm m}\,[h^{-1}M_\odot]$',fontsize=18)
ax8.set_ylabel(r'$T_{\rm halo}\,[K]$',fontsize=18)

for f,ls in zip(f8,linestyles):
    data = np.loadtxt(f)
    #ax8.plot(data[:,0],data[:,9],c='k',linestyle=ls)
#########################

######## Radii ##########
ax9.set_xscale('log')
ax9.set_yscale('log')
ax9.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax9.set_ylabel(r'$R_{1/2}\,[h^{-1}{\rm kpc}]$',fontsize=18)

for f,ls in zip(f9,linestyles):
    X,Y,N = np.loadtxt(f, unpack=True)
    ax9.plot(X,Y,c='k',linestyle=ls)
#########################

####### BH masses #######
ax10.set_xscale('log')
ax10.set_yscale('log')
ax10.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax10.set_ylabel(r'$M_{\rm black-holes}\,[h^{-1}M_\odot]$',fontsize=18)

for f,ls in zip(f10,linestyles):
    X,Y,N = np.loadtxt(f, unpack=True)
    ax10.plot(X,Y,c='k',linestyle=ls)
#########################

######### Vmax ##########
ax11.set_xscale('log')
ax11.set_yscale('log')
ax11.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax11.set_ylabel(r'$V_{\rm max}\,[{\rm km/s}]$',fontsize=18)

for f,ls in zip(f11,linestyles):
    X,Y,N = np.loadtxt(f, unpack=True)
    ax11.plot(X,Y,c='k',linestyle=ls)
#########################

########## SFR ##########
ax12.set_xscale('log')
ax12.set_yscale('log')
ax12.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax12.set_ylabel(r'${\rm SFR}\,[M_\odot{\rm yr}^{-1}]$',fontsize=18)

for f,ls in zip(f12,linestyles):
    X,Y,N = np.loadtxt(f, unpack=True)
    ax12.plot(X,Y,c='k',linestyle=ls)
#########################

#ax1.set_title(r'$\sum m_\nu=0.0\/{\rm eV}$',position=(0.5,1.02),size=18)
#title('About as simple as it gets, folks')
#suptitle('About as simple as it gets, folks')  #for title with several panels
#grid(True)
#show()
savefig(f_out, bbox_inches='tight')
close(fig)









