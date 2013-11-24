Download
========

PDFgetX3
========

PDFgetX3-academic can be obtained from the 
`Columbia flintbox <http://columbia.flintbox.com/public/project/22569/>`_, provided it will 
be used for open academic research. 
`Installation instructions <http://www.diffpy.org/doc/pdfgetx3/install.html>`_.

If you plan to use PDFgetX3 in any other way, please contact 
`Beth Kauderer <techtransfer@columbia.edu>`_ at Columbia Technology Ventures.

DiffPy Library
==============

`Unix, Linux, Mac <http://www.diffpy.org/download.shtml#unix>`_ - 
`Windows <http://www.diffpy.org/download.shtml#windows>`_ - 
`Updates <http://www.diffpy.org/download.shtml#updates>`_ - 
`Subversion <http://www.diffpy.org/download.shtml#subversion>`_ - 
`Releases <http://www.diffpy.org/download.shtml#releases>`_

License
=======

By downloading and using this software you are agreeing to the following conditions.



Unix, Linux, Mac
================

The installation of DiffPy requires several external libraries and applications. 
Consult the `README.txt <http://danse.us/trac/diffraction/browser/releases/diffpy-1.0/unix/README.txt>`_ 
file included with the distribution and make sure these 
requirements are all in place.

The DiffPy components are registered at the Python Package Index (PyPI), therefore 
the most straightforward way to install is to execute ``easy_install MODULE_NAME``. The 
easy_install command downloads, unzips and installs the required package together with 
its requirements, for example::

    easy_install diffpy.pdfgui
    
    
would install diffpy.pdfgui together with diffpy.pdffit2 and diffpy.Structure that are 
required for its function. The programs can be then started as ``pdfgui`` or ``pdffit2``.

The ``easy_install`` command is a part of the Python setuptools library. If it is not available, 
install the "python-setuptools" package with the system package manager or use the ".tgz" archive 
below, which comes with ``easy_install`` included.

If you prefer to install from local files, download the latest **diffpy-VERSION.tgz** archive 
list below, unpack and run the enclosed ``easy_install`` script::

    tar -xzf diffpy-VERSION.tgz
    cd diffpy-VERSION
    ./easy_install diffpy.pdfgui
    
For more detailed installation instructions see PDFgui manual.


Windows
========

DiffPy is provided as self-installing archive for Windows systems. Download the latest 
**diffpy-VERSION.exe** file below, run it and follow the prompts.

The self-installing archive includes a complete installation of Python that is used to 
run PDFgui and PDFfit2. Nevertheless, PDFgui (and other DiffPy components) can be also 
installed under existing Python tree. This requires Python 2.5 with several external 
Python packages, namely setuptools, numpy, wxPython and matplotlib. To add PDFgui to an 
existing Python tree, start Windows command prompt and run the ``easy_install`` script from 
the ``Python25/Scripts`` directory::

    cd c:\Python25\Scripts
    ..\python.exe easy_install-script.py diffpy.pdfgui
    
This installs library files under ``Python25/Lib/site-packages`` and executable scripts for 
``pdfgui`` and ``pdffit2`` under ``Python25/Scripts``.


DiffPy updates
==============

Both Unix and Windows platforms can use the ``easy_install`` command to obtain the latest 
updates to the code. For example, to upgrade PDFgui, run::

    easy_install -U diffpy.pdfgui
    
This installs only the changed DiffPy components as they become available at the DiffPy 
`package repository <http://www.diffpy.org/packages/>`_. These packages are smaller and 
will be updated more frequently than the complete installation archives.

Subversion repository
=====================

The latest development sources of DiffPy packages are available in a public subversion code 
repository. To install the latest development version of a DiffPy component called ``MODULE_NAME``, run::

    easy_install -U svn://svn@danse.us/diffraction/diffraction/MODULE_NAME/trunk
    
Another option is to install in a development mode, which is more convenient for debugging 
and experimenting with the code. This can be done as::

    svn checkout svn://svn@danse.us/diffraction/diffraction/MODULE_NAME
    cd MODULE_NAME/trunk
    python setup.py develop
    
The DiffPy subversion repository can be browsed online `here <http://danse.us/trac/diffraction/browser/>`_.

