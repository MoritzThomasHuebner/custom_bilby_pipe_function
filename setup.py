#!/usr/bin/env python

from setuptools import setup
import subprocess
import sys
import os

# check that python version is 3.5 or above
python_version = sys.version_info
if python_version < (3, 5):
    sys.exit("Python < 3.5 is not supported, aborting setup")
print("Confirmed Python version {}.{}.{} >= 3.5.0".format(*python_version[:3]))

# get version info from __init__.py
def readfile(filename):
    with open(filename) as fp:
        filecontents = fp.read()
    return filecontents


VERSION = '1.0'

setup(name='custom_bilby_pipe_function',
      description='Just a brief tutorial',
      author='Moritz Huebner',
      author_email='moritz.huebner@monash.edu',
      license="MIT",
      version=VERSION,
      packages=['custom_bilby_pipe_function'],
      package_dir={'custom_bilby_pipe_function': 'custom_bilby_pipe_function'},
      package_data={},
      python_requires='>=3.5',
      install_requires=[
          'bilby'],
      entry_points={},
      classifiers=[
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Operating System :: OS Independent"])