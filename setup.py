#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-featured-objects',
    version='0.0.1-beta',
    description='Pluggable search for Django.',
    author='Pedro Burón',
    author_email='pedro@witoi.com',
    long_description=open('README.md', 'r').read(),
    url='http://desarrollo.witoi.com/',
    packages=[
        'featured',
        'featured.migrations',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)