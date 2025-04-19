# To run this code, use: python -W ignore ramses_2_hdf5.py
# as pynbody gives lots of warnings
# use pynbody 1.2.3 as stable version. Version 2.0.0 has problems with msink for black holes
import numpy as np
import sys,os,h5py
import pynbody
from scipy.io import FortranFile
from scipy.interpolate import griddata


class Cool:
    def __init__(self, n1, n2):
        """
        Creates a python class to store the different lookup tables
        """
        self.n1   = n1                    #number of log10(nH) entries
        self.n2   = n2                    #number of log10(T/mu) entries
        self.nH   = np.zeros([n1])        #actual values of log10(nH)
        self.T2   = np.zeros([n2])        #actual values of log10(T/mu)
        self.cool = np.zeros([n1, n2])    #cool(nH,T/mu)
        self.heat = np.zeros([n1, n2])    #heat(nH,T/mu)
        self.spec = np.zeros([n1, n2, 6]) #log10(ionized_species(nH,T/mu))
        self.ne   = np.zeros([n1, n2])    #log10(ne/nH(nH,T/mu))
        self.mu   = np.zeros([n1, n2])    #mu(nH,T/mu)
        self.HI   = np.zeros([n1, n2])    #log10(n_HI/nH(nH,T/mu))

def interpolate_table(points, table, lognHpart, logT2part):
    """
    This function interpolates a given quantity of the cooling table to get the quantity
    of interest for all gas particles

    points is a np.array([n2*n1,2]) array containing log(nH) and log(T2) entries for the table
    table is a np.array([n2,n1]) array containing the values of the table
    table_values = concatenate(field) will make it np.array([n1*n2])

    lognHpart is an array with the log10(nH) for the gas particles
    logT2part is an array with the log10(T/mu) for the gas particles
    """

    table_values = np.concatenate(table)
    
    # get the mean molecular fraction for each gas particle
    field_interp = griddata(points, table_values,
                            np.array([lognHpart, logT2part]).T, method="linear")
    
    # Fix potential NaNs
    nan_mask = np.isnan(field_interp)
    if np.any(nan_mask):
        field_interp[nan_mask] = griddata(points, table_values,
                                          np.array([lognHpart, logT2part]).T[nan_mask],
                                          method="nearest")
    return field_interp


# This function takes some data and returns a numpy array with the correct dimensions
def clean(dat, n1, n2, spec=False, transpose=False):
    dat = np.array(dat)

    if spec is True:
        dat = dat.reshape(6, n2, n1)
    else:
        dat = dat.reshape(n2, n1)

    if transpose is True:
        dat = np.transpose(dat)

    return dat


# This function reads a Ramses cooling file
def rd_cool(filename):
    with FortranFile(filename, "r") as f:

        # read the number of density and temperatures entries in the table
        n1, n2 = f.read_ints("i") 
        c = Cool(n1, n2)

        # mu is the mean molecular weight (dimensionless)
        # mu = rho/(n*m_H);
        # rho is the mass density of gas
        # n is the number density of particles
        # m_H is the mass of the hydrogen atom

        # read the content of the cooling table
        nH             = f.read_reals("f8") #log10(nH) entries in the cooling table
        T2             = f.read_reals("f8") #log10(T/mu) entries in the cooling table
        cool           = f.read_reals("f8") #log10(cooling rates)
        heat           = f.read_reals("f8") #log10(heating rates)
        cool_com       = f.read_reals("f8")
        heat_com       = f.read_reals("f8")
        metal          = f.read_reals("f8")
        cool_prime     = f.read_reals("f8")
        heat_prime     = f.read_reals("f8")
        cool_com_prime = f.read_reals("f8")
        heat_com_prime = f.read_reals("f8")
        metal_prime    = f.read_reals("f8")
        mu             = f.read_reals("f8") #mu values not in log10
        n_spec         = f.read_reals("f8") #log10(n_e, n_HI, n_HII, n_HeI, n_HeII, n_HeIII)

        # fill the cooling class with its values
        c.nH   = nH                  #log10(nH)   entries in the cooling table
        c.T2   = T2                  #log10(T/mu) entries in the cooling table
        c.cool = clean(cool, n1, n2) #cooling rates with dimensions (n2,n1)
        c.heat = clean(heat, n1, n2) #heating rates with dimensions (n2,n2)
        c.mu   = clean(mu,   n1, n2) #mean molecular weight with dimensions (n2,n1)
        c.spec = clean(n_spec, n1, n2, spec=True) #ionized species. Dimensions (6,n2,1)

        # beyond the ionized species, also get log10(ne/nH) and log10(nHI/nH) 
        c.ne = c.spec[0]
        c.HI = c.spec[1]
        for i in range(n2):
            c.ne[i, :] = c.spec[0, i, :] - c.nH #log(ne)  - log(nH) = log(ne/nH)
            c.HI[i, :] = c.spec[1, i, :] - c.nH #log(nHI) - log(nH) = log(nHI/nH)
            
        return nH, T2, c



