#!/usr/bin/env python
req = ['nose','python-dateutil','pytz', 'numpy','xarray','matplotlib', 'h5py','scipy',
'pathvalidate', 'sciencedates','pymap3d',
'GeoData',]

# %%
from setuptools import setup,find_packages

setup(name='isrutils',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/isrutils',
      description='utilities for reading and plotting ISR raw data',
      version='0.5.1',
      python_requires='>=3.6',
	  install_requires= req,
      dependency_links = ['https://github.com/jswoboda/GeoDataPython/tarball/master#egg=GeoData-999.0.0',],
      extras_require={'plot':['seaborn',]},
	  )
