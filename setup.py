from setuptools import setup, find_packages
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
      scripts=[],
      zip_safe=False,
      install_requires=[
          'geometry',
          'numpy',
          'matplotlib',
          #'cython',
          'cytoolz',
          ],
      include_dirs = [np.get_include()], 
      ext_modules = cythonize('ism/*.pyx'),
      packages=find_packages(exclude=["tests"]),
      tests_require=['pytest'],
      package_data={"ism": ["*.pxd"]},
      )
