.. pysnirf documentation master file, created by
   sphinx-quickstart on Thu Jun 16 15:27:19 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

The pretty html version of this file can be found here: http://pysnirf.readthedocs.io/en/latest/

pysnirf
==========
pysnirf is a suite of python programs used to read and write standard near infrared format files (.snirf file).  It aims to comply with the file specification set out here: https://docs.google.com/document/d/1EKEMrB6CxmEGnzI4zi7MugHq318HRaR3M2i_vzRIPFU/edit?usp=sharing

.. toctree::
   :maxdepth: 2

Introduction
============
      
Python version compatibility: 
-----------------------------
This code has been tested in python 2.7, 3.5, and 3.6.  I try very hard not to use any version dependant features when I write programs, so it will probably work on any subversion of python 3.  I think there is some weirdness in the python's numerical routines in versions 2.6 and below, so no guarantees it will work in anything lower than 2.7.
      
How do I cite this?
-------------------
Don't know yet.

What’s included in this package?
================================
For the time being, I’m including the following:

snirftest
----------

Description:
^^^^^^^^^^^^

	This script writes a  sample snirf file, filling most of the fields in the spec, then reads it back.  This proves that the library is compatible with itself, which isn't nothing, but it isn't much.

Inputs:
^^^^^^^
        None

Outputs:
^^^^^^^^
	Creates the file 'testfile.snirf' in the run directory.

Usage:
^^^^^^

	::

		snirftest - create a test snirf file

		usage: snirftest


snirflib
--------

Description:
^^^^^^^^^^^^

	snirflib is the library that actually does everything.   This is likely to get completely rewritten, but at the moment it works.  It has two main functions


Functions:
^^^^^^^^^^

        ::

                read_snirf(filename)


        ::

                write_snirf(name,thisdata,thisSD,thisstim,metadict,theaux=[], debug=False) (and some routines for initializing arrays).  



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

