from pylab import *
import numpy as np
from matplotlib.ticker import ScalarFormatter
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from matplotlib.ticker import AutoMinorLocator
from matplotlib.colors import LogNorm
from matplotlib.patches import Ellipse
rcParams["mathtext.fontset"]='cm'

############################### figure ###########################
#fig=figure(figsize=(15,10))     #give dimensions to the figure
##################################################################

################################ INPUT #######################################
#axes range
##############################################################################

############################ subplots ############################
#gs = gridspec.GridSpec(2,1,height_ratios=[5,2])
#ax1=plt.subplot(gs[0])
#ax2=plt.subplot(gs[1])

#make a subplot at a given position and with some given dimensions
#ax2=axes([0.4,0.55,0.25,0.1])

#gs.update(hspace=0.0,wspace=0.4,bottom=0.6,top=1.05)
#subplots_adjust(left=None, bottom=None, right=None, top=None,
#                wspace=0.5, hspace=0.5)

#set minor ticks
#ax1.xaxis.set_minor_locator(AutoMinorLocator(4))
#ax1.yaxis.set_minor_locator(AutoMinorLocator(4))


#ax1.xaxis.set_major_formatter( NullFormatter() )   #unset x label 
#ax1.yaxis.set_major_formatter( NullFormatter() )   #unset y label

# custom xticks 
#ax1.set_xticks([0.25, 0.5, 1.0])
#ax1.set_yticks([0.25, 0.5, 1.0])
#ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter()) #for log 


#ax1.get_yaxis().set_label_coords(-0.2,0.5)  #align y-axis for multiple plots
##################################################################

##################### special behaviour stuff ####################
#to show error missing error bars in log scale
#ax1.set_yscale('log',nonposy='clip')  #set log scale for the y-axis

#set the x-axis in %f format instead of %e
#ax1.xaxis.set_major_formatter(ScalarFormatter()) 

#set size of ticks
#ax1.tick_params(axis='both', which='major', labelsize=10)
#ax1.tick_params(axis='both', which='minor', labelsize=8)

#set the position of the ylabel 
#ax1.yaxis.set_label_coords(-0.2, 0.4)

#set yticks in scientific notation
#ax1.ticklabel_format(axis='y',style='sci',scilimits=(1,4))

#set the x-axis in %f format instead of %e
#formatter = matplotlib.ticker.FormatStrFormatter('$%.2e$') 
#ax1.yaxis.set_major_formatter(formatter) 

#add two legends in the same plot
#ax5 = ax1.twinx()
#ax5.yaxis.set_major_formatter( NullFormatter() )   #unset y label 
#ax5.legend([p1,p2],['0.0 eV','0.3 eV'],loc=3,prop={'size':14},ncol=1)

#set points to show in the yaxis
#ax1.set_yticks([0,1,2])

#highlight a zoomed region
#mark_inset(ax1, ax2, loc1=2, loc2=4, fc="none",edgecolor='purple')
##################################################################

############################ plot type ###########################
#standard plot
#p1,=ax1.plot(x,y,linestyle='-',marker='None')

#error bar plot with the minimum and maximum values of the error bar interval
#p1=ax1.errorbar(r,xi,yerr=[delta_xi_min,delta_xi_max],lw=1,fmt='o',ms=2,
#               elinewidth=1,capsize=5,linestyle='-') 

#filled area
#p1=ax1.fill_between([x_min,x_max],[1.02,1.02],[0.98,0.98],color='k',alpha=0.2)

#hatch area
#ax1.fill([x_min,x_min,x_max,x_max],[y_min,3.0,3.0,y_min],#color='k',
#         hatch='X',fill=False,alpha=0.5)

#scatter plot
#p1=ax1.scatter(k1,Pk1,c='b',edgecolor='none',s=8,marker='*')

#plot with markers
#pl4,=ax1.plot(ke3,Pk3/Pke3,marker='.',markevery=2,c='r',linestyle='None')

#set size of dashed lines
#ax.plot([0, 1], [0, 1], linestyle='--', dashes=(5, 1)) #length of 5, space of 1

