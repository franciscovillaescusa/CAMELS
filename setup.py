from setuptools import setup
from setuptools import find_packages
from setuptools import Extension
import numpy

with open("README.md", "r") as f:
    documentation = f.read()

setup(
    name         = 'CAMELS_library',
    version      = "0.3", 
    author       = 'Francisco Villaescusa-Navarro',
    author_email = 'villaescusa.francisco@gmail.com',
    description  = "Python routines to analyze the data from the simulations of the Cosmology and Astrophysics with MachinE Learning Simulations (CAMELS) project",
    url          = "https://github.com/franciscovillaescusa/CAMELS",
    license      = 'MIT',
    long_description_content_type = "text/markdown",
    long_description = documentation,
    packages=find_packages(where="library/"),
    include_dirs=[numpy.get_include()],
    install_requires=['scipy', 'h5py', 'Pylians', 'tables'],
    package_dir={'':'library/'},
    py_modules=['camels_library']
)




