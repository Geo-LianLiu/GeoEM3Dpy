#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   setup.py
@Time    :   2023/12/08 15:18:46
@Version :   1.0
@Author  :   Lian Liu
@Contact :   lianliu1017@126.com
@License :   (C)Copyright 2023, Lian Liu
@Desc    :   
@Run     :   python setup.py build; python setup.py install
'''

# 1. Import modules
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from setuptools import setup, find_packages


VERSION = '0.1.0'

setup(
    name='GeoEM3Dpy',  # package name
    version=VERSION,  # package version
    description='A python package for 3D geophysical electromagnetic simulation and inversion',  # package description
    packages=find_packages(include=['GeoEM3Dpy*']),
    zip_safe=False,
    author="Lian Liu"
)