#image plot
#cax = ax1.imshow(densities,cmap=get_cmap('jet'),origin='lower',
#           extent=[x_min, x_max, y_min, y_max],
#           #vmin=min_density,vmax=max_density)
#           norm = LogNorm(vmin=min_density,vmax=max_density))
#cbar = fig.colorbar(cax, ax2, ax=ax1, ticks=[-1, 0, 1]) #in ax2 colorbar of ax1
#cbar.set_label(r"$M_{\rm CSF}\/[h^{-1}M_\odot]$",fontsize=14,labelpad=-50)
#cbar.ax.tick_params(labelsize=10)  #to change size of ticks

#make a polygon
#polygon = Rectangle((0.4,50.0), 20.0, 20.0, edgecolor='purple',lw=0.5,
#                    fill=False)
#ax1.add_artist(polygon)
####################################################################

x_min, x_max = 0.0, 25.0
y_min, y_max = 0.0, 25.0


fig  = figure(figsize=(7,12))     #give dimensions to the figure
gs   = gridspec.GridSpec(9,4)
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
ax13 = plt.subplot(gs[12])
ax14 = plt.subplot(gs[13])
ax15 = plt.subplot(gs[14])
ax16 = plt.subplot(gs[15])
ax17 = plt.subplot(gs[16])
ax18 = plt.subplot(gs[17])
ax19 = plt.subplot(gs[18])
ax20 = plt.subplot(gs[19])
ax21 = plt.subplot(gs[20])
ax22 = plt.subplot(gs[21])
ax23 = plt.subplot(gs[22])
ax24 = plt.subplot(gs[23])
ax25 = plt.subplot(gs[24])
ax26 = plt.subplot(gs[25])
ax27 = plt.subplot(gs[26])
ax28 = plt.subplot(gs[27])
ax29 = plt.subplot(gs[28])
ax30 = plt.subplot(gs[29])
ax31 = plt.subplot(gs[30])
ax32 = plt.subplot(gs[31])
ax33 = plt.subplot(gs[32])
ax34 = plt.subplot(gs[33])
ax35 = plt.subplot(gs[34])
ax36 = plt.subplot(gs[35])

gs.update(hspace=0.07,wspace=0.05,bottom=0.0,top=1.00)

for ax in [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12,ax13,ax14,ax15,
           ax16,ax17,ax18,ax19,ax20,ax21,ax22,ax23,ax24,ax25,ax26,ax27,ax28,
           ax29,ax30,ax31,ax32,ax33,ax34,ax35,ax36]:
    ax.tick_params(
        axis='both',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        left=False,
        right=False,
        labelleft=False,
        labelbottom=False) # labels along the bottom edge are off

#ax1.set_xscale('log')
#ax1.set_yscale('log')

#ax1.set_xlim([x_min,x_max])
#ax1.set_ylim([y_min,y_max])

#ax1.set_xlabel(r'$k\/[h\/{\rm Mpc}^{-1}]$',fontsize=18)
#ax1.set_ylabel(r'$P(k)\,[(h^{-1}{\rm Mpc})^3]$',fontsize=18)


root  = '/mnt/ceph/users/camels/Results/images_EX'
f_out = 'images_EX.pdf'
i     = 7 #map index

f1 = '%s/Images_EX_fiducial_T.npy'%root
f2 = '%s/Images_EX_AGN_T.npy'%root
f3 = '%s/Images_EX_SN_T.npy'%root
f4 = '%s/Images_EX_noFB_T.npy'%root
T1, T2, T3, T4 = np.load(f1), np.load(f2), np.load(f3), np.load(f4) 

f1 = '%s/Images_EX_fiducial_Z.npy'%root
f2 = '%s/Images_EX_AGN_Z.npy'%root
f3 = '%s/Images_EX_SN_Z.npy'%root
f4 = '%s/Images_EX_noFB_Z.npy'%root
Z1, Z2, Z3, Z4 = np.load(f1), np.load(f2), np.load(f3), np.load(f4) 
Zsun = 0.02;  Z1 = Z1/Zsun;  Z2 = Z2/Zsun;  Z3 = Z3/Zsun;  Z4 = Z4/Zsun

