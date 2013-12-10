PDFgui
======

Platforms
=========

:ref:`unix` -
:ref:`windows` -
:ref:`updates` -
:ref:`releases`

License
=======

By downloading and using this software you are agreeing to the following conditions.

  .. include:: PDFgui_LICENSE.txt
    :literal:

.. _unix:

Unix, Linux, Mac
================

The installation of PDFgui requires several external libraries and applications.
Consult the `README.txt <http://danse.us/trac/diffraction/browser/releases/diffpy-1.0/unix/README.txt>`_
file included with the distribution and make sure these
requirements are all in place.

The PDFgui components are registered at the Python Package Index (PyPI), therefore
the most straightforward way to install is to execute::

    easy_install diffpy.pdfgui

The easy_install command downloads, unzips and installs pdfgui together with
its requirements,
diffpy.pdffit2 and diffpy.Structure.
The program can be then started as ``pdfgui``.

The ``easy_install`` command is a part of the Python setuptools library. If it is not available,
install the "python-setuptools" package with the system package manager or use the ".tgz" archive
below, which comes with ``easy_install`` included.

If you prefer to install from local files, download the latest **diffpy-VERSION.tgz**
from the `download archive <https://googledrive.com/host/0BwRWQI5RTLvCOW9MbG9nR0JoMjQ/download/>`_,
unpack and run the enclosed ``easy_install`` script::

    tar -xzf diffpy-VERSION.tgz
    cd diffpy-VERSION
    ./easy_install diffpy.pdfgui

For more detailed installation instructions see the `PDFgui manual <../doc/pdfgui/pdfgui.html>`_.

.. _windows:

Windows
========

PDFgui is provided as a self-installing archive for Windows systems. Download the latest
**diffpy-VERSION.exe** file below, run it and follow the prompts.

The self-installing archive includes a complete installation of Python that is used to
run PDFgui. Nevertheless, PDFgui (and other DiffPy components) can be also
installed under existing Python tree. This requires Python 2.5 with several external
Python packages, namely setuptools, numpy, wxPython and matplotlib. To add PDFgui to an
existing Python tree, start Windows command prompt and run the ``easy_install`` script from
the ``Python25/Scripts`` directory::

    cd c:\Python25\Scripts
    ..\python.exe easy_install-script.py diffpy.pdfgui

This installs library files under ``Python25/Lib/site-packages`` and executable scripts for
``pdfgui`` and ``pdffit2`` under ``Python25/Scripts``.

.. _updates:

PDFgui updates
==============

Both Unix and Windows platforms can use the ``easy_install`` command to obtain the latest
updates to the code. To upgrade PDFgui, run::

    easy_install -U diffpy.pdfgui

This installs only the changed DiffPy components as they become available at the DiffPy
`package repository <https://googledrive.com/host/0BwRWQI5RTLvCOW9MbG9nR0JoMjQ/packages/>`_.
These packages are smaller and
will be updated more frequently than the complete installation archives.

.. _releases:

PDFgui Releases
===============


======================== ================== ============ ===================================
Name                     Date               Size         Description
======================== ================== ============ ===================================
`diffpy-1.0-r3067.exe`_	 2009-04-10         21.5 M        Windows self extracting installer
`diffpy-1.0-r3067.tgz`_	 2009-04-10         6.4 M         Unix tarball
======================== ================== ============ ===================================

|

.. _diffpy-1.0-r3067.exe:
   https://googledrive.com/host/0BwRWQI5RTLvCOW9MbG9nR0JoMjQ/download/diffpy-1.0-r3067.exe
.. _diffpy-1.0-r3067.tgz:
   https://googledrive.com/host/0BwRWQI5RTLvCOW9MbG9nR0JoMjQ/download/diffpy-1.0-r3067.tgz


Please, join the `community <community.html>`_ forum for tips, tricks, and feedback.
Older releases are available for download
`here <https://googledrive.com/host/0BwRWQI5RTLvCOW9MbG9nR0JoMjQ/download/>`__.
