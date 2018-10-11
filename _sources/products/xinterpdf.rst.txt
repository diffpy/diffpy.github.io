#########
xINTERPDF
#########

xINTERPDF is a Python GUI program for analyzing X-ray pair distribution
function (PDF) data of organic compounds collected at synchrotron and/or
laboratory X-ray sources. It uses DiffPy-CMI as a backend for simulation
of PDFs.

Currently it supports:

* The study of intermolecular interaction (e.g. hydrogen bonds) by
  subtracting out the scattering signal(s) of single molecule(s) in real
  space.
* The PDF model fit of the crystalline organic compound using the method
  proposed by Prill *et al*. (`J. Appl. Crystallogr., 48, 171-178, 2015
  <http://scripts.iucr.org/cgi-bin/paper?S1600576714026454>`__).
* The phase quantification of physical mixtures of organics.
* Generate Score/Scree plots based on Principle Component Analysis (PCA).

A video demo about installation and usage is available at
https://www.youtube.com/watch?v=lAFZ5VYEH1g. The code for xINTERPDF
is hosted on `GitHub <https://github.com/curieshicy/xINTERPDF>`__.

.. figure:: ../images/xinterpdf.png
   :align: center

This is a first release of the program (v.0.1.0). Comments and
suggestions are welcome. Please send an email to Chenyang Shi at
cs3000@columbia.edu or post your questions to `diffpy-users`_
Google Group.

Getting Started
===============

The xINTERPDF package requires Python 2.7 and the following dependency packages:

* ``NumPy`` - Numerical mathematics and fast array operations for Python
* ``SciPy`` - Scientific libraries for Python
* ``matplotlib`` - Python plotting library
* ``Scikit-Learn`` - Python machine learning library; its PCA module is called.
* ``diffpy-cmi`` - Versatile Python packages for simulation of atomic pair distribution functions
* ``Tkinter`` - Python default library for creation of graphical user interface

See the :doc:`xINTERPDF license <xinterpdflicense>` for terms and conditions of use.

Installation
------------

xINTERPDF can be installed on Linux and Mac OS machines. The recommended
way to install this package is through conda. Please visit
|anaconda-download|, and select Python 2.7 version
to download and install. Once conda is installed, you can follow the
steps below to install xINTERPDF.

*Step 1: Add the diffpy conda channel to your conda configuration.* ::

    conda config --add channels diffpy

*Step 2: Create a virtural environment and install the program there.* ::

    conda create –c curieshicy –n xinterpdf xinterpdf

This command first adds a *curieshicy* channel, then creates a virtual
environment *xinterpdf*, before finally install the *xinterpdf* program.
Note that you can name the environment anything you choose by passing it
a different name after the *-n* flag in the command.

*Step 3: Activate the virtual environment and start the program.* ::

    source activate xinterpdf
    xinterpdf

The first command starts the virtual environment and the second invokes
the main GUI window of the xINTERPDF program.

User Guide
----------

Please see `user manual <../doc/xinterpdf/xINTERPDF_User_Guide_20180615.pdf>`__
for more details.

References
----------

If you use this software in a research work which leads to publication,
we ask you to acknowledge the use of xINTERPDF by citing the following
papers:

* |citeShiJac18|
* |citeJuhasAca15|


.. include:: ../abbreviations.txt

.. toctree::
   :hidden:

   xinterpdflicense
