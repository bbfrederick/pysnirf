from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 0
_version_micro = 1  # use '' for first of series, number for 1 and above
_version_extra = ''
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ['Development Status :: 4 - Alpha',
               'Intended Audience :: Science/Research',
               'Topic :: Scientific/Engineering :: Medical Science Apps.',
               'License :: OSI Approved :: Apache Software License',
               "Environment :: Console",
               "Operating System :: OS Independent",
               "Programming Language :: Python"]

# Description should be a one-liner:
description = "rapidtide: a suite of programs for doing RIPTiDe analysis"
# Long description will go up on the pypi page
long_description = """
Pysnirf
========
pysnirf is a suite of python programs used to read and write standard near
infrared format files (.snirf file). It aims to comply with the file
specification set out here:
https://docs.google.com/document/d/1EKEMrB6CxmEGnzI4zi7MugHq318HRaR3M2i_vzRIPFU/edit?usp=sharing
To get started using these components in your own software, please go to the
repository README_.
.. _README: https://github.com/bbfrederick/pysnirf/blob/master/README.md
License
=======
``pysnirf`` is licensed under the terms of the Apache 2 license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.
All trademarks referenced herein are property of their respective holders.
Copyright (c) 2016-2018, Blaise Frederick, McLean Hospital Brain Imaging Center
"""

NAME = "pysnirf"
MAINTAINER = "Blaise Frederick"
MAINTAINER_EMAIL = "blaise.frederick@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/bbfrederick/pysnirf"
DOWNLOAD_URL = ""
LICENSE = "Apache"
AUTHOR = "Blaise Frederick"
AUTHOR_EMAIL = "blaise.frederick@gmail.com"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'pysnirf': [pjoin('data', '*')]}
REQUIRES = ['numpy', 'h5py']
