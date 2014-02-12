##########
DiffPy-CMI
##########

DiffPy-CMI is a highly flexible library of Python modules for carrying out customizable structure 
analysis tasks from diffraction data.


Overview
========

The following modules are included in the DiffPy-CMI bundle:

Python modules developed by the diffpy team
-------------------------------------------

   **diffpy.srfit**
      Setup and control of general fitting problems, control of constraints 
      and restraints, complex structure refinement of multiple datasets.

   **diffpy.srreal**
      Python library for calculation of pair based quantities such as
      the pair distribution function (PDF), bond lengths, and bond valence
      sums from a structural model.

   **diffpy.Structure**
      Handles storage of crystal structure data. Provides functions for 
      simple crystal structure operations such as calculation of distances 
      or angles from fractional coordinates as well as spacegroup expansion 
      and generation of symmetry constraints on atomic positions. Provides
      import and export of common structure file formats.

   **diffpy.utils**
      General purpose shared utilities for the diffpy libraries.


C++ modules developed by the diffpy team
----------------------------------------

   **pyobjcryst**
      Python bindings to the ObjCryst++ Object-Oriented Crystallographic
      Library.

   **libdiffpy**
      C++ library fore calculation of PDF and other real-space
      quantities.

   **pyobjcryst/libobjcryst/ObjCryst**


Externally developed modules
----------------------------

   **periodictable**
      Extensible periodic table of the elements with support for mass,
      density, and Xray/neutron scattering information.

   **cxxtest**
      Testing framework for C++.

   **pycifrw**
      Support for reading and writing CIF files using Python.

   **cctbx**
      Libraries for general crystallographic applications, useful for both 
      small-molecule and macro-molecular crystallography.


   **sans/data_util**
      FIXME: add description

   **sans/sansdataloader**
      FIXME: add description

   **sans/sansmodels**
      FIXME: add description

   **sans/pr_inversion**
      FIXME: add description


Installation
============

DiffPy-CMI is currently only available to Linux and Unix users.
:ref:`cmi_linux`

License
=======

By downloading and using this software you are agreeing to the following conditions.

  .. include:: CMI_LICENSE.txt
    :literal:


.. _cmi_linux:

Unix, Linux
============

To install DiffPy-CMI follow the steps below:

#. The following libraries must be installed in order for DiffPy-CMI to
   work properly:

   **libgsl0-dev**
      The GNU Scientific Library (GSL) is a collection of routines for
      numerical analysis.

   **libboost-all-dev**
      A set of useful C++ libraries.

   **python-dev**
      Header files, a static library and development tools for building 
      Python modules.
 
   **python-setuptools**
      A collection of enhancements to the Python distutils that allow 
      developers to more easily build and distribute Python packages.

   **python-numpy**
      General-purpose array-processing for efficient manipulation of
      large multi-dimensional arrays.

   **python-scipy**
      The fundamental library for scientific computing with Python.

   **python-matplotlib**
      A Python 2D plotting library which produces publication quality 
      figures in a variety of hardcopy formats and interactive environments.

   **python-lxml**
      Python library for processing XML.

   **ipython**
      An enhanced interactive Python shell.

   All the required dependencies can be installed from the command line
   by using ``apt-get`` or a similar package manager::

    sudo apt-get install \
        libgsl0-dev \
        libboost-all-dev \
        python-dev \
        python-setuptools \
        python-numpy \
        python-scipy \
        python-matplotlib \
        python-lxml \
        ipython 

#. Download and extract the most recent 
   `diffpy-CMI tarball <http://slapper.apam.columbia.edu/diffpy-daily-builds/>`_ 
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

Documentation
=============

Documenation for modules developed by the diffpy team can generally be
found at diffpy.org/doc/moduleName or by following the links below: 

Diffpy modules
--------------

   `diffpy.srfit <../doc/srfit>`__

   `diffpy.srreal <../doc/srreal>`__

   `diffpy.Structure <../doc/Structure>`__

   `diffpy.utils <../doc/utils>`__

   `pyobjcryst <../doc/pyobjcryst>`__

   `libdiffpy <../doc/libdiffpy>`__

   pyobjcryst/libobjcryst/ObjCryst  FIXME: add documentation


External modules
----------------
FIXME: add links to documentation

   **periodictable**

   **cxxtest**

   **pycifrw**

   **cctbx**

   **sans/data_util**

   **sans/sansdataloader**

   **sans/sansmodels**

   **sans/pr_inversion**


Contribution
============

The diffpy team welcomes feedback and contribution from the community.
If you have questions, comments, or bugreports please visit the
`diffpy-users <https://groups.google.com/d/forum/diffpy-users>`_ group.

If you would like to contribute code please visit the 
`diffpy-dev <https://groups.google.com/d/forum/diffpy-dev>`_ group
The source code can be downloaded from the
`diffpy project page <https://github.com/diffpy>`__.
