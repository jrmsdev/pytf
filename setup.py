#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
from setuptools import setup
from unittest import TestLoader

sys.path.insert (0, './test')

desc = 'Python3 Tests Factory'
tests_discover = TestLoader ().discover ('test', '*_t.py'),

setup(
    name = 'tf',
    version = '0.0',

    description = desc,
    long_description = desc,

    license = 'BSD',
    url = 'https://github.com/jrmsdev/pytf',

    author = 'Jeremías Casteglione',
    author_email = 'jrmsdev@gmail.com',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
    ],

    py_modules = ['tf', 'loader', 'suite', 'tc', 'tc_http'],
    data_files = [
        ('', ['LICENSE', 'README.md']),
        ('examples', ['examples/basic.ini']),
    ],
    zip_safe = False,

    entry_points = {
        'console_scripts': [
            'tf=tf:main',
        ],
    },

    test_suite = 'test.suite',
)
