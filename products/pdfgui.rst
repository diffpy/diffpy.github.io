.. highlight:: bash

######
PDFgui
######

Overview
========

For users who do not have the expertise or necessity for command line analysis, PDFgui is
a convenient and easy to use graphical front end for the PDFfit2 refinement program. It is
capable of full-profile fitting of the atomic pair distribution function (PDF)
derived from x-ray or neutron diffraction data
and comes with built in graphical and structure visualization capabilities.

PDFgui is also included in :doc:`xPDFsuite <xPDFsuite>`,
a powerful end-to-end software for X-ray PDF analysis.
xPDFsuite is designed for flexible,
high throughput PDF analyses and contains many features for interrogating, comparing and
modeling data as well as simply doing data reduction.


.. figure:: ../images/PDFgui_screenshot_small.png
   :align: center

   Screen-shot of PDFgui during a refinement of multiple data-sets


Installation
============

By downloading and using this software you are agreeing to the
conditions specified in the :doc:`software license <pdfguilicense>`.

PDFgui is distributed as a software package for
`Anaconda Python <https://www.continuum.io>`__.  PDFgui is available
for all operating systems supported by Anaconda, namely for 32 and
64-bit Linux, Mac OS X, and 32 and 64-bit Windows.

As a prerequisite for PDFgui installation, download and
install **Anaconda for Python 2.7** from
https://www.continuum.io/downloads.

.. note::
   If you already use Anaconda for Python 3.5, create a separate
   Anaconda environment *py27* which will provide Python 2.7
   instead of 3.5. ::

      conda create --name=py27 python=2.7
      source activate py27
      
   On Windows use just ``activate py27``.  Make sure that *py27*
   environment is activated in your shell prior to running
   the "install" or "update" commands below.

PDFgui is available from the "diffpy" channel of Anaconda packages.
Open a *Terminal* window or *Anaconda Command Prompt* on Windows
and install PDFgui using the :program:`conda` command ::

   conda config --add channels diffpy
   conda install diffpy.pdfgui

All done.  To start PDFgui enter :program:`pdfgui` command in a
Terminal or use the *DiffPy* start menu on Windows.  PDFgui can be
also started from the *Launcher* application included with Anaconda.


PDFgui updates
==============

The Anaconda package system makes it easy to prepare and distribute
software updates and bugfixes.  To update to the latest version of
PDFgui use ::

   conda update --channel=diffpy diffpy.pdfgui

To use a bleeding edge development version, visit the project source
repository at https://github.com/diffpy/diffpy.pdfgui and consult
its README file.


Old versions
============

Here is an archive of old single-file installers.  They might be
handy if there is some problem with Anaconda or if you
need to install on a machine with no Internet connection.

======================== ================== ============ =====================================
Name                     Date               Size         Description
======================== ================== ============ =====================================
`diffpy-1.0-r3067.exe`_	 2009-04-10         21.5 M        Windows self extracting installer
`diffpy-1.0-r3067.tgz`_	 2009-04-10         6.4 M         Linux and Mac tarball
======================== ================== ============ =====================================

.. _diffpy-1.0-r3067.exe:
   https://googledrive.com/host/0BwRWQI5RTLvCOW9MbG9nR0JoMjQ/download/diffpy-1.0-r3067.exe
.. _diffpy-1.0-r3067.tgz:
   https://googledrive.com/host/0BwRWQI5RTLvCOW9MbG9nR0JoMjQ/download/diffpy-1.0-r3067.tgz

Even older releases are available
`here <https://googledrive.com/host/0BwRWQI5RTLvCOW9MbG9nR0JoMjQ/download/>`__.


Documentation and help
======================

*  The user manual is available in `HTML <../doc/pdfgui/index.html>`__
   and `PDF <../doc/pdfgui/pdfgui.pdf>`__ formats.

*  Tutorial files are available from
   `pdfgui-tutorial.zip <../doc/pdfgui/pdfgui-tutorial.zip>`__.

*  Please, join the :doc:`community forum <../community>` for tips, tricks, and feedback.


.. toctree::
   :hidden:

   pdfguilicense
