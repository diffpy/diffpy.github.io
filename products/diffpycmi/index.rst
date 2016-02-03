##########
DiffPy-CMI
##########

DiffPy-CMI is our complex modeling framework. It is a highly flexible
library of Python modules for robust modeling of nanostructures in
crystals, nanomaterials, and amorphous materials.

The software provides functionality for storage and manipulation of
structure data and calculation of structure-based quantities, such as
PDF, SAS, bond valence sums, atom overlaps, bond lengths, and
coordinations. Most importantly the DiffPy-CMI package contains a
fitting framework for combining multiple experimental inputs in a single
optimization problem.

This is an early release of code that is under intense development, with
support for installation on Unix, Linux, and Macintosh machines.  The
scope and documentation of the project will evolve rapidly, but we want
to make the code available at the earliest possible date. Please make
use of the software and provide feedback and suggestions for
improvement, but please be patient and check back frequently for
updates.



.. figure:: ../../images/diffpycmi_screenshot.png
   :align: center



Installation
============

DiffPy-CMI is available for Linux and Mac operating systems as a
collection of packages for Anaconda Python.  It is therefore
essential to download and install `Anaconda Python
<http://www.continuum.io/downloads>`__ first.  When ready,
open a system shell (terminal), and install DiffPy-CMI from
the "diffpy" channel of Anaconda packages ::

   conda config --add channels diffpy
   conda install diffpy-cmi

.. note::

   Use of this software is subject to the conditions in
   :doc:`LICENSE.txt <license>`.

We will be publishing frequent software updates which can be
obtained later using ::

   conda update diffpy-cmi

If you don't want to use Anaconda, there is also an option to
:doc:`install from source distribution <install>`.  Note that
this method takes more time and requires some experience with
building software from sources.



* `Download <https://github.com/diffpy/diffpy-release/releases/latest>`_
  (use of this software is subject to the conditions in
  :doc:`LICENSE.txt <license>`)

* :doc:`Install <install>`



What next?
==========

* Play - visit our collection of example problems and data analysis
  scripts at `CMI exchange
  <https://github.com/diffpy/cmi_exchange#cmi-exchange>`__

* :doc:`Get tips on using the CMI exchange <cmi_exchange>`

* :doc:`Contribute code <contributecode>`


Contents and Documentation
==========================

For a list of packages bundled in the DiffPy-CMI release visit the
:ref:`contents page <contents>`.

Documentation for modules developed by the DiffPy team can generally be
found at *diffpy.org/doc/ModuleName* or by following one of the links
below.

   `diffpy.srfit`_ -
   `diffpy.srreal`_ -
   `diffpy.Structure`_ -
   `pyobjcryst`_ -
   `diffpy.utils`_ -
   `libdiffpy`_

.. _diffpy.srfit: ../../doc/srfit/

.. _diffpy.srreal: ../../doc/srreal/

.. _diffpy.Structure: ../../doc/Structure/

.. _diffpy.utils: ../../doc/utils/

.. _pyobjcryst: ../../doc/pyobjcryst/

.. _libdiffpy: ../../doc/libdiffpy/


Reference
=========

If you use this software in a research work which leads to publication,
we ask you to acknowledge the use of DiffPy-CMI by citing the following
paper:

   |citeJuhasAca15|

.. include:: ../../abbreviations.txt