class ramses_2_hdf5():
    def __init__(self, snapshot, BoxSize):
        """
        snapshot: '/mnt/ceph/users/camels/Sims/Ramses/L25n256/CV/CV_0/output_00092'
        BoxSize: 25000.0 #kpc/h
        """

        # get some units
        self.Msun = 1.988e33      #grams
        self.kpc  = 3.0857e21     #cm
        self.km   = 1e5           #cm
        self.kB   = 1.380649e-26  #grams*(km^2/s^2)/K
        self.mH   = 1.6735575e-24 #grams

        # compression kwargs
        self.ck = {'compression': 'gzip', 'compression_opts': 4}
        
        # read the box size
        self.data         = pynbody.load(snapshot)
        self.Omega_m      = self.data.properties['omegaM0']
        self.Omega_l      = self.data.properties['omegaL0']
        self.h            = self.data.properties['h']
        self.scale_factor = self.data.properties['a']
        self.redshift     = 1.0/self.data.properties['a'] - 1.0
        self.BoxSize      = BoxSize
        self.snapshot     = snapshot
        print(self.data.properties)
        print(self.data.families())


    def write_header(self, f):
        """
        This method writes the header of the snapshot
        """
        
        header = f.create_group("Header")
        header.attrs['BoxSize']                  = np.array(self.BoxSize,      dtype=np.float64)
        header.attrs['Flag_Cooling']             = np.array(1,                 dtype=np.int32)
        header.attrs['Flag_DoublePrecision']     = np.array(0,                 dtype=np.int32)
        header.attrs['Flag_Feedback']            = np.array(1,                 dtype=np.int32)
        header.attrs['Flag_Metals']              = np.array(0,                 dtype=np.int32)
        header.attrs['Flag_Sfr']                 = np.array(1,                 dtype=np.int32)
        header.attrs['Flag_StellarAge']          = np.array(0,                 dtype=np.int32)
        header.attrs['HubbleParam']              = np.array(self.h,            dtype=np.float64)
        header.attrs['MassTable']                = np.array([0,0,0,0,0,0],     dtype=np.float64)
        header.attrs['NumFilesPerSnapshot']      = np.array(1,                 dtype=np.int32)
        header.attrs['NumPart_Total_HighWord']   = np.array([0,0,0,0,0,0],     dtype=np.uint32)
        header.attrs['Omega0']                   = np.array(self.Omega_m,      dtype=np.float64)
        header.attrs['OmegaBaryon']              = np.array(0.049,             dtype=np.float64)
        header.attrs['OmegaLambda']              = np.array(1.0-self.Omega_m,  dtype=np.float64)
        header.attrs['Redshift']                 = np.array(self.redshift,     dtype=np.float64)
        header.attrs['Time']                     = np.array(self.scale_factor, dtype=np.float64)
        header.attrs['UnitLength_in_cm']         = np.array(3.085678e+21,      dtype=np.float64)
        header.attrs['UnitMass_in_g']            = np.array(1.989e+43,         dtype=np.float64)
        header.attrs['UnitVelocity_in_cm_per_s'] = np.array(100000.0,          dtype=np.float64)

        self.header = header

    def get_ions(self):
        """
        This method computes the ne/nH, nHI/nH, and the gas temperature
        """

        data     = self.data
        mH       = self.mH
        kB       = self.kB
        h        = self.h

        # get the name of the cooling file
        coolcode = self.snapshot[-5:]
        coolpath = f"{self.snapshot}/cooling_{coolcode}.out"

        # read the cooling table
        # lognH and logT2 are the entries of the cooling table
        # c is a class with several lookup tables, including ne and nHI
        # points just creates a np.array([n2*n1,2]) containing the values of lognH and logT2
        # for the cooling table
        lognH, logT2, c = rd_cool(coolpath) 
        lognHvals, logT2vals = np.meshgrid(lognH, logT2)
        points = np.array([np.concatenate(lognHvals), np.concatenate(logT2vals)]).T

        # compute the number density of hydrogen atoms for the gas particles
        # units of density are g/cm^3; factors of h are already taken into account
        lognHpart = np.log10(data.gas["rho"].in_units("g cm**-3")*0.76/mH)
        #Romain: some values are outside range of cooling table. Do I need to worry about h values?

        # compute the gas temperature
        # when reading P_g and rho_g, the units are physical, i.e. there are no factors of h
        P_g       = data.gas['p'].in_units('Msol km**-1 s**-2')  #Msun/km/s^2
        rho_g     = data.gas['rho'].in_units('Msol km**-3')      #Msun/km^3
        T_g       = P_g/rho_g*(mH/kB)                            #K This is T/mu
        logT2part = np.log10(T_g)
        #logT2gal = np.log10(data.gas["temp"])

        # get the mean molecular fraction for each gas particle and gas temperature
        mu = interpolate_table(points, c.mu, lognHpart, logT2part)
        T  = T_g*mu
        self.T = T
        # Romain: why ratio between pynbody and T/mu only has two values?

        # get nHI/nH and ne/nH
        logne = interpolate_table(points, c.ne, lognHpart, logT2part) #This is log10(ne/nH)
        logHI = interpolate_table(points, c.HI, lognHpart, logT2part) #This is log10(nHI/nH)
        ne    = 10**logne    #This is ne/nH
        HI    = 10**logHI    #This is nHI/nH
        
        #nHgal     = 10**lognHgal  #TODO: use lognH or log nHgal? Ask Romain
        #nElectron = xion * nHgal  #TODO: use lognH or log nHgal? Ask Romain
        
        self.ne        = ne
        self.HI        = HI
        print(self.ne.shape)
        print(self.HI.shape)
        print(f'{np.min(ne):.3e} < ne < {np.max(ne):.3e}')
        print(f'{np.min(HI):.3e} < HI < {np.max(HI):.3e}')
        print(f'{np.min(T):.3e} < T  < {np.max(T):.3e}')
        

    def write_gas(self, f):
        """
        This method writes the properties of the gas particles
        """

        data     = self.data
        kpc      = self.kpc
        Msun     = self.Msun
        km       = self.km
        mH       = self.mH
        kB       = self.kB
        redshift = self.redshift
        BoxSize  = self.BoxSize
        h        = self.h
        ck       = self.ck
        
        pos_g   = data.gas['pos'].in_units('kpc h**-1')*(1.0+redshift) #ckpc/h
        vel_g   = data.gas['vel'].in_units('km s**-1')                 #km/s
        mass_g  = data.gas['mass'].in_units('Msol h**-1')              #Msun/h
        P_g     = data.gas['p'].in_units('Msol km**-1 s**-2')          #Msun/km/s^2
        rho_g   = data.gas['rho'].in_units('Msol km**-3')              #Msun/km^3
        U_g     = P_g/(5.0/3.0-1)/rho_g                                #(km/s)^2
        rho_g   = data.gas['rho'].in_units('Msol h**2 kpc**-3')
        rho_g   = rho_g/(1.0 + redshift)**3                            #(Msun/h)/(ckpc/h)^3
        Z_g     = data.gas['metal'].astype(np.float32)
        L_g     = data.gas['smooth'].in_units('kpc h**-1')*(1.0+redshift) #ckpc/h (AMR cell size)
        level_g = np.around(np.log2(BoxSize/L_g)).astype(np.int32)     #corresponding AMR level
        TKED_g  = data.gas['scalar_01'] #turbulent kinetic energy density g/cm^3 cm^2/s^2 
        TKED_g  = TKED_g*kpc**3/Msun/km**2/(1.0+redshift)**3/h**2      #(km/s)^2*(Msun/h)/(ckpc/h)^3
        #T2      = data.gas['temp']
        self.get_ions() #this gets ne/nH, nHI/nH, and T

        #no need to save pressure, as it satisfies
        #P_g = (gamma-1)*U_g*rho_g where gamma = 5/3
        #P_g   = data.gas['p'].in_units('Msol h**2 km**2 s**-2 kpc**-3') #(Msun/h)*(km/s)^2/(kpc/h)^3
        #P_g   = P_g/(1.0 + redshift)**3
        #print(P_g.units)
        #gamma = P_g/(U_g*rho_g)
        #print(f'{np.min(gamma)} {np.max(gamma)}')
        #sys.exit()
        
        self.Ng = pos_g.shape[0]
        pos_g   = pos_g.astype(np.float32)
        vel_g   = vel_g.astype(np.float32)
        mass_g  = mass_g.astype(np.float32)
        rho_g   = rho_g.astype(np.float32)           
        U_g     = U_g.astype(np.float32)
        TKED_g  = TKED_g.astype(np.float32)
        self.T  = self.T.astype(np.float32)
        self.ne = self.ne.astype(np.float32)
        self.HI = self.HI.astype(np.float32)

        print('\n################## gas ###################')
        print(data.gas.loadable_keys())
        print(f'Found {self.Ng} gas particles')
        print(f'Omega_g = {np.sum(mass_g)/2.775e2/BoxSize**3:.4f}')
        print(f'{np.min(pos_g[:,0]):10.3f} < X     < {np.max(pos_g[:,0]):10.3f}', end='')
        print(f'{str(pos_g.dtype):>10} {str(pos_g.units):>10}')
        print(f'{np.min(pos_g[:,1]):10.3f} < Y     < {np.max(pos_g[:,1]):10.3f}', end='')
        print(f'{str(pos_g.dtype):>10} {str(pos_g.units):>10}')
        print(f'{np.min(pos_g[:,2]):10.3f} < Z     < {np.max(pos_g[:,2]):10.3f}', end='')
        print(f'{str(pos_g.dtype):>10} {str(pos_g.units):>10}')
        print(f'{np.min(vel_g[:,0]):10.3f} < Vx    < {np.max(vel_g[:,0]):10.3f}', end='')
        print(f'{str(vel_g.dtype):>10} {str(vel_g.units):>10}')
        print(f'{np.min(vel_g[:,1]):10.3f} < Vy    < {np.max(vel_g[:,1]):10.3f}', end='')
        print(f'{str(vel_g.dtype):>10} {str(vel_g.units):>10}')
        print(f'{np.min(vel_g[:,2]):10.3f} < Vz    < {np.max(vel_g[:,2]):10.3f}', end='')
        print(f'{str(vel_g.dtype):>10} {str(vel_g.units):>10}')
        print(f'{np.min(mass_g):10.3e} < M     < {np.max(mass_g):10.3e}', end='')
        print(f'{str(mass_g.dtype):>10} {str(mass_g.units):>10}')
        print(f'{np.min(U_g):10.3e} < U     < {np.max(U_g):10.3e}', end='')
        print(f'{str(U_g.dtype):>10} {str(U_g.units):>10}')
        print(f'{np.min(Z_g):10.3e} < Z     < {np.max(Z_g):10.3e}', end='')
        print(f'{str(Z_g.dtype):>10} {str(Z_g.units):>10}')
        print(f'{np.min(TKED_g):10.3e} < TKED  < {np.max(TKED_g):10.3e}', end='')
        print(f'{str(TKED_g.dtype):>10} (Msun/h)(km/s)^2/(kpc/h)^3')
        print(f'{np.min(rho_g):10.3e} < rho   < {np.max(rho_g):10.3e}', end='')
        print(f'{str(rho_g.dtype):>10} {str(rho_g.units):>10}')
        print(f'{np.min(P_g):10.3e} < P     < {np.max(P_g):10.3e}', end='')
        print(f'{str(P_g.dtype):>10} {str(P_g.units):>10}')
        print(f'{np.min(level_g):10d} < level < {np.max(level_g):10d}', end='')
        print(f'{str(level_g.dtype):>10} NoUnit()')


        # write gas section
        #, compression='gzip', compression_opts=4)
        gas = f.create_group("PartType0")
        gas.create_dataset('Coordinates',    data=pos_g, **ck)         #ckpc/h
        gas.create_dataset('Masses',         data=mass_g/1e10, **ck)   #1e10*Msun/h
        gas.create_dataset('Velocities',     data=vel_g, **ck)         #km/s
        gas.create_dataset('InternalEnergy', data=U_g, **ck)           #(km/s)^2
        gas.create_dataset('Density',        data=rho_g/1e10, **ck)    #1e10*(Msun/h)/(ckpc/h)**3
        gas.create_dataset('TKED',           data=TKED_g/1e10, **ck)   #(km/s)^2*(1e10*Msun/h)/(ckpc/h)^3
        gas.create_dataset('Metallicity',    data=Z_g, **ck)           #M_metals/M_total
        gas.create_dataset('AMR_level',      data=level_g, **ck)       #AMR level
        gas.create_dataset('NeutralHydrogenAbundance', data=self.HI, **ck) #nHI/nH
        gas.create_dataset('ElectronAbundance',        data=self.ne, **ck) #ne/nH
        gas.create_dataset('Temperature',              data=self.T, **ck)  #K


    def write_dm(self,f):
        """
        This method write the properties of the dark matter particles to file
        """

        data     = self.data
        redshift = self.redshift
        BoxSize  = self.BoxSize
        ck       = self.ck

        # read the positions, velocities, masses, IDs and levels of the DM particles
        pos_c   = data.dm['pos'].in_units('kpc h**-1')*(1.0+redshift) #ckpc/h
        vel_c   = data.dm['vel'].in_units('km s**-1')
        mass_c  = data.dm['mass'].in_units('Msol h**-1') #Msun/h
        IDs_c   = data.dm['iord']
        level_c = data.dm['level']
        
        self.Nc = pos_c.shape[0]
        pos_c   = pos_c.astype(np.float32)
        vel_c   = vel_c.astype(np.float32)
        mass_c  = mass_c.astype(np.float32)

        print('\n############### dark matter ################')
        print(data.dm.loadable_keys())
        print(f'Found {self.Nc} dark matter particles')
        print(f'Omega_c = {np.sum(mass_c)/2.775e2/BoxSize**3:.4f}')
        print(f'{np.min(pos_c[:,0]):10.3f} < X     < {np.max(pos_c[:,0]):10.3f}', end='')
        print(f'{str(pos_c.dtype):>10} {str(pos_c.units):>10}')
        print(f'{np.min(pos_c[:,1]):10.3f} < Y     < {np.max(pos_c[:,1]):10.3f}', end='')
        print(f'{str(pos_c.dtype):>10} {str(pos_c.units):>10}')
        print(f'{np.min(pos_c[:,2]):10.3f} < Z     < {np.max(pos_c[:,2]):10.3f}', end='')
        print(f'{str(pos_c.dtype):>10} {str(pos_c.units):>10}')
        print(f'{np.min(vel_c[:,0]):10.3f} < Vx    < {np.max(vel_c[:,0]):10.3f}', end='')
        print(f'{str(vel_c.dtype):>10} {str(vel_c.units):>10}')
        print(f'{np.min(vel_c[:,1]):10.3f} < Vy    < {np.max(vel_c[:,1]):10.3f}', end='')
        print(f'{str(vel_c.dtype):>10} {str(vel_c.units):>10}')
        print(f'{np.min(vel_c[:,2]):10.3f} < Vz    < {np.max(vel_c[:,2]):10.3f}', end='')
        print(f'{str(vel_c.dtype):>10} {str(vel_c.units):>10}')
        print(f'{np.min(mass_c):10.3e} < M     < {np.max(mass_c):10.3e}', end='')
        print(f'{str(mass_c.dtype):>10} {str(mass_c.units):>10}')
        print(f'{np.min(IDs_c):10d} < IDs   < {np.max(IDs_c):10d}', end='')        
        print(f'{str(IDs_c.dtype):>10} {str(IDs_c.units):>10}')
        print(f'{np.min(level_c):10d} < level < {np.max(level_c):10d}', end='')
        print(f'{str(level_c.dtype):>10} {str(level_c.units):>10}')

        # write cdm section
        dm = f.create_group("PartType1")
        dm.create_dataset('Coordinates', data=pos_c, **ck)       #ckpc/h
        dm.create_dataset('Masses',      data=mass_c/1e10, **ck) #1e10*Msun/h
        dm.create_dataset('Velocities',  data=vel_c, **ck)       #km/s
        dm.create_dataset('ParticleIDs', data=IDs_c, **ck)       #dimensionless
        dm.create_dataset('AMR_level',   data=level_c, **ck)     #dimensionless


    def write_stars(self, f):
        """
        This method writes the properties of stars to file
        """

        data     = self.data
        redshift = self.redshift
        BoxSize  = self.BoxSize
        ck       = self.ck

        pos_s   = data.star['pos'].in_units('kpc h**-1')*(1.0+redshift) #ckpc/h
        vel_s   = data.star['vel'].in_units('km s**-1')                 #km/s
        mass_s  = data.star['mass'].in_units('Msol h**-1')              #Msun/h
        Z_s     = data.star['metal'].astype(np.float32)                 #M_metals/M_total
        IDs_s   = data.star['iord'] + self.Nc #add an offset equal to the number of DM particles
        level_s = data.star['level']                                    #dimensionless
        tform_s = data.star['tform'].in_units('Gyr')                    #Gyr

        self.Ns = pos_s.shape[0]
        pos_s   = pos_s.astype(np.float32)
        vel_s   = vel_s.astype(np.float32)
        mass_s  = mass_s.astype(np.float32)
        tform_s = tform_s.astype(np.float32)
        
        print('\n############### Stars ################')
        print(data.star.loadable_keys())
        print(f'Found {self.Ns} star particles')
        print(f'Omega_s = {np.sum(mass_s)/2.775e2/BoxSize**3:.4f}')
        print(f'{np.min(pos_s[:,0]):10.3f} < X     < {np.max(pos_s[:,0]):10.3f}', end='')
        print(f'{str(pos_s.dtype):>10} {str(pos_s.units):>10}')
        print(f'{np.min(pos_s[:,1]):10.3f} < Y     < {np.max(pos_s[:,1]):10.3f}', end='')
        print(f'{str(pos_s.dtype):>10} {str(pos_s.units):>10}')
        print(f'{np.min(pos_s[:,2]):10.3f} < Z     < {np.max(pos_s[:,2]):10.3f}', end='')
        print(f'{str(pos_s.dtype):>10} {str(pos_s.units):>10}')
        print(f'{np.min(vel_s[:,0]):10.3f} < Vx    < {np.max(vel_s[:,0]):10.3f}', end='')
        print(f'{str(vel_s.dtype):>10} {str(vel_s.units):>10}')
        print(f'{np.min(vel_s[:,1]):10.3f} < Vy    < {np.max(vel_s[:,1]):10.3f}', end='')
        print(f'{str(vel_s.dtype):>10} {str(vel_s.units):>10}')
        print(f'{np.min(vel_s[:,2]):10.3f} < Vz    < {np.max(vel_s[:,2]):10.3f}', end='')
        print(f'{str(vel_s.dtype):>10} {str(vel_s.units):>10}')
        print(f'{np.min(mass_s):10.3e} < M     < {np.max(mass_s):10.3e}', end='')
        print(f'{str(mass_s.dtype):>10} {str(mass_s.units):>10}')
        print(f'{np.min(Z_s):10.3e} < Z     < {np.max(Z_s):10.3e}', end='')
        print(f'{str(Z_s.dtype):>10} {str(Z_s.units):>10}')
        print(f'{np.min(tform_s):10.3e} < tform < {np.max(tform_s):10.3e}', end='')
        print(f'{str(tform_s.dtype):>10} {str(tform_s.units):>10}')
        print(f'{np.min(IDs_s):10d} < IDs   < {np.max(IDs_s):10d}', end='')        
        print(f'{str(IDs_s.dtype):>10} {str(IDs_s.units):>10}')
        print(f'{np.min(level_s):10d} < level < {np.max(level_s):10d}', end='')
        print(f'{str(level_s.dtype):>10} {str(level_s.units):>10}')

        # write stars section
        stars = f.create_group("PartType4")
        stars.create_dataset('Coordinates',   data=pos_s, **ck)         #ckpc/h
        stars.create_dataset('Velocities',    data=vel_s, **ck)         #km/s
        stars.create_dataset('Masses',        data=mass_s/1e10, **ck)   #1e10*Msun/h
        stars.create_dataset('ParticleIDs',   data=IDs_s, **ck)         #dimensionless
        stars.create_dataset('Metallicity',   data=Z_s, **ck)           #dimensionless
        stars.create_dataset('AMR_level',     data=level_s, **ck)       #dimensionless
        stars.create_dataset('FormationTime', data=tform_s, **ck)       #Gyr

    def write_bh(self,f):
        """
        This method write the properties of the black-holes to file
        """

        data     = self.data
        redshift = self.redshift
        BoxSize  = self.BoxSize
        ck       = self.ck
        
        pos_bh     = data.bh['pos'].in_units('kpc h**-1')*(1.0+redshift) #ckpc/h
        vel_bh     = data.bh['vel'].in_units('km s**-1')                 #km/s
        mass_bh    = data.bh['msink'].in_units('Msol h**-1')             #Msun/h
        tform_bh   = data.bh['tform'].in_units('Gyr')                    #Gyr
        level_bh   = data.bh['level '].astype(np.int32)                  #dimensionless
        lx         = data.bh['lx'].in_units('Msol kpc h**-2 km s**-1')*(1.0+redshift)
        ly         = data.bh['ly'].in_units('Msol kpc h**-2 km s**-1')*(1.0+redshift)
        lz         = data.bh['lz'].in_units('Msol kpc h**-2 km s**-1')*(1.0+redshift)
        l_bh       = np.zeros(pos_bh.shape, dtype=np.float32)
        l_bh[:,0]  = ly                                                  #(Msun/h)*(ckpc/h)*(km/s)
        l_bh[:,1]  = ly                                                  #(Msun/h)*(ckpc/h)*(km/s)
        l_bh[:,2]  = lz                                                  #(Msun/h)*(ckpc/h)*(km/s)
        vx_gas     = data.bh['vx_gas'].in_units('km s**-1').astype(np.float32)   #km/s
        vy_gas     = data.bh['vy_gas'].in_units('km s**-1').astype(np.float32)   #km/s
        vz_gas     = data.bh['vz_gas'].in_units('km s**-1').astype(np.float32)   #km/s
        v_gas      = np.zeros(pos_bh.shape, dtype=np.float32)
        v_gas[:,0] = vx_gas
        v_gas[:,1] = vy_gas
        v_gas[:,2] = vz_gas
        cs2        = data.bh['cs**2'].in_units('km**2 s**-2').astype(np.float32)      #(km/s)^2
        acc_rate   = data.bh['acc_rate'].in_units('Msol Myr**-1').astype(np.float32)  #Msun/Myr
        rho_gas    = data.bh['rho_gas'].in_units('Msol h**2 kpc**-3')/(1.0+redshift)**3 #(Msun/h)/(ckpc/h)^3
        IDs_bh   = data.bh['id'].astype(np.int32)                      #dimensionless
        self.Nbh = pos_bh.shape[0]
        
        pos_bh   = pos_bh.astype(np.float32)
        vel_bh   = vel_bh.astype(np.float32)
        mass_bh  = mass_bh.astype(np.float32)
        tform_bh = tform_bh.astype(np.float32)
        rho_gas  = rho_gas.astype(np.float32)
        
        print('\n############ Black Holes #############')
        print(data.bh.loadable_keys())
        print(f'Found {self.Nbh} star particles')
        print(f'Omega_bh = {np.sum(mass_bh)/2.775e2/BoxSize**3:.4f}')
        print(f'{np.min(pos_bh[:,0]):10.3f} < X        < {np.max(pos_bh[:,0]):10.3f}', end='')
        print(f'{str(pos_bh.dtype):>10} {str(pos_bh.units):>10}')
        print(f'{np.min(pos_bh[:,1]):10.3f} < Y        < {np.max(pos_bh[:,1]):10.3f}', end='')
        print(f'{str(pos_bh.dtype):>10} {str(pos_bh.units):>10}')
        print(f'{np.min(pos_bh[:,2]):10.3f} < Z        < {np.max(pos_bh[:,2]):10.3f}', end='')
        print(f'{str(pos_bh.dtype):>10} {str(pos_bh.units):>10}')
        print(f'{np.min(vel_bh[:,0]):10.3f} < Vx       < {np.max(vel_bh[:,0]):10.3f}', end='')
        print(f'{str(vel_bh.dtype):>10} {str(vel_bh.units):>10}')
        print(f'{np.min(vel_bh[:,1]):10.3f} < Vy       < {np.max(vel_bh[:,1]):10.3f}', end='')
        print(f'{str(vel_bh.dtype):>10} {str(vel_bh.units):>10}')
        print(f'{np.min(vel_bh[:,2]):10.3f} < Vz       < {np.max(vel_bh[:,2]):10.3f}', end='')
        print(f'{str(vel_bh.dtype):>10} {str(vel_bh.units):>10}')
        print(f'{np.min(mass_bh):10.3e} < M        < {np.max(mass_bh):10.3e}', end='')
        print(f'{str(mass_bh.dtype):>10} {str(mass_bh.units):>10}')
        print(f'{np.min(tform_bh):10.3e} < tform    < {np.max(tform_bh):10.3e}', end='')
        print(f'{str(tform_bh.dtype):>10} {str(tform_bh.units):>10}')
        print(f'{np.min(l_bh[:,0]):10.3e} < lx       < {np.max(l_bh[:,0]):10.3e}', end='')
        print(f'{str(l_bh.dtype):>10} NoUnit()')
        print(f'{np.min(l_bh[:,1]):10.3e} < ly       < {np.max(l_bh[:,1]):10.3e}', end='')
        print(f'{str(l_bh.dtype):>10} NoUnit()')
        print(f'{np.min(l_bh[:,2]):10.3e} < lz       < {np.max(l_bh[:,2]):10.3e}', end='')
        print(f'{str(l_bh.dtype):>10} NoUnit()')
        print(f'{np.min(v_gas[:,0]):10.3e} < vx_gas   < {np.max(v_gas[:,0]):10.3e}', end='')
        print(f'{str(v_gas.dtype):>10} NoUnit()')
        print(f'{np.min(v_gas[:,1]):10.3e} < vy_gas   < {np.max(v_gas[:,1]):10.3e}', end='')
        print(f'{str(v_gas.dtype):>10} NoUnit()')
        print(f'{np.min(v_gas[:,2]):10.3e} < vz_gas   < {np.max(v_gas[:,2]):10.3e}', end='')
        print(f'{str(v_gas.dtype):>10} NoUnit()')
        print(f'{np.min(cs2):10.3e} < cs^2     < {np.max(cs2):10.3e}', end='')
        print(f'{str(cs2.dtype):>10} {str(cs2.units):>10}')
        print(f'{np.min(acc_rate):10.3e} < acc_rate < {np.max(acc_rate):10.3e}', end='')
        print(f'{str(acc_rate.dtype):>10} {str(acc_rate.units):>10}')
        print(f'{np.min(rho_gas):10.3e} < rho_gas  < {np.max(rho_gas):10.3e}', end='')
        print(f'{str(rho_gas.dtype):>10} {str(rho_gas.units):>10}')
        print(f'{np.min(level_bh):10d} < level    < {np.max(level_bh):10d}', end='')
        print(f'{str(level_bh.dtype):>10} {str(level_bh.units):>10}')
        print(f'{np.min(IDs_bh):10d} < IDs      < {np.max(IDs_bh):10d}', end='')        
        print(f'{str(IDs_bh.dtype):>10} {str(IDs_bh.units):>10}')

        # write black-holes section
        bh = f.create_group("PartType5")
        bh.create_dataset('Coordinates',     data=pos_bh, **ck)           #ckpc/h
        bh.create_dataset('Velocities',      data=vel_bh, **ck)           #km/s
        bh.create_dataset('Masses',          data=mass_bh/1e10, **ck)     #1e10*Msun/h
        bh.create_dataset('FormationTime',   data=tform_bh, **ck)         #Gyr; conformal time
        bh.create_dataset('AngularMomentum', data=l_bh/1e10, **ck)        #(1e10*Msun/h)*(ckpc/h)*(km/s)
        bh.create_dataset('v_gas',           data=v_gas, **ck)            #km/s
        bh.create_dataset('cs2',             data=cs2, **ck)              #(km/s)^2
        bh.create_dataset('acc_rate',        data=acc_rate/1e10, **ck)    #1e10*Msun/Myr
        bh.create_dataset('rho_gas',         data=rho_gas/1e0, **ck)      #(1e10*Msun/h)/(ckpc/h)^3
        bh.create_dataset('AMR_level',       data=level_bh, **ck)         #dimensionlesss
        bh.create_dataset('ParticleIDs',     data=IDs_bh+2*self.Nc, **ck) #dimensionless; add offset of 2*Nc
        
        
    def write_hdf5(self, fout):
        """
        This method converts the Ramses snapshot to an IllustrisTNG-like hdf5 file
        """
        
        # write hdf5 file
        f = h5py.File(fout, 'w')
        self.write_header(f)
        self.write_gas(f)
        self.write_dm(f)
        self.write_stars(f)
        self.write_bh(f)

        # finish header attributes
        self.header.attrs['NumPart_ThisFile'] = np.array([self.Ng,self.Nc,0,0,self.Ns,self.Nbh],
                                                         dtype=np.int32)
        self.header.attrs['NumPart_Total']    = np.array([self.Ng,self.Nc,0,0,self.Ns,self.Nbh],
                                                         dtype=np.uint32)
        f.close()



