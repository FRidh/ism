from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
      name='ism',
      version='0.1',
      description="Implementation of Image Source Method.",
      #long_description=open('README').read(),
      author='Frederik Rietdijk',
      author_email='fridh@fridh.nl',
      license='LICENSE',
      packages=['ism'],
      scripts=[],
      zip_safe=False,
      install_requires=[
          'geometry',
          'numpy',
          'matplotlib'
          'cython',
          ],
      include_dirs = [np.get_include()], 
      ext_modules = cythonize('ism/*.pyx'),
      )
