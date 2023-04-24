.. highlight:: bash
.. include:: ../abbreviations.txt

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
`Anaconda Python <https://www.anaconda.com>`__.  PDFgui is available
for all operating systems supported by Anaconda, namely for
Linux, Mac OS X, and Windows.

As a prerequisite for PDFgui installation, download and install
**Miniconda** (https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links)
or Anaconda Python (https://www.anaconda.com/download).

PDFgui is available from the "conda-forge" channel of Anaconda packages.
To do so open a *Terminal* window or *Anaconda Command Prompt* and use
the :program:`conda` command as follows ::

   conda create --name=pdfgui2 python=3.9
   conda activate pdfgui2
   conda install -c conda-forge diffpy.pdfgui

PDFgui can be then started from a *Terminal* window or *Anaconda Command Prompt* by typing ::

   pdfgui

The PDFgui window will appear automatically. An alternative method on Windows is to start
PDFgui through the *Diffpy* start menu.

.. note::
   To start PDFgui from a Terminal make sure *pdfgui2* is
   the active Anaconda environment::

      conda activate pdfgui2

   Alternatively you can add the following line to your shell startup
   file :file:`.bashrc` to define an alias which will work in
   any Anaconda environment ::

      alias pdfgui="/path/to/pdfgui2/bin/pdfgui"

   where ``/path/to`` needs to be adjusted according to the output of
   ``which pdfgui`` command.


PDFgui updates
==============

The Anaconda package system makes it easy to prepare and distribute
software updates and bugfixes.  To update to the latest version of
PDFgui use ::

   conda update -c conda-forge diffpy.pdfgui

To use a bleeding edge development version, visit the project source
repository at https://github.com/diffpy/diffpy.pdfgui and consult
its README file.


Other versions
==============
v1.1.2 is the last python 2 version of PDFgui. It is no longer supported,
but may be needed to open python 2 generated `.ddp` project files. It can
be installed in a python2 anaconda environment using the commands::

   conda config --set restore_free_channel true
   conda config --add channels diffpy
   conda create --name=py27 python=2.7
   conda activate py27
   conda install -c diffpy "diffpy.pdfgui==1.1.2"

When Anaconda Python is not available, PDFgui can be installed from
sources.  The latest source package is at the `Python Package
Index <https://pypi.org/project/diffpy.pdfgui>`__ and the
prior versions are at
https://github.com/diffpy/diffpy.pdfgui/releases.  See the `README
<https://github.com/diffpy/diffpy.pdfgui#pdfgui>`__ document
for further details on installation from sources,

Finally, here are the previous single-file installers.  Although
quite outdated, they might be handy if there is some problem with
Anaconda or if one needs to install without Internet connection.

======================== ================== ============ =====================================
Name                     Date               Size         Description
======================== ================== ============ =====================================
`diffpy-1.0-r3067.exe`_	 2009-04-10         21.5 M       Windows self extracting installer
`diffpy-1.0-r3067.tgz`_	 2009-04-10         6.4 M        Linux and Mac tarball
======================== ================== ============ =====================================

.. _diffpy-1.0-r3067.exe:
   https://github.com/diffpy/diffpy.pdfgui/releases/download/svn3067/diffpy-1.0-r3067.exe
.. _diffpy-1.0-r3067.tgz:
   https://github.com/diffpy/diffpy.pdfgui/releases/download/svn3067/diffpy-1.0-r3067.tgz

MD5 check sums for these installer files are available
`here <https://github.com/diffpy/diffpy.pdfgui/releases/svn3067>`__.


Documentation and help
======================

*  The user manual is available in `HTML <../doc/pdfgui/index.html>`__
   and `PDF <../doc/pdfgui/pdfgui.pdf>`__ formats.

*  Search "PDFgui" on YouTube for some video tutorials on how to use
   PDFgui.

*  For in-depth help in using PDFgui to solve scientific problems please
   see the book "Atomic Pair Distribution Function Analysis: A primer" by
   Simon Billinge, Kirsten Jensen, and past and present Billinge group members,
   published by Oxford University Press. Data for the worked examples can
   be found here: https://github.com/Billingegroup/pdfttp_data

*  Tutorial files are available from
   `pdfgui-tutorial.zip <../doc/pdfgui/pdfgui-tutorial.zip>`__.

*  Please, join the :doc:`community forum <../community>` for tips, tricks, and feedback.


.. toctree::
   :hidden:

   pdfguilicense
