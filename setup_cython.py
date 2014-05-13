import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

ext = Extension(
    "ism._ism",            
    [os.path.join("ism", "_ism.pyx")],     
    language="c++",         
    libraries=["stdc++"],
    )

setup(
    cmdclass = {'build_ext': build_ext},
    include_dirs = [np.get_include()],  
    ext_modules = [ext]
)
