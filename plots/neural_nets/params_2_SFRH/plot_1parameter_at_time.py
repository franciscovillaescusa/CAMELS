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

#ax1.set_xticks([])
#ax1.set_yticks([])


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

root = '/mnt/ceph/users/camels'

x_min, x_max = -0.1, 7.1
y_min = [4e-4, 4e-4, 4e-4, 4e-4, 4e-4, 4e-4]
y_max = [0.13, 0.13, 0.13, 0.13, 0.13, 0.13]



fig = figure(figsize=(15,8)) 
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(234)
ax3 = fig.add_subplot(232)
ax4 = fig.add_subplot(235)
ax5 = fig.add_subplot(233)
ax6 = fig.add_subplot(236)

subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=0.2, hspace=0.15)

fin   = '%s/Results/neural_nets/params_2_SFRH/SFRH_ML_pred.txt'%root
f_out = 'SFRH_NN_1parameter.pdf'

# read data
data = np.loadtxt(fin)
z = data[:,0]


for i,ax in enumerate([ax1,ax2,ax3,ax4,ax5,ax6]):
    #ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim([x_min,x_max])
    ax.set_ylim([y_min[i],y_max[i]])

for ax in [ax2,ax4,ax6]:
    ax.set_xlabel(r'$z$',fontsize=18)

for ax in [ax1,ax2]:
    ax.set_ylabel(r'${\rm SFRH}\,[M_\odot{\rm yr^{-1}}{\rm Mpc}^{-3}]$',fontsize=18)

    
for start,end,ax in zip([1,  12, 23, 34, 45, 56],
                        [11, 22, 33, 44, 55, 66],
                        [ax1,ax2,ax3,ax4,ax5,ax6]):

    # read the SFRH
    for i,c in zip(np.arange(start,end,2),['red','orange','k','green','blue']):
        
        ax.plot(z,data[:,i+1],linestyle='-',marker='None',c=c)


#place a label in the plot
ax1.text(0.07, 0.07, r'$\Omega_{\rm m}$', fontsize=22, color='k', transform=ax1.transAxes)
ax2.text(0.07, 0.07, r'$\sigma_8$', fontsize=22, color='k', transform=ax2.transAxes)
ax3.text(0.07, 0.07, r'$A_1$', fontsize=22, color='k', transform=ax3.transAxes)
ax4.text(0.07, 0.07, r'$A_2$', fontsize=22, color='k', transform=ax4.transAxes)
ax5.text(0.07, 0.07, r'$A_3$', fontsize=22, color='k', transform=ax5.transAxes)
ax6.text(0.07, 0.07, r'$A_4$', fontsize=22, color='k', transform=ax6.transAxes)


savefig(f_out, bbox_inches='tight')
close(fig)









