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


f_out = 'SFRH_2_params_new.pdf'

f_in = '../../../../Results/neural_nets/SFRH_2_params/results/3hd_750_750_750_0.0_3e-3.txt'
data = np.loadtxt(f_in, unpack=False)


fig = figure(figsize=(18,10))     #give dimensions to the figure
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(234)
ax3 = fig.add_subplot(232)
ax4 = fig.add_subplot(235)
ax5 = fig.add_subplot(233)
ax6 = fig.add_subplot(236)

ax1.set_xlim([0.1,0.5])
ax1.set_ylim([0.1,0.5])
ax1.set_xticks([0.1, 0.2, 0.3, 0.4, 0.5])
ax1.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5])

ax2.set_xlim([0.6,1.0])
ax2.set_ylim([0.6,1.0])
ax2.set_xticks([0.6, 0.7, 0.8, 0.9, 1.0])
ax2.set_yticks([0.6, 0.7, 0.8, 0.9, 1.0])

for ax in [ax5,ax6]:
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim([0.5, 2.0])
    ax.set_ylim([0.5, 2.0])
    #ax.set_xticks([0.5, 1.0, 2.0])
    #ax.set_yticks([0.5, 1.0, 2.0])
    #ax.get_xaxis().get_major_formatter().labelOnlyBase = False
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    #ax.xaxis.set_major_formatter( NullFormatter() )   #unset x label 
    #ax.yaxis.set_major_formatter( NullFormatter() )   #unset y label

for ax in [ax3,ax4]:
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim([0.25,4.0])
    ax.set_ylim([0.25,4.0])
    ax.set_xticks([0.25, 0.5, 1.0, 2.0, 4.0])
    ax.set_yticks([0.25, 0.5, 1.0, 2.0, 4.0])
    ax.get_xaxis().get_major_formatter().labelOnlyBase = False
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    

for ax in [ax1,ax2,ax3,ax4,ax5,ax6]:
    ax.plot([0,100],[0,100],linestyle='-',c='r')
    ax.set_xlabel(r'${\rm True}$',fontsize=18)
    ax.set_ylabel(r'${\rm Predicted}$',fontsize=18)


for i,ax,label in zip([0,1,2,3,4,5],[ax1,ax2,ax3,ax4,ax5,ax6],
                      [r'$\Omega_{\rm m}$', r'$\sigma_8$', r'$A_1$',
                       r'$A_2$', r'$A_3$', r'$A_4$']):
    ax.plot(data[:,i],data[:,i+6],linestyle='None',marker='*')
    ax.text(0.05,0.9, label, fontsize=22, color='k',transform=ax.transAxes)



#ax1.set_title(r'$\sum m_\nu=0.0\/{\rm eV}$',position=(0.5,1.02),size=18)
#title('About as simple as it gets, folks')
#suptitle('About as simple as it gets, folks')  #for title with several panels
#grid(True)
#show()
savefig(f_out, bbox_inches='tight')
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
