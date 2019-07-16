.. include:: ../abbreviations.txt

########
PDFmorph
########

Overview
========

.. note::

	PDFmorph is currently run from the command line, which requires
	opening and typing into a terminal window or Windows command
	prompt. It is recommended that you consult online resources and
	become somewhat familiar before using PDFmorph.

PDFmorph is a Python software package designed to increase the insight
researchers can obtain from measured atomic pair distribution functions
(PDFs) in a model-independent way. The program was designed to help a
researcher answer the question: "Has my material undergone a phase
transition between these two measurements?"

PDFmorph makes use of several data manipulation techniques to correct
for benign effects such as thermal expansion (peak shift) and increased
thermal motion (peak broadening) or a cahnge in scale due to differences
in incident flux, for example. PDFmorph will do its best to correct
for these benign effects before computing and plotting a difference
curve.

One PDF (typically that collected at higher temperature) is identified
as the "target" PDF and the second is "morphed" by "stretching" (changing
the r-axis to simulate a uniform lattice expansion), "smearing"
(broadening peaks through a uniform convolution to simulate increased
thermal motion), and "scaling" (self-explanatory). PDFmorph will vary
amplitude of morphing transformations to obtain the best fit between
morphed and target PDFs, then plot them along with the difference curve
plotted below.

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

In order to take automatically take care of software dependency
downloads, we recomment you install PDFmorph using conda. To do that,
you will first have to download and install *Anaconda* or *mini-conda*
from `continuum <https://www.continuum.io>`__.

PDFmorph is available for all operating systems supported by Anaconda,
namely for 32 and 64-bit Linux, Mac OS X, and 32 and 64-bit Windows.

.. note::
	We recommend that you run PDFmorph in a Python 3 conda virtual
	environment. With Anaconda or mini-conda installed on your system,
	first create the virtual environment by typing ::
		
		conda create --name=<env_name> python=3

	You can give the environment any name you like but it should
	have some Python version 3 installed (though PDFmorph also works
	on Python 2.7). You only need to create the environment once,
	but every time you want to use PDFmorph you will have to
	reactivate the environment in which it is installed by typing ::
	
		source activate <env_name>

	on Mac/Linux, or ``activate <env_name>`` on Windows.

Once you're in your desired conda environment, you can install PDFmorph
from either the ``diffpy`` or ``conda-forge`` channels of Anaconda packages
by running opening a *Terminal* window or *Anaconda Command Prompt*
on Windows and using the :program:`conda` command ::

	conda config --add channels conda-forge
	conda install diffpy.pdfmorph

If you prefer to install from the diffpy channel, simply replace
``conda-forge`` with ``diffpy`` in the commands above.

By then it should be installed! To make sure that installation has
completed correctly, run the following command from your PDFmorph-equipped
conda environment ::

	pdfmorph --version

This command should return the version of PDFmorph you have on your
machine.


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

0.1.0 - latest
----------------------

* User manual (available in HTML and PDF)
* Installation instructions
* `Sample PDF files <https://github.com/diffpy/diffpy.pdfmorph/tree/master/tests/testdata>`__
* Tutorial
* Please, join the :doc:`community forum <../community>` for tips,
  tricks, and feedback.


.. References// # update upon paper resease

.. toctree::
    :hidden:

    pdfmorph_license
