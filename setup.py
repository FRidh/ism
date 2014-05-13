from setuptools import setup

setup(
      name='ism',
      version='0.0',
      description="Implementation of Image Source Method.",
      long_description=open('README').read(),
      author='Frederik Rietdijk',
      author_email='fridh@fridh.nl',
      license='LICENSE',
      packages=['ism'],
      scripts=[],
      zip_safe=False,
      install_requires=[
          'geometry',
          ],
      )