f1 = '%s/Images_EX_fiducial_Mgas.npy'%root
f2 = '%s/Images_EX_AGN_Mgas.npy'%root
f3 = '%s/Images_EX_SN_Mgas.npy'%root
f4 = '%s/Images_EX_noFB_Mgas.npy'%root
Mg1, Mg2, Mg3, Mg4 = np.load(f1), np.load(f2), np.load(f3), np.load(f4) 

f1 = '%s/Images_EX_fiducial_Mcdm.npy'%root
f2 = '%s/Images_EX_AGN_Mcdm.npy'%root
f3 = '%s/Images_EX_SN_Mcdm.npy'%root
f4 = '%s/Images_EX_noFB_Mcdm.npy'%root
Mc1, Mc2, Mc3, Mc4 = np.load(f1), np.load(f2), np.load(f3), np.load(f4) 

f1 = '%s/Images_EX_fiducial_Mstar.npy'%root
f2 = '%s/Images_EX_AGN_Mstar.npy'%root
f3 = '%s/Images_EX_SN_Mstar.npy'%root
f4 = '%s/Images_EX_noFB_Mstar.npy'%root
Ms1, Ms2, Ms3, Ms4 = np.load(f1), np.load(f2), np.load(f3), np.load(f4) 

f1 = '%s/Images_EX_fiducial_Vgas.npy'%root
f2 = '%s/Images_EX_AGN_Vgas.npy'%root
f3 = '%s/Images_EX_SN_Vgas.npy'%root
f4 = '%s/Images_EX_noFB_Vgas.npy'%root
Vg1, Vg2, Vg3, Vg4 = np.load(f1), np.load(f2), np.load(f3), np.load(f4) 

f1 = '%s/Images_EX_fiducial_HI.npy'%root
f2 = '%s/Images_EX_AGN_HI.npy'%root
f3 = '%s/Images_EX_SN_HI.npy'%root
f4 = '%s/Images_EX_noFB_HI.npy'%root
HI1, HI2, HI3, HI4 = np.load(f1), np.load(f2), np.load(f3), np.load(f4) 

f1 = '%s/Images_EX_fiducial_ne.npy'%root
f2 = '%s/Images_EX_AGN_ne.npy'%root
f3 = '%s/Images_EX_SN_ne.npy'%root
f4 = '%s/Images_EX_noFB_ne.npy'%root
ne1, ne2, ne3, ne4 = np.load(f1), np.load(f2), np.load(f3), np.load(f4) 
ne1 *= 1e20;  ne2 *= 1e20;  ne3 *= 1e20;  ne4 *= 1e20

f1 = '%s/Images_EX_fiducial_P.npy'%root
f2 = '%s/Images_EX_AGN_P.npy'%root
f3 = '%s/Images_EX_SN_P.npy'%root
f4 = '%s/Images_EX_noFB_P.npy'%root
P1, P2, P3, P4 = np.load(f1), np.load(f2), np.load(f3), np.load(f4) 

min_T, max_T   = 2e3, 2e7
min_Z, max_Z   = 7e-10/Zsun, 7e-2/Zsun
min_Mg, max_Mg = 2e9, 1e14
min_Mc, max_Mc = 5e9, 1e15
min_Ms, max_Ms = 2e8, 1e15
min_Vg, max_Vg = 50.0, 500
min_HI, max_HI = 1e4, 1e14
min_ne, max_ne = 1e25, 1e33
min_P,  max_P  = 1e0, 1e11

Ms1[np.where(Ms1<min_Ms)] = min_Ms
Ms2[np.where(Ms2<min_Ms)] = min_Ms
Ms3[np.where(Ms3<min_Ms)] = min_Ms
Ms4[np.where(Ms4<min_Ms)] = min_Ms

dy = 0.112

for ax,T in zip([ax1,ax2,ax3,ax4],[T1[i], T2[i], T3[i], T4[i]]):
    cax = ax.imshow(T,cmap=get_cmap('hot'),origin='lower',
                    interpolation='bicubic', extent=[x_min, x_max, y_min, y_max],
                    norm = LogNorm(vmin=min_T,vmax=max_T))

