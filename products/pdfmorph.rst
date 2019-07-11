.. include:: ../abbreviations.txt

########
PDFmorph
########

Overview
========

.. note::
	The PDFmorph application has a Command Line Interface. If you 
	are unfamiliar with the terminal or windows command prompt, it 
	is recommended that you consult online resources and become 
	somewhat familiar before using PDFmorph.

PDFmorph is a Python software package designed to increase the insight 
researchers can obtain from measured atomic pair distribution functions 
(PDFs) in a model-independent way. The program was designed to help a 
researcher answer the question: Has my material undergone a phase 
transition between these two measurements?

PDFmorph makes use of several data manipulation techniques to correct 
for benign effects such as thermal expansion and increased thermal 
motion before computing and plotting a difference curve between two PDFs. 
One PDF is identified as the "target" PDF and the second is "morphed" 
by "stretching", "smearing", and "scaling". PDFmorph will vary amplitude 
of morphing transformations to obtain the best fit between morphed and 
target PDFs, then plot them along with the difference curve plotted
below.

There are also a few other morphing transformations in the program.

Finally, we note that PDFmorph should work on other spectra that are 
not PDFs, though it has not been extensively tested beyond the PDF.

.. PDFmorph will soon be included in :doc:`xPDFsuite <xPDFsuite>`, a powerful end-to-end software for X-ray PDF analysis. xPDFsuite is designed for flexible, high throughput PDF analyses and contains many features for interrogating, comparing, and modeling data as well as simply doing data reduction.

.. figure:: ../images/pdfmorph_nacl_ex.png
	:align: center

	Transformation techniques (scale, smear, and stretch, respectively) 
	utilized by PDFmorph applied sequentially on an NaCl sample


Installation
============

By downloading and using this software, you are agreeing to the conditions 
specified in the :doc:`software license <pdfmorph_license>`.

PDFmorph is distributed using conda. To install software using conda
you will first have to download and install ``Anaconda`` or ``mini-conda``
from `continuum <https://www.continuum.io>`__.

PDFmorph is available for all operating systems supported by Anaconda, 
namely for 32 and 64-bit Linux, Mac OS X, and 32 and 64-bit Windows.

.. note::
	We recommend that you run PDFmorph in a Python 3 conda virtual
	environment. With Anaconda or mini-conda installed on your system, 
	first create the virtual environment by typing ::
		
		conda create --name=py3 python=3

	You can give the environment any name you like but it should 
	have some Python version 3 installed. You only need to create
	the environment once, but every time you want to use PDFmorph
	you will have to activate the environment in which it is installed
	by typing ::
	
		source activate py3

	on Mac/Linux, or ::

		activate py3

	on Windows.

PDFmorph is available from the "conda-forge" channel of Anaconda packages. 
Open a *Terminal* window or *Anaconda Command Prompt* on Windows and 
install PDFmorph using the :program:`conda` command ::

	conda config --add channels conda-forge
	conda install diffpy.pdfmorph

And it should be installed! To make sure that installation has completed 
correctly, run the following command from your relevant conda environment :: 

	pdfmorph --version

This command should return PDFmorph's current version number.


PDFmorph Updates
================

The Anaconda package system makes it easy to prepare and distribute 
software packages and bugfixes. To update the latest version of PDFmorph, 
use ::

	conda update diffpy.pdfmorph

With other Python distributions, the program can be updated to the 
latest version with ::

	easy_install --upgrade diffpy.pdfmorph

To use a development version, visit the project source repository at
https://github.com/diffpy/diffpy.pdfmorph and consult its README file.


Documentation/Help
==================

0.0.1 - latest
----------------------

* User manual (available in HTML and PDF)
* Installation instructions
* `Sample PDF files <https://github.com/diffpy/diffpy.pdfmorph/tree/master/tests/testdata>`__
* Tutorial
* Please, join the :doc:`community forum <../community>` for tips, 
  tricks, and feedback.


.. References// # update upon paper resease
