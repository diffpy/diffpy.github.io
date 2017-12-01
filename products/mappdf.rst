##########
mappdf
##########

The diffpy.mappdf package provides a convenient method for computing the magnetic PDF
(mappdf) from magnetic structures and performing fits to neutron total scattering
data. The mappdf is calculated by an mappdfcalculator object, which extracts the spin
positions and spin vectors from a MagStructure object that the mappdfcalculator
takes as input. The MagStructure object in turn can contain multiple MagSpecies
objects, which generate magnetic configurations based on a diffpy.Structure object
and a set of propagation vectors and basis vectors provided by the user.
Alternatively, the user can manually define a magnetic unit cell that will be used
to generate the magnetic structure, or the magnetic structure can be defined simply
as lists of spin positions and spin vectors provided by the user.



.. figure:: ../images/mappdf_screenshot.png
   :align: center

This is an early release of mappdf, and the capabilities and documentation of the
project will evolve. The DiffPy team encourages investigators to provide feedback,
suggestions, and feature requests.


Getting Started
=================

The diffpy.mappdf package requires Python 2.6 or 2.7 and the following software:

* ``NumPy`` - numerical mathematics and fast array operations for Python
* ``SciPy`` - scientific libraries for Python
* ``matplotlib`` - python plotting library
* ``diffpy.Structure`` - diffpy package for generating atomic structure
* ``diffpy.srreal`` - diffpy package for calculating real-space quantities

See the :doc:`mappdf license <mappdflicense>` for terms and conditions of use.

Installation
------------

The recommended way to install this package is through conda. For help installing conda,
please visit `https://www.continuum.io/downloads <https://www.continuum.io/downloads>`__.
Once conda is installed, you can follow the simple steps below to install diffpy.mappdf.
You will also install the full diffpy-cmi suite along the way.

*Step 1: Add the appropriate conda channels to your conda configuration.* ::

    conda config --add channels diffpy

These commands tell conda to look through these channels on the Anaconda cloud server to
find the appropriate software.

*Step 2 (recommended): Create and activate a conda environment for diffpy + diffpy.mappdf.* ::

    conda create --name diffpy python=2.7
    source activate diffpy

Note that you can name the environment anything you choose by passing it a different name
after the --name flag in the first command.

*Step 3: Install diffpy.mappdf.* ::

    conda install diffpy.mappdf

Note that this will also install the full diffpy-cmi suite if it has not already been
installed in this environment.

*Alternative option: Install from the python package index.*

If you prefer to use the python package index and have pip installed, please install the
prerequisite software and then use the command ::

    pip install diffpy.mappdf

*Alternative option: Download and install from source.*

If you prefer to install from source, you can also zip and download the entire package
from `PyPI <https://pypi.python.org/pypi/diffpy.mappdf>`__ or
`GitHub <https://github.com/benfrandsen/diffpy.magpdf>`__, then unzip the file and
execute the following command from inside the unzipped directory ::

    python setup.py install

Note that this will only work if all the dependencies are already properly installed.

Documentation
-------------
Please see `http://pythonhosted.org/diffpy.mappdf/ <http://pythonhosted.org/diffpy.mappdf/>`__
for the documentation.

What next?
============

Explore the mappdf tutorial and examples on the
`CMI Exchange <https://github.com/diffpy/cmi_exchange>`_!

.. toctree::
   :hidden:

   mappdflicense
