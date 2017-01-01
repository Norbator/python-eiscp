#!/usr/bin/env python

import re
from setuptools import setup, find_packages
import sys
import warnings

dynamic_requires = []

version = 1.1

setup(
    name='anthemav',
    version=1.1,
    author='David McNett',
    author_email='nugget@macnugget.org',
    url='https://github.com/nugget/python-anthemav',
    packages=find_packages(),
    scripts=[],
    install_requires=['asyncio'],
    description='Python API for controlling Anthem Receivers',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    include_package_data=True,
    zip_safe=True,
)
