#!/usr/bin/env python

__version__ = '0.0.1'

import sys
import os
from setuptools import setup  # , find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='SetupVariableTracker',
      version=__version__,
      use_2to3=False,
      author='Rene Vollmer',
      author_email='admin@aypac.de',
      maintainer='Rene Vollmer',
      maintainer_email='admin@aypac.de',
      description='Small library to track and log the declaration of new (setup) variables',
      long_description=read('README.md'),
      url='https://github.com/Aypac/SetupVariableTracker',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers'
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Scientific/Engineering',
      ],
      # license=read('LICENCE'),
      # if we want to install without tests:
      # packages=find_packages(exclude=["*.tests", "tests"]),
      # packages=find_packages(),
      packages=['SetupVariableTracker', ],
      install_requires=['tabulate', 'datetime', 'codecs'],
      # test_suite='pyqip.tests',
      zip_safe=False,
      )
