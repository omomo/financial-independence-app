# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import financial-independence-app
version = financial-independence-app.__version__

setup(
    name='Financial Independence Application',
    version=version,
    author='',
    author_email='author@gmail.com',
    packages=[
        'financial-independence-app',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['financial-independence-app/manage.py'],
)
