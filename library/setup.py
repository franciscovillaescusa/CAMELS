from distutils.core import setup
from setuptools import find_packages
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

# details on installing python packages can be found here
# https://docs.python.org/3.7/install/

ext_modules = []

setup(
    name    = 'CAMELS library',
    version = "0.1", 
    author  = 'Francisco Villaescusa-Navarro',
    author_email = 'villaescusa.francisco@gmail.com',
    ext_modules = cythonize(ext_modules, include_path=[],
                            compiler_directives={'language_level' : "3"}),
    include_dirs=[numpy.get_include()],
    packages=find_packages(),
    py_modules=['camels_library']
)




