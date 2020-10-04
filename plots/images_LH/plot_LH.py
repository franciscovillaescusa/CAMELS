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

root = '/mnt/ceph/users/camels/Results/images_LH'
seed = 20

x_min, x_max = 0.0, 25.0
y_min, y_max = 0.0, 25.0

rows = 10
cols = 8

for f, f_out,minimum,maximum,cmap,title in zip(['%s/Images_Mgas_IllustrisTNG.npy'%root,
                                                '%s/Images_Mstar_IllustrisTNG.npy'%root,
                                                '%s/Images_Mcdm_IllustrisTNG.npy'%root,
                                                '%s/Images_HI_IllustrisTNG.npy'%root,
                                                '%s/Images_T_IllustrisTNG.npy'%root,
                                                '%s/Images_Vgas_IllustrisTNG.npy'%root,
                                                '%s/Images_Z_IllustrisTNG.npy'%root,
                                                '%s/Images_ne_IllustrisTNG.npy'%root,
                                                '%s/Images_P_IllustrisTNG.npy'%root],
                                    
                                         ['images_Mgas_IllustrisTNG.png',
                                          'images_Mstar_IllustrisTNG.png',
                                          'images_Mcdm_IllustrisTNG.png',
                                          'images_HI_IllustrisTNG.png',
                                          'images_T_IllustrisTNG.png',
                                          'images_Vgas_IllustrisTNG.png',
                                          'images_Z_IllustrisTNG.png',
                                          'images_ne_IllustrisTNG.png',
                                          'images_P_IllustrisTNG.png'], 
                                         
                            [2e9,  2e8,  5e9,  1e4, 2e3,  50.0,  1e-9, 1e5,  1e2], 
                            [5e13, 1e15, 1e15, 1e13, 2e7, 500.0, 7e-2, 1e16, 1e11],
                                ['jet', 'nipy_spectral', 'gist_stern',
                                 'magma', 'hot', 'rainbow', 'cubehelix',
                                 'gist_earth', 'terrain'],

                ['Gas density', 'Stellar mass', 'dark matter density',
                 'Neutral hydrogen', 'Gas temperature', 'Gas velocity',
                 'Gas metallicity', 'Electron density', 'Gas pressure']):


    fig, axs = plt.subplots(rows, cols, figsize=(9.0, 11.2))
    subplots_adjust(left=None, bottom=None, right=None, top=None,
                    wspace=0.1, hspace=0.1)

    for i in range(rows):
        for j in range(cols):
            #axs[i,j].xaxis.set_major_formatter( NullFormatter() )   #unset x label 
            #axs[i,j].yaxis.set_major_formatter( NullFormatter() )   #unset y label
            axs[i,j].tick_params(
                axis='both',          # changes apply to the x-axis
                which='both',      # both major and minor ticks are affected
                bottom=False,      # ticks along the bottom edge are off
                top=False,         # ticks along the top edge are off
                left=False,
                right=False,
                labelleft=False,
                labelbottom=False) # labels along the bottom edge are off

    # read data
    data = np.load(f)
    print('%.3e %.3e'%(np.min(data), np.max(data)))

    # select maps from differnet realizations
    np.random.seed(seed)
    indexes = np.arange(0,data.shape[0],15)
    indexes = np.random.choice(indexes, size=rows*cols, replace=False)
    data = data[indexes]
    
    data[np.where(data<minimum)] = minimum

    num = 0
    for i in range(rows):
        for j in range(cols):
            cax = axs[i,j].imshow(data[num],cmap=get_cmap(cmap),origin='lower',
                        interpolation='bicubic', extent=[x_min, x_max, y_min, y_max],
                                  norm = LogNorm(vmin=minimum, vmax=maximum))
            num += 1

    # colorbar
    axb = axes([0.1267, 0.09, 0.772, 0.015])
    cbar = fig.colorbar(cax, axb, ax=axs[0,0], orientation='horizontal') #in ax2 colorbar of ax1
    cbar.set_label(r"$\Sigma_{\rm g}\/[hM_\odot{\rm Mpc}^{-2}]$",fontsize=14,labelpad=5)
    cbar.ax.tick_params(labelsize=10)  #to change size of ticks

    #suptitle('%s'%title, size=20, y=0.91)  #for title with several panels
    savefig(f_out, bbox_inches='tight', dpi=150)#dpi=300)
    close(fig)

    sys.exit()







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
