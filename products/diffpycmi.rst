##########
DiffPy-CMI
##########

DiffPy-CMI is a highly flexible library of Python modules for carrying out customizable structure 
analysis tasks from diffraction data.


* :ref:`overview`
* :ref:`install`
* :ref:`getting_started`
* :ref:`documentation`
* :ref:`contribution`


.. _overview:

Contents
========

The DiffPy-CMI release includes Python and C++ modules developed by the
DiffPy team as well as external libraries necessasary for functionality.

Python modules developed by the DiffPy team
-------------------------------------------

======================      ============================================
Module                      Description
======================      ============================================
`diffpy.srfit`_             Setup and control of general fitting 
                            problems, control of constraints and 
                            restraints, complex structure refinement of
                            multiple datasets.

`diffpy.srreal`_            Python library for calculation of pair based 
                            quantities such as the pair distribution 
                            function (PDF), bond lengths, and bond 
                            valence sums from a structural model.

`diffpy.Structure`_         Handles storage of crystal structure data.  
                            Provides functions for simple crystal 
                            structure operations such as calculation of 
                            distances or angles from fractional 
                            coordinates as well as spacegroup expansion 
                            and generation of symmetry constraints on 
                            atomic positions. Provides import and export 
                            of common structure file formats.

`diffpy.utils`_             General purpose shared utilities for the 
                            diffpy libraries.

`pyobjcryst`_               Python bindings to the ObjCryst++ 
                            Object-Oriented Crystallographic
                            Library.

`libdiffpy`_                C++ library for calculation of PDF and 
                            other real-space quantities.

`libobjcryst`_              ObjCryst++ re-packaged for installation 
                            as a shared library
======================      ============================================


External libraries 
-------------------

======================      ============================================
Module                      Description
======================      ============================================
**periodictable**           Extensible periodic table of the elements 
                            with support for mass, density, and 
                            Xray/neutron scattering information.

**cxxtest**                 Testing framework for C++.

**pycifrw**                 Support for reading and writing CIF files 
                            using Python.

**sans**                    Analysis and modeling of small angle
                            scattering data.
======================      ============================================

.. _diffpy.srfit: ../doc/srfit

.. _diffpy.srreal: ../doc/srreal

.. _diffpy.Structure: ../doc/Structure

.. _diffpy.utils: ../doc/utils

.. _pyobjcryst: ../doc/pyobjcryst

.. _libdiffpy: ../doc/libdiffpy

.. _libobjcryst: https://github.com/diffpy/libobjcryst/



.. _install:

Installation
============

DiffPy-CMI is currently only available to Linux and Unix users.


By downloading and using this software you are agreeing to the conditions
specified in 
`LICENSE.txt <license.html>`_


To install DiffPy-CMI follow the steps below:

#. Install the required dependences from the command line by using a
   suitable package manager.

   For Ubuntu use ``apt-get``::

    sudo apt-get install libgsl0-dev libboost-all-dev \
        python-dev python-setuptools python-numpy \
        python-scipy python-matplotlib python-lxml ipython 

   For Fedora use ``yum``::

    FIXME - add command line 

#. Download and extract the most recent 
   `diffpy-CMI tarball <https://github.com/diffpy/pyobjcryst/releases/>`_ 
   into a directory of your choice.

#. Create a symbolic link to the diffpy-CMI directory inside the Python
   directory for user files.

   For a one-user installation determine the Python directory for user
   files, create it if it does not exist yet, and put a symbolic
   link to the diffpy-1.0.pth file inside this folder. This can be done 
   by executing the follwing code from within your diffpy-CMI directory::

    D="$(python -c 'import site; print site.USER_SITE')"
    mkdir -p "$D"
    ln -si $PWD/diffpy-1.0.pth "$D"/

   For a system-wide installation create symbolic link in the directory
   for system-wide Python packages. Again, the following code should be
   executed from within your diffpy-CMI directory::

    sudo ln -si $PWD/diffpy-1.0.pth /usr/local/lib/python2.7/dist-packages/

   Note that it is essential to use a symbolic link.  Making a copy of the
   pth file will not work.

#. Test the installation by running::

   ./runtests.sh

.. _getting_started:

Getting Started
===============

If you have successful installed the DiffPy-CMI software to your local
machine and would like to see some coding examples to get started, check
out the `cmi_exchange <https://github.com/diffpy/cmi_exchange>`_.



.. _documentation:

Documentation
=============

Documenation for modules developed by the diffpy team can generally be
found at diffpy.org/doc/moduleName or by following the links in the
tables above. 

.. _contribution:

Contribution
============

The diffpy team welcomes feedback and contribution from the community.
If you have questions, comments, or bugreports please visit the
`diffpy-users <https://groups.google.com/d/forum/diffpy-users>`_ group.

If you would like to contribute code please visit the 
`diffpy-dev <https://groups.google.com/d/forum/diffpy-dev>`_ group
The source code can be downloaded from the
`diffpy project page <https://github.com/diffpy>`__.


   ======================      ============================================
   Library                     Description
   ======================      ============================================
   **libgsl0-dev**             The GNU Scientific Library (GSL) is a 
                               collection of routines for numerical 
                               analysis.

   **libboost-all-dev**        A set of useful C++ libraries.

   **python-dev**              Header files, a static library and 
                               development tools for building 
                               Python modules.
 
   **python-setuptools**       A collection of enhancements to the Python 
                               distutils that allow developers to more 
                               easily build and distribute Python packages.

   **python-numpy**            General-purpose array-processing for 
                               efficient manipulation of large 
                               multi-dimensional arrays.

   **python-scipy**            The fundamental library for scientific 
                               computing with Python.

   **python-matplotlib**       A Python 2D plotting library which produces 
                               publication quality figures in a variety of 
                               hardcopy formats and interactive environments.

   **python-lxml**             Python library for processing XML.

   **ipython**                 An enhanced interactive Python shell.
   ======================      ============================================

