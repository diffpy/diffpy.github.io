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
thermal motion (peak broadening) or a change in scale due to differences
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

	PDFmorph transformation techniques (scale, smear, and stretch)
	applied sequentially to a PDF from NaCl sample


Installation
============

By downloading and using this software, you are agreeing to the conditions
specified in the software :doc:`LICENSE <pdfmorph_license>`.

PDFmorph will run on Python 3.5 or higher or on Python 2.7.
We recommend to use Anaconda Python which can be obtained from
|anaconda-download|.
PDFmorph is available from the ``diffpy`` channel of Anaconda
packages and also from `conda-forge <https://conda-forge.org>`__.
To install open a *Terminal* window (*Anaconda Command Prompt*
on Windows) and use the :program:`conda` command as follows ::

   conda install --channel=diffpy diffpy.pdfmorph

If you prefer to use ``conda-forge`` make sure it is configured as
the priority channel for Anaconda packages, which will allow you
to install without the ``--channel`` option ::

   conda config --add channels conda-forge
   conda install diffpy.pdfmorph
   
For all other Python distributions use the standard
:program:`pip` installation program::

   pip install diffpy.pdfmorph

To make sure that the installation has completed correctly,
run the following command from a *Terminal* ::

   pdfmorph --version

If all is good this should display the version of PDFmorph installed on your
machine.


PDFmorph Updates
================

The Anaconda package system makes it easy to prepare and distribute
software packages and bugfixes. To obtain the latest version of PDFmorph,
use ::

	conda update diffpy.pdfmorph

With other Python distributions, the program can be updated to the
latest version with ::

	pip --upgrade diffpy.pdfmorph

To use a development version, visit the project source repository
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

.. URL definitions below -----------------------------------------------

.. include:: ../abbreviations.txt
