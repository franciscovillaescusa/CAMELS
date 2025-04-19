from setuptools import setup, find_packages
import numpy

with open("README.md", "r") as f:
    documentation = f.read()

setup(
    name         = 'CAMELS_library',
    version      = "0.6", 
    author       = 'Francisco Villaescusa-Navarro',
    author_email = 'villaescusa.francisco@gmail.com',
    description  = "Python routines to analyze the data from the simulations of the Cosmology and Astrophysics with MachinE Learning Simulations (CAMELS) project",
    url          = "https://github.com/franciscovillaescusa/CAMELS",
    license      = 'MIT',
    long_description_content_type = "text/markdown",
    long_description = documentation,
    packages=find_packages(where="library/"),
    package_dir={"": "library"},
    install_requires=['scipy', 'h5py', 'Pylians', 'tables',
                      'pynbody==1.2.3', 'tqdm'],
)

