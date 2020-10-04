# This script plots the median from the CV sets and the 16-84 percentiles from LH
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
f_out = 'different_seed2.pdf'

# Pk m
f11 = '%s/Pk/IllustrisTNG/mean_LH_Pk_m_z=0.00.txt'%root
f12 = '%s/Pk/SIMBA/mean_LH_Pk_m_z=0.00.txt'%root
f13 = '%s/Pk/IllustrisTNG/mean_CV_Pk_m_z=0.00.txt'%root
f14 = '%s/Pk/SIMBA/mean_CV_Pk_m_z=0.00.txt'%root

# Pk g
f21 = '%s/Pk/IllustrisTNG/mean_LH_Pk_g_z=0.00.txt'%root
f22 = '%s/Pk/SIMBA/mean_LH_Pk_g_z=0.00.txt'%root
f23 = '%s/Pk/IllustrisTNG/mean_CV_Pk_g_z=0.00.txt'%root
f24 = '%s/Pk/SIMBA/mean_CV_Pk_g_z=0.00.txt'%root

# ratio Pk m
f31 = '%s/Pk_ratio/IllustrisTNG/mean_LH_Pk_ratio_m_z=0.00.txt'%root
f32 = '%s/Pk_ratio/SIMBA/mean_LH_Pk_ratio_m_z=0.00.txt'%root
f33 = '%s/Pk_ratio/IllustrisTNG/mean_CV_Pk_ratio_m_z=0.00.txt'%root
f34 = '%s/Pk_ratio/SIMBA/mean_CV_Pk_ratio_m_z=0.00.txt'%root

# HMF
f41 = '%s/HMF/IllustrisTNG/mean_LH_mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f42 = '%s/HMF/SIMBA/mean_LH_mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f43 = '%s/HMF/IllustrisTNG/mean_CV_mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f44 = '%s/HMF/SIMBA/mean_CV_mass_function_1.00e+10_1.00e+14_30_z=0.00.txt'%root

# SFRH
f51 = '%s/SFRH/IllustrisTNG/mean_LH_SFRH_0.00_10.00_10000.txt'%root
f52 = '%s/SFRH/SIMBA/mean_LH_SFRH_0.00_10.00_10000.txt'%root
f53 = '%s/SFRH/IllustrisTNG/mean_CV_SFRH_0.00_10.00_10000.txt'%root
f54 = '%s/SFRH/SIMBA/mean_CV_SFRH_0.00_10.00_10000.txt'%root

# SMF
f61 = '%s/SMF/IllustrisTNG/mean_LH_SMF_1.00e+09_5e+11_10_z=0.00.txt'%root
f62 = '%s/SMF/SIMBA/mean_LH_SMF_1.00e+09_5e+11_10_z=0.00.txt'%root
f63 = '%s/SMF/IllustrisTNG/mean_CV_SMF_1.00e+09_5e+11_10_z=0.00.txt'%root
f64 = '%s/SMF/SIMBA/mean_CV_SMF_1.00e+09_5e+11_10_z=0.00.txt'%root

# baryon fraction
f71 = '%s/baryon_fraction/IllustrisTNG/mean_LH_bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f72 = '%s/baryon_fraction/SIMBA/mean_LH_bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f73 = '%s/baryon_fraction/IllustrisTNG/mean_CV_bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root
f74 = '%s/baryon_fraction/SIMBA/mean_CV_bf_1.00e+10_1.00e+14_30_z=0.00.txt'%root

# halos temperature
f81 = '%s/SO/IllustrisTNG/mean_T_LH_1.00e+12_1.00e+14_10_z=0.00.txt'%root
f82 = '%s/SO/SIMBA/mean_T_LH_1.00e+12_1.00e+14_10_z=0.00.txt'%root
f83 = '%s/SO/IllustrisTNG/mean_T_CV_1.00e+12_1.00e+14_10_z=0.00.txt'%root
f84 = '%s/SO/SIMBA/mean_T_CV_1.00e+12_1.00e+14_10_z=0.00.txt'%root

# galaxies radius
f91 = '%s/Radii/IllustrisTNG/mean_R_vs_SM_LH_z=0.00.txt'%root
f92 = '%s/Radii/SIMBA/mean_R_vs_SM_LH_z=0.00.txt'%root
f93 = '%s/Radii/IllustrisTNG/mean_R_vs_SM_CV_z=0.00.txt'%root
f94 = '%s/Radii/SIMBA/mean_R_vs_SM_CV_z=0.00.txt'%root

# Black hole masses
f101 = '%s/BH/IllustrisTNG/mean_BH_vs_SM_LH_z=0.00.txt'%root
f102 = '%s/BH/SIMBA/mean_BH_vs_SM_LH_z=0.00.txt'%root
f103 = '%s/BH/IllustrisTNG/mean_BH_vs_SM_CV_z=0.00.txt'%root
f104 = '%s/BH/SIMBA/mean_BH_vs_SM_CV_z=0.00.txt'%root