axa = axes([0.91, 0.896, 0.015, 0.105])
cbar = fig.colorbar(cax, axa, ax=ax4) #in ax2 colorbar of ax1
cbar.set_label(r"$T_{\rm g}\,[K]$",fontsize=14,labelpad=5)
cbar.ax.tick_params(labelsize=8)  #to change size of ticks

for ax,Z in zip([ax5,ax6,ax7,ax8],[Z1[i], Z2[i], Z3[i], Z4[i]]):
    cax = ax.imshow(Z,cmap=get_cmap('cubehelix'),origin='lower',
                    interpolation='bicubic', extent=[x_min, x_max, y_min, y_max],
                    norm = LogNorm(vmin=min_Z,vmax=max_Z))

axa = axes([0.91, 0.896-dy, 0.015, 0.105])
cbar = fig.colorbar(cax, axa, ax=ax8) #in ax2 colorbar of ax1
cbar.set_label(r"$Z/Z_\odot$",fontsize=14,labelpad=5)
cbar.ax.tick_params(labelsize=8)  #to change size of ticks

for ax,Mg in zip([ax9,ax10,ax11,ax12],[Mg1[i], Mg2[i], Mg3[i], Mg4[i]]):
    cax = ax.imshow(Mg,cmap=get_cmap('jet'),origin='lower',
                    interpolation='bicubic', extent=[x_min, x_max, y_min, y_max],
                    norm = LogNorm(vmin=min_Mg,vmax=max_Mg))

axa = axes([0.91, 0.896-2*dy, 0.015, 0.105])
cbar = fig.colorbar(cax, axa, ax=ax12) #in ax2 colorbar of ax1
cbar.set_label(r"$\Sigma_{\rm g}\,[hM_\odot{\rm Mpc}^{-2}]$",fontsize=12,labelpad=5)
cbar.ax.tick_params(labelsize=8)  #to change size of ticks

for ax,Ms in zip([ax13,ax14,ax15,ax16],[Ms1[i], Ms2[i], Ms3[i], Ms4[i]]):
    cax = ax.imshow(Ms,cmap=get_cmap('nipy_spectral'),origin='lower',
                    interpolation='bicubic', extent=[x_min, x_max, y_min, y_max],
                    norm = LogNorm(vmin=min_Ms, vmax=max_Ms))

axa = axes([0.91, 0.896-3*dy, 0.015, 0.105])
cbar = fig.colorbar(cax, axa, ax=ax12) #in ax2 colorbar of ax1
cbar.set_label(r"$\Sigma_{\rm *}\,[hM_\odot{\rm Mpc}^{-2}]$",fontsize=12,labelpad=5)
cbar.ax.tick_params(labelsize=8)  #to change size of ticks

for ax,Vg in zip([ax17,ax18,ax19,ax20],[Vg1[i], Vg2[i], Vg3[i], Vg4[i]]):
    cax = ax.imshow(Vg,cmap=get_cmap('rainbow'),origin='lower',
                    interpolation='bicubic', extent=[x_min, x_max, y_min, y_max],
                    vmin=min_Vg, vmax=max_Vg)
                    #norm = LogNorm(vmin=min_Vg, vmax=max_Vg))

axa = axes([0.91, 0.896-4*dy, 0.015, 0.105])
cbar = fig.colorbar(cax, axa, ax=ax12) #in ax2 colorbar of ax1
cbar.set_label(r"$|\vec{V}_{\rm g}|\,[{\rm km/s}]$",fontsize=14,labelpad=5)
cbar.ax.tick_params(labelsize=8)  #to change size of ticks

for ax,HI in zip([ax21,ax22,ax23,ax24],[HI1[i], HI2[i], HI3[i], HI4[i]]):
    cax = ax.imshow(HI,cmap=get_cmap('magma'),origin='lower',
                    interpolation='bicubic', extent=[x_min, x_max, y_min, y_max],
                    norm = LogNorm(vmin=min_HI, vmax=max_HI))

axa = axes([0.91, 0.896-5*dy, 0.015, 0.105])
cbar = fig.colorbar(cax, axa, ax=ax12) #in ax2 colorbar of ax1
cbar.set_label(r"$\Sigma_{\rm HI}\,[hM_\odot{\rm Mpc}^{-2}]$",fontsize=12,labelpad=5)
cbar.ax.tick_params(labelsize=8)  #to change size of ticks

