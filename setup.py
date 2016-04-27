#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path and open files
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

try:
    REQUIREMENTS = open('requirements.txt').read()
except:
    REQUIREMENTS = None


try:
    README = open('README.md').read()
except:
    README = None

setup(
    name='django-la-links',
    version="v0.1.0",
    description=(
        'Django app for a simple links management '
    ),
    long_description=README,
    install_requires=REQUIREMENTS,
    author='Fábio Piovam Elias',
    author_email='fabio@laborautonomo.org',
    url='https://github.com/laborautonomo/django-la-links/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
