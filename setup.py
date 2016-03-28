# coding: utf8

# Copyright (C) 2016 NOUCHET Christophe
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

setup(
    name='SimplePigKernel',
    version='0.1',
    description='A pig kernel for Jupyter',
    url='http://gogs.atrevrix.fr/Jupyter/SimplePigKernel',
    author='Christophe Nouchet',
    author_email='nouchet.christophe@gmail.com',
    license='GPLv3',
    packages=['PigKernel'],
)
