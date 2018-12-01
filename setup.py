#!/usr/bin/env python

from distutils.core import setup

requirements = [
    'requests>=2.0',
    'xmltodict==0.11',
    'boto3>=1.9',
]

setup(name='ebay',
      version='0.1.0',
      description='Python based basic ebay api to get orders from seller central',
      author='Umair Ashraf',
      author_email='umrashrf@gmail.com',
      url='https://github.com/umrashrf/ebay',
      packages=['ebay'],
      install_requires=requirements,
     )
