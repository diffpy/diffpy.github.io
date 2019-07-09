.. include:: ../abbreviations.txt

########
PDFmorph
########

Overview
========

.. note::
	PDFmorph is an application which makes use of the Command Line Interface. If
	you are unfamiliar with the CLI, it is recommended that you consult online
	resources and become somewhat familiar before using PDFmorph.

PDFmorph is a Python software package designed to increase the insight researchers
can obtain from measured atomic pair distribution functions (PDFs) in a model 
independent way. The program was designed to help a researcher answer the question: 
"has my material undergone a phase transition between these two measurements?"

PDFmorph makes use of several data manipulation techniques to correct for benign
effects such as thermal expansion and increased thermal motion before computing and
plotting a difference curve between two PDFs. One PDF is identified as the "target" 
PDF and the second is "morphed" by "stretching", "smearing", and "scaling". PDFmorph
will vary amplitude of morphing transformations to obtain the best fit between
morphed and target PDFs, then plot them along with the difference curve plotted
below.

There are also a few other morphing transformations in the program.

Finally, we note that PDFmorph should work on other spectra that are not PDFs, 
though it has not been extensively texted beyond the PDF.

PDFmorph will soon be included in :doc:`xPDFsuite <xPDFsuite>`, a powerful
end-to-end software for X-ray PDF analysis. PxPDFsuite is designed for flexible,
high throughput PDF analyses and contains many features for interrogating,
comparing, and modeling data as well as simply doing data reduction.

.. figure:: ../images/pdfmorph_nacl_ex.png
	:align: center

	Transformation techniques utilized by PDFmorph on an NaCl sample


Installation
============

By downloading and using this software, you are agreeing to the conditions 
specified in the :doc:`software license <pdfmorphLICENSE>`.

PDFmorph is distributed as a software package for `Anaconda Python <https://www.continuum.io>`__.
PDFmorph is available for all operating systems supported by Anaconda, namely for
32 and 64-bit Linux, Mac OS X, and 32 and 64-bit Windows.

As a prerequisite for PDFmorph installation, download and install Anaconda
from |anaconda-download|.

.. note::
	PDFmorph is a software which operates on any version of Python 3. Anaconda
	should install the latest version of Python by default, but in case you 
	already use Anaconda for a prior release of Python, create a separate
	Anaconda environment *py3x* which will provide your preferred version of 
	Python 3 (substitute x for your preferred release) instead of Python 2.7 
	or earlier. ::

		conda create --name=py3x python=3.x 
		conda activate py3x

	On Windows use just ``activate py27``. Make sure that *py3x* environment is
	activated in your shell prior to running the "install" or "update" commands
	below.

PDFmorph is available from the "conda-forge" channel of Anaconda packages. Open a 
*Terminal* window or *Anaconda Command Prompt* on Windows and install PDFmorph
using the :program:`conda` command ::

	conda config --add channels conda-forge
	conda install diffpy.pdfmorph

And it should be installed! To make sure that installation has completed correctly, 
run the following command from your relevant conda environment :: 

	pdfmorph --version

If installed correctly, this command should return PDFmorph's current version number.


PDFmorph Updates
================

The Anaconda package sustem makes it easu to prepare and distribute software
packages and bugfixes. To update the lates version of PDFmorph use ::

	conda update diffpy.pdfmorph

With other Python distributions, the program can be updated to the latest version
as follows ::

	easy_install --upgrade diffpy.pdfmorph

To use a development version, visit the project source repository at
https://github.com/diffpy/diffpy.pdfmorph and consult its README file.


Documentation/Help
==================

Alpha Version - latest
----------------------

* User manual (available in HTML and PDF) to be made available soon
* Installation instructions to come
* Tutorial files will be made available soon
* Please, join the :doc:`community forum <../community>` for tips, 
  tricks, and feedback.


References
==========

Paper on PDfmorph will be released soon.
