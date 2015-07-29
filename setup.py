#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


requirements = [
    'GitPython',
    'six',
    'requests',
    'python-dateutil',
    'cached-property'
]

setup(
    name="tta",
    version="0.2.0",
    url="https://github.com/erm0l0v/tta",

    author="Kirill Ermolov",
    author_email="erm0l0v@ya.ru",

    description="Time Tracker Autocompleter for Muranosoft",
    long_description=open('README.rst').read(),

    packages=['tta'],

    package_dir={'tta':
                 'tta'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,

    entry_points={
        'console_scripts': [
            'tta = tta.__main__:main',
        ]
    },

    keywords='Time Tracker, Autocomplete, Muranosoft',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    test_suite='tests',
)
