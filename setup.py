#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('pandoc --from=markdown --to=rst -o README.rst README.md')
    os.system('python setup.py sdist upload')
    sys.exit()

README = open('README.md').read()
HISTORY = open('CHANGES.txt').read().replace('.. :changelog:', '')

setup(
    name='momentx',
    version='0.2.3',
    description="A lightweight wrapper around datetime with a focus on timezone handling and few dependencies (datetime, pytz and six).",
    long_description=README + '\n\n' + HISTORY,
    author='Ulf Bartel',
    author_email='elastic.code@gmail.com',
    url='https://github.com/berlincode/momentx',
    packages=[
        'momentx',
        'momentx.contrib'
    ],
    package_dir={'momentx': 'momentx'},
    include_package_data=True,
    install_requires=['pytz', 'six'], # python already ships datetime and calendar
    license="new-style BSD",
    zip_safe=False,
    keywords='datetime, timezone, wrapper, pytz, simple, moment',
    entry_points={
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
)
