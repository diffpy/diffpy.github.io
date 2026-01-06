.. highlight:: bash
.. include:: ../abbreviations.txt

#############
diffpy.pdfgui
#############


For users who do not have the expertise or necessity for command line analysis, diffpy.pdfgui is
a convenient and easy to use graphical front end for the PDFfit2 refinement program. It is
capable of full-profile fitting of the atomic pair distribution function (PDF)
derived from x-ray or neutron diffraction data
and comes with built in graphical and structure visualization capabilities.

.. figure:: ../images/PDFgui_screenshot_small.png
   :align: center

   Screen-shot of diffpy.pdfgui during a refinement of multiple data-sets


Reference
=========

If you use this program for a scientific research that leads to publication,
we ask that you acknowledge use of the program by citing the following paper
in your publication:

   C L Farrow, P Juhas, J W Liu, D Bryndin, E S Božin,
   J Bloch, Th Proffen and S J L Billinge, `PDFfit2 and PDFgui:
   computer programs for studying nanostructure in crystals <https://doi.org/10.1088/0953-8984/19/33/335219>`_,
   J. Phys.: Condens. Matter 19 (2007) 335219.


Installation
============
For the most up-to-date installation instructions, please refer to the installation section of the
`diffpy.pdfgui README page on GitHub <https://github.com/diffpy/diffpy.pdfgui>`_.

Running pdfgui
===============

To run diffpy.pdfgui after installation, type the command::

   pdfgui

Tutorials
=========

Search "PDFgui" on YouTube for some video tutorials on how to use diffpy.pdfgui.

For in-depth help in using diffpy.pdfgui to solve scientific problems please
see the book "Atomic Pair Distribution Function Analysis: A primer" by
Simon Billinge, Kirsten Jensen, and past and present Billinge group members,
published by Oxford University Press. Data for the worked examples can
be found here: https://github.com/Billingegroup/pdfttp_data.

Please, join the :doc:`community forum <../community>` for tips, tricks, and feedback.

Documentation
=============

Documentation for diffpy.pdfgui is available at https://www.diffpy.org/diffpy.pdfgui.

Legacy versions
===============

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

.. toctree::
   :hidden:

   pdfguilicense
