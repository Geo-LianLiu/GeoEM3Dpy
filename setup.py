# Copyright 2023 Lian Liu. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ====================================================================== #
#                       @Author  :   Lian Liu                            #
#                       @e-mail  :   lianliu1017@126.com                 #
# ====================================================================== #

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