# Vmax
f111 = '%s/Vmax/IllustrisTNG/mean_V_vs_SM_LH_z=0.00.txt'%root
f112 = '%s/Vmax/SIMBA/mean_V_vs_SM_LH_z=0.00.txt'%root
f113 = '%s/Vmax/IllustrisTNG/mean_V_vs_SM_CV_z=0.00.txt'%root
f114 = '%s/Vmax/SIMBA/mean_V_vs_SM_CV_z=0.00.txt'%root

# SFR
f121 = '%s/SFR/IllustrisTNG/mean_SFR_vs_SM_LH_z=0.00.txt'%root
f122 = '%s/SFR/SIMBA/mean_SFR_vs_SM_LH_z=0.00.txt'%root
f123 = '%s/SFR/IllustrisTNG/mean_SFR_vs_SM_CV_z=0.00.txt'%root
f124 = '%s/SFR/SIMBA/mean_SFR_vs_SM_CV_z=0.00.txt'%root
################################################################################

fig  = figure(figsize=(20/1.3,22/1.3)) 
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
subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.24, hspace=0.25)

c1='blue'
c2='red'

###### Pk m plot ######
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlim([0.3,35])
ax1.set_ylim([1e-1,1e3])
ax1.set_xlabel(r'$k\,[h{\rm Mpc}^{-1}]$',fontsize=18)
ax1.set_ylabel(r'$P_{\rm m}(k)\,[h^{-3}{\rm Mpc}^3]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f11, unpack=True)
ax1.fill_between(X, dYp, dYm, color=c1, alpha=0.6)
#p1,=ax1.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f12, unpack=True)
ax1.fill_between(X, dYp, dYm, color=c2, alpha=0.6)
#p2,=ax1.plot(X,Ym,c='k',linestyle='--')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f13, unpack=True)
p1,=ax1.plot(X,Ym,c=c1,linestyle='-')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f14, unpack=True)
p2,=ax1.plot(X,Ym,c=c2,linestyle='--')
#######################

###### Pk g plot ######
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlim([0.3,35])
ax2.set_ylim([1e-2,1e3])
ax2.set_xlabel(r'$k\,[h{\rm Mpc}^{-1}]$',fontsize=18)
ax2.set_ylabel(r'$P_{\rm g}(k)\,[h^{-3}{\rm Mpc}^3]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f21, unpack=True)
ax2.fill_between(X, dYp, dYm, color=c1, alpha=0.6)
#ax2.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f22, unpack=True)
ax2.fill_between(X, dYp, dYm, color=c2, alpha=0.6)
#ax2.plot(X,Ym,c='k',linestyle='--')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f23, unpack=True)
p1,=ax2.plot(X,Ym,c=c1,linestyle='-')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f24, unpack=True)
p2,=ax2.plot(X,Ym,c=c2,linestyle='--')
#######################

###### ratio Pk m plot ######
ax3.set_xscale('log')
ax3.set_xlim([0.3,35])
ax3.set_ylim([0.5,1.05])
ax3.set_xlabel(r'$k\,[h{\rm Mpc}^{-1}]$',fontsize=18)
ax3.set_ylabel(r'$P_{\rm hydro}(k)/P_{\rm Nbody}(k)$',fontsize=18)

X,Y,dY,dYp,dYm,Ym= np.loadtxt(f31, unpack=True)
ax3.fill_between(X, dYp, dYm, color=c1, alpha=0.6)
#ax3.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f32, unpack=True)
ax3.fill_between(X, dYp, dYm, color=c2, alpha=0.6)
#ax3.plot(X,Ym,c='k',linestyle='--')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f33, unpack=True)
p1,=ax3.plot(X,Ym,c=c1,linestyle='-')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f34, unpack=True)
p2,=ax3.plot(X,Ym,c=c2,linestyle='--')
#######################

######### HMF #########
ax4.set_xscale('log')
ax4.set_yscale('log')
ax4.set_xlabel(r'$M_{\rm halo}/\Omega_{\rm m}\,[h^{-1}M_\odot]$',fontsize=18)
ax4.set_ylabel(r'${\rm HMF}\,[h^{4}{\rm Mpc}^{-3}M_\odot^{-1}]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f41, unpack=True)
ax4.fill_between(X, dYp, dYm, color=c1, alpha=0.6)
#ax4.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f42, unpack=True)
ax4.fill_between(X, dYp, dYm, color=c2, alpha=0.6)
#ax4.plot(X,Ym,c='k',linestyle='--')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f43, unpack=True)
p1,=ax4.plot(X,Ym,c=c1,linestyle='-')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f44, unpack=True)
p2,=ax4.plot(X,Ym,c=c2,linestyle='--')
#######################

###### SFRH ######
ax5.set_yscale('log')
ax5.set_xlim([0.0,7.0])
ax5.set_ylim([5e-4,0.2])
ax5.set_xlabel(r'$z$',fontsize=18)
ax5.set_ylabel(r'${\rm SFRD}\,[M_\odot{\rm yr}^{-1}{\rm Mpc}^{-3}]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f51, unpack=True)
ax5.fill_between(X, dYp, dYm, color=c1, alpha=0.6)
#ax5.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f52, unpack=True)
ax5.fill_between(X, dYp, dYm, color=c2, alpha=0.6)
#ax5.plot(X,Ym,c='k',linestyle='--')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f53, unpack=True)
p1,=ax5.plot(X,Ym,c=c1,linestyle='-')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f54, unpack=True)
p2,=ax5.plot(X,Ym,c=c2,linestyle='--')
#######################

###### SMF ######
ax6.set_xscale('log')
ax6.set_yscale('log')
ax6.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax6.set_ylabel(r'${\rm SMF}\,[h^4{\rm Mpc}^{-3}M_\odot^{-1}]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f61, unpack=True)
ax6.fill_between(X, dYp, dYm, color=c1, alpha=0.6)
#ax6.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f62, unpack=True)
ax6.fill_between(X, dYp, dYm, color=c2, alpha=0.6)
#ax6.plot(X,Ym,c='k',linestyle='--')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f63, unpack=True)
p1,=ax6.plot(X,Ym,c=c1,linestyle='-')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f64, unpack=True)
p2,=ax6.plot(X,Ym,c=c2,linestyle='--')
#######################

###### baryon fraction ######
ax7.set_xscale('log')
ax7.set_xlabel(r'$M_{\rm halo}/\Omega_{\rm m}\,[h^{-1}M_\odot]$',fontsize=18)
ax7.set_ylabel(r'$M_{\rm b}/M_{\rm halo}/(\Omega_{\rm b}/\Omega_{\rm m})$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f71, unpack=True)
ax7.fill_between(X, dYp, dYm, color=c1, alpha=0.6)
#ax7.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f72, unpack=True)
ax7.fill_between(X, dYp, dYm, color=c2, alpha=0.6)
#ax7.plot(X,Ym,c='k',linestyle='--')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f73, unpack=True)
p1,=ax7.plot(X,Ym,c=c1,linestyle='-')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f74, unpack=True)
p2,=ax7.plot(X,Ym,c=c2,linestyle='--')
#######################

######## halos temperature #######
ax8.set_xscale('log')
ax8.set_yscale('log')
ax8.set_xlabel(r'$M_{\rm halo}\,[h^{-1}M_\odot]$',fontsize=18)
ax8.set_ylabel(r'$T_{\rm halo}\,[K]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f81, unpack=True)
ax8.fill_between(X, dYp, dYm, color=c1, alpha=0.6)
#ax8.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f82, unpack=True)
ax8.fill_between(X, dYp, dYm, color=c2, alpha=0.6)
#ax8.plot(X,Ym,c='k',linestyle='--')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f83, unpack=True)
p1,=ax8.plot(X,Ym,c=c1,linestyle='-')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f84, unpack=True)
p2,=ax8.plot(X,Ym,c=c2,linestyle='--')
##################################

############# Radii ##############
ax9.set_xscale('log')
ax9.set_yscale('log')
ax9.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax9.set_ylabel(r'$R_{1/2}\,[h^{-1}{\rm kpc}]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f91, unpack=True)
ax9.fill_between(X, dYp, dYm, color=c1, alpha=0.6)
#ax9.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f92, unpack=True)
ax9.fill_between(X, dYp, dYm, color=c2, alpha=0.6)
#ax9.plot(X,Ym,c='k',linestyle='--')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f93, unpack=True)
p1,=ax9.plot(X,Ym,c=c1,linestyle='-')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f94, unpack=True)
p2,=ax9.plot(X,Ym,c=c2,linestyle='--')
##################################

############# BH masses ##############
ax10.set_xscale('log')
ax10.set_yscale('log')
ax10.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax10.set_ylabel(r'$M_{\rm BH}\,[h^{-1}M_\odot]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f101, unpack=True)
ax10.fill_between(X, dYp, dYm, color=c1, alpha=0.6)
#ax10.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f102, unpack=True)
ax10.fill_between(X, dYp, dYm, color=c2, alpha=0.6)
#ax10.plot(X,Ym,c='k',linestyle='--')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f103, unpack=True)
p1,=ax10.plot(X,Ym,c=c1,linestyle='-')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f104, unpack=True)
p2,=ax10.plot(X,Ym,c=c2,linestyle='--')
##################################

