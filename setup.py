#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


# Add your dependencies in requirements.txt
# Note: you can add test-specific requirements in tox.ini
requirements = []
with open('requirements.txt') as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)


# https://github.com/pypa/setuptools_scm
use_scm = {"write_to": "napari_nikon_nd2/_version.py"}

setup(
    name='napari-nikon-nd2',
    version="0.1.2",
    author='Chris Wood',
    author_email='cwood1967@gmail.com',
    license='Apache Software License 2.0',
    url='https://github.com/cwood1967/napari-nikon-nd2',
    description='Opens Nikon ND2 files into napari.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,
    use_scm_version=use_scm,
    setup_requires=['setuptools_scm', 'nd2reader'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: napari',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'napari.plugin': [
            'napari-nikon-nd2 = napari_nikon_nd2',
        ],
    },
)
