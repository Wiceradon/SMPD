#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='SMPD',
    version='0.1.0',
    description='University project for kNN classification.',
    long_description=readme + '\n\n' + history,
    author='Jakub Jeleński',
    author_email='jakub.jelenski@runbox.com',
    url='https://github.com/Wiceradon/SMPD',
    packages=[
        'SMPD',
    ],
    package_dir={'SMPD':
                 'SMPD'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='SMPD',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