############# Vmax ##############
ax11.set_xscale('log')
#ax11.set_yscale('log')
ax11.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax11.set_ylabel(r'${\rm max}(\sqrt{GM/R})\,[{\rm km/s}]$',fontsize=18)

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f111, unpack=True)
ax11.fill_between(X, dYp, dYm, color=c1, alpha=0.6)
#ax11.plot(X,Ym,c='k',linestyle='-')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f112, unpack=True)
ax11.fill_between(X, dYp, dYm, color=c2, alpha=0.6)
#ax11.plot(X,Ym,c='k',linestyle='--')

X,Y,dY,dYp,dYm,Ym = np.loadtxt(f113, unpack=True)
p1,=ax11.plot(X,Ym,c=c1,linestyle='-')
X,Y,dY,dYp,dYm,Ym = np.loadtxt(f114, unpack=True)
p2,=ax11.plot(X,Ym,c=c2,linestyle='--')
##################################

############# SFR ##############
ax12.set_xscale('log')
ax12.set_yscale('log')
ax12.set_xlabel(r'$M_*\,[h^{-1}M_\odot]$',fontsize=18)
ax12.set_ylabel(r'${\rm SFR}\,[M_\odot{\rm yr}^{-1}]$',fontsize=18)

#X,Y,dY,dYp,dYm,Ym = np.loadtxt(f121, unpack=True)
X, Y,dY,dYp,dYm,Ym, Y2,dY2,dY2p,dY2m,Y2m = np.loadtxt(f121, unpack=True)
ax12.fill_between(X, dY2p, dY2m, color=c1, alpha=0.6)
#ax12.plot(X,Ym,c='k',linestyle='-')

#X,Y,dY,dYp,dYm,Ym = np.loadtxt(f122, unpack=True)
X, Y,dY,dYp,dYm,Ym, Y2,dY2,dY2p,dY2m,Y2m = np.loadtxt(f122, unpack=True)
ax12.fill_between(X, dY2p, dY2m, color=c2, alpha=0.6)
#ax12.plot(X,Ym,c='k',linestyle='--')

#X,Y,dY,dYp,dYm,Ym = np.loadtxt(f123, unpack=True)
X, Y,dY,dYp,dYm,Ym, Y2,dY2,dY2p,dY2m,Y2m = np.loadtxt(f123, unpack=True)
p1,=ax12.plot(X,Y2m,c=c1,linestyle='-')
#X,Y,dY,dYp,dYm,Ym = np.loadtxt(f124, unpack=True)
X, Y,dY,dYp,dYm,Ym, Y2,dY2,dY2p,dY2m,Y2m = np.loadtxt(f124, unpack=True)
p2,=ax12.plot(X,Y2m,c=c2,linestyle='--')
##################################

ax1.text(0.05,0.05, r"$I$",    fontsize=22, color='k',transform=ax1.transAxes)
ax2.text(0.05,0.05, r"$II$",   fontsize=22, color='k',transform=ax2.transAxes)
ax3.text(0.05,0.05, r"$III$",  fontsize=22, color='k',transform=ax3.transAxes)
ax4.text(0.05,0.05, r"$IV$",   fontsize=22, color='k',transform=ax4.transAxes)
ax5.text(0.05,0.05, r"$V$",    fontsize=22, color='k',transform=ax5.transAxes)
ax6.text(0.05,0.05, r"$VI$",   fontsize=22, color='k',transform=ax6.transAxes)
ax7.text(0.05,0.9,  r"$VII$",  fontsize=22, color='k',transform=ax7.transAxes)
ax8.text(0.05,0.9,  r"$VIII$", fontsize=22, color='k',transform=ax8.transAxes)
ax9.text(0.05,0.9,  r"$IX$",   fontsize=22, color='k',transform=ax9.transAxes)
ax10.text(0.05,0.9, r"$X$",    fontsize=22, color='k',transform=ax10.transAxes)
ax11.text(0.05,0.9, r"$XI$",   fontsize=22, color='k',transform=ax11.transAxes)
ax12.text(0.05,0.9, r"$XII$",  fontsize=22, color='k',transform=ax12.transAxes)

#legend
ax1.legend([p1,p2],
           [r"${\rm IllustrisTNG}$",
            r"${\rm SIMBA}$"],
           loc=8,prop={'size':16},ncol=1,frameon=True)

#ax1.set_title(r'$\sum m_\nu=0.0\/{\rm eV}$',position=(0.5,1.02),size=18)
#title('About as simple as it gets, folks')
#suptitle('About as simple as it gets, folks')  #for title with several panels
#grid(True)
#show()
savefig(f_out, bbox_inches='tight')
close(fig)