for ax,Mc in zip([ax25,ax26,ax27,ax28],[Mc1[i], Mc2[i], Mc3[i], Mc4[i]]):
    cax = ax.imshow(Mc,cmap=get_cmap('gist_stern'),origin='lower',
                    interpolation='bicubic', extent=[x_min, x_max, y_min, y_max],
                    norm = LogNorm(vmin=min_Mc, vmax=max_Mc))

axa = axes([0.91, 0.896-6*dy, 0.015, 0.105])
cbar = fig.colorbar(cax, axa, ax=ax12) #in ax2 colorbar of ax1
cbar.set_label(r"$\Sigma_{\rm DM}\,[hM_\odot{\rm Mpc}^{-2}]$",fontsize=12,labelpad=5)
cbar.ax.tick_params(labelsize=8)  #to change size of ticks

for ax,ne in zip([ax29,ax30,ax31,ax32],[ne1[i], ne2[i], ne3[i], ne4[i]]):
    cax = ax.imshow(ne,cmap=get_cmap('gist_earth'),origin='lower',
                    interpolation='bicubic', extent=[x_min, x_max, y_min, y_max],
                    norm = LogNorm(vmin=min_ne, vmax=max_ne))

axa = axes([0.91, 0.896-7*dy, 0.015, 0.105])
cbar = fig.colorbar(cax, axa, ax=ax12) #in ax2 colorbar of ax1
cbar.set_label(r"$\Sigma_{\rm e}\,[h{\rm cm}^{-3}{\rm Mpc}^{-1}]$",fontsize=11,labelpad=5)
cbar.ax.tick_params(labelsize=8)  #to change size of ticks

for ax,P in zip([ax33,ax34,ax35,ax36],[P1[i], P2[i], P3[i], P4[i]]):
    cax = ax.imshow(P,cmap=get_cmap('terrain'),origin='lower',
                    interpolation='bicubic', extent=[x_min, x_max, y_min, y_max],
                    norm = LogNorm(vmin=min_P, vmax=max_P))

axa = axes([0.91, 0.896-8*dy, 0.015, 0.105])
cbar = fig.colorbar(cax, axa, ax=ax12) #in ax2 colorbar of ax1
cbar.set_label(r"$P_{\rm g}\,[h^2M_\odot{\rm kms}^{-1}{\rm kpc}^{-3}]$",fontsize=10,labelpad=5)
cbar.ax.tick_params(labelsize=8)  #to change size of ticks


#cbar = fig.colorbar(cax, ax2, ax=ax1, ticks=[-1, 0, 1]) #in ax2 colorbar of ax1
#cbar.set_label(r"$M_{\rm CSF}\/[h^{-1}M_\odot]$",fontsize=14,labelpad=-50)
#cbar.ax.tick_params(labelsize=10)  #to change size of ticks

#p1,=ax1.plot(x,y,linestyle='-',marker='None')


#place a label in the plot
#ax1.text(0.2,0.1, r"$z=4.0$", fontsize=22, color='k',transform=ax1.transAxes)

#legend
#ax1.legend([p1,p2],
#           [r"$z=3$",
#            r"$z=4$"],
#           loc=0,prop={'size':18},ncol=1,frameon=True)
            
            #columnspacing=2,labelspacing=2)




#ax1.set_title(r'$\sum m_\nu=0.0\/{\rm eV}$',position=(0.5,1.02),size=18)
#title('About as simple as it gets, folks')
#suptitle('About as simple as it gets, folks')  #for title with several panels
#grid(True)
#show()
savefig(f_out, bbox_inches='tight', dpi=150)
close(fig)










###############################################################################
#some useful colors:

#'darkseagreen'
#'yellow'
#"hotpink"
#"gold
#"fuchsia"
#"lime"
#"brown"
#"silver"
#"cyan"
#"dodgerblue"
#"darkviolet"
#"magenta"
#"deepskyblue"
#"orchid"
#"aqua"
#"darkorange"
#"coral"
#"lightgreen"
#"salmon"
#"bisque"
