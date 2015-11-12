#!/usr/bin/env python3

from setuptools import setup
import subprocess,os
#%%
with open('README.rst','r') as f:
	long_description = f.read()

setup(name='isrutils',
      version='0.1',
	  description='Utilities for working with Incoherent Scatter Radar raw data (initially targeted for PFISR)',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/isrutils',
	  install_requires=['pathlib2'],
      packages=['isrutils'],
	  )
#%%
try:
    subprocess.call(['conda','install','--yes','--file','requirements.txt'],env={'PATH': os.environ['PATH']},shell=False)
except Exception as e:
    print('you will need to install packages in requirements.txt  {}'.format(e))
