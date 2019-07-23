##########
SrMise
##########

.. include:: ../abbreviations.txt

SrMise is the DiffPy tool for peak extraction and peak fitting from atomic
pair distribution functions (PDFs). It implements a powerful
information-theoretic multimodeling approach based on the  Akaike information
criterion (AIC) to generate and rank physically plausible sets of peaks even in
the absence of a constraining structural model.  This approach to peak
extraction is premised upon PDFs reporting accurate experimentally-determined
uncertainties, and when these are unavailable results are contingent on a
user-specified *ad hoc* uncertainty. PDFs mixing positive and negative
peaks, such as some neutron PDFs, are compatible with the SrMise peak fitting,
but not peak extraction, capability.

The software aids rapid analysis of crystalline and nanostructured
materials. Reasonable values for nearly all program parameters can be
estimated directly from the data, although the PDF baseline of non-crystalline
materials requires user judgment.  Crystalline (linear) and spherical
nanoparticle baselines are included, and SrMise also supports arbitrary
polynomial and interpolated baselines.  Other key features include peak
functions incorporating termination effects, standard uncertainty reporting, and
a framework enabling a flexible AIC-driven multimodeling analysis.  A
command-line tool exposes basic peak extraction functionality, with full
functionality available through Python scripting.


.. figure:: ../images/srmise_screenshot.png
   :align: center

This is an alpha release of SrMise, and the capabilities and documentation of
the project will evolve.  In particular, the multimodeling API is expected to
change significantly in a future version.  The DiffPy team encourages
investigators to use the software even at this early stage, and invites
feedback and suggestions.


Getting Started
=================

The diffpy.srmise package requires Python 2.6 or 2.7 and the following software:

* ``setuptools`` - software distribution tools for Python
* ``NumPy`` - numerical mathematics and fast array operations for Python
* ``SciPy`` - scientific libraries for Python
* ``matplotlib`` - python plotting library

See the :doc:`SrMise license <SrMiselicense>` for terms and conditions of use.
Detailed installation instructions for the :ref:`Windows <windows_install>`,
:ref:`Mac OS X <macosx_install>`, and :ref:`Linux <linux_install>`
platforms follow.

.. _windows_install:

Windows
-------

Several prebuilt Python distributions for Windows include all the
prerequisite software required to run SrMise, and installing one of these is the
simplest way to get started.  These distributions are usually free for
individual and/or academic use, but some also have commercial version.  Links to
executables, installation instructions, and licensing information
for some popular options are listed below.

* `Anaconda`_
* `Enthought Canopy <https://www.enthought.com/product/canopy/>`_
* `Python(x,y) <https://python-xy.github.io>`_
* `WinPython <http://winpython.github.io>`_

.. _Anaconda: anaconda-download_

Alternately, individual Windows executables for Python and the required
components can be downloaded and installed.  The official Windows releases of
Numpy and SciPy do not currently support 64-bit Python installations, so be
sure to download the 32-bit versions of these packages.

* `Python 2.6/2.7 <https://www.python.org/downloads/windows/>`_
* `NumPy <https://sourceforge.net/projects/numpy/files/NumPy/>`_
* `SciPy <https://sourceforge.net/projects/scipy/files/scipy/>`_
* `matplotlib <https://matplotlib.org/downloads.html>`_

After installing Python and the required packages, we can install SrMise.
The simplest way to obtain diffpy.srmise on Windows systems
is using ``pip`` to download and install the latest release from the
`Python Package Index <https://pypi.org>`_ (PyPI).  To do so, open a
command window by running ``cmd`` from the Start Menu's application search box
(Windows 7/8/10) or Run command (Windows Vista and earlier).  Verify that the
``pip`` program is installed by running ::

    pip --version

If this command is not found, download and run
`get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_, which will install both it
and setuptools.  For example, if your Windows user name is ``MyName`` and you
download the file to the desktop, you would run the following from the command
line: ::

    cd C:\Users\MyName\Desktop
    python get-pip.py

Finally, install the latest version of SrMise by running ::

    pip install diffpy.srmise


.. _macosx_install:

Mac OS X
--------

For Mac OS X systems with the MacPorts package manager, the required
software can be installed with ::

   sudo port install \
      python27 py27-setuptools py27-numpy py27-scipy py27-matplotlib

When installing for MacPorts, make sure the MacPorts bin directory is the first
in the system PATH and that python27 is selected as the default Python version
in MacPorts::

   sudo port select --set python python27

The simplest way to obtain diffpy.srmise on Mac OS X systems
is using ``pip`` to download and install the latest release from
`PyPI <https://pypi.org>`_. ::

   sudo pip install diffpy.srmise

If you prefer to install from sources, download them from the
`GitHub <https://github.com/diffpy/diffpy.srmise/releases>`__ or
`PyPI <https://pypi.org/project/diffpy.srmise>`__ pages for SrMise.
Uncompress them to a directory, and from that directory run ::

   sudo python setup.py install

This installs diffpy.srmise for all users in the default system location. If
administrator (root) access is not available, see the usage info from
``python setup.py install --help`` for options to install to user-writable
directories.

.. _linux_install:

Linux
-----

On Ubuntu and Debian Linux, the required software can easily be installed using
the system package manager::

   sudo apt-get install \
      python-setuptools python-numpy python-scipy python-matplotlib

Similarly, on Fedora::

    sudo yum install python-setuptools numpy scipy python-matplotlib

For other Linux distributions consult the appropriate package manager.

The simplest way to obtain diffpy.srmise on Linux systems
is using ``pip`` to download and install the latest release from
`PyPI <https://pypi.org>`_. ::

   sudo pip install diffpy.srmise

If you prefer to install from sources, download them from the
`GitHub <https://github.com/diffpy/diffpy.srmise/releases>`__ or
`PyPI <https://pypi.org/project/diffpy.srmise>`__ pages for SrMise.
Uncompress them to a directory, and from that directory run ::

   sudo python setup.py install

This installs diffpy.srmise for all users in the default system location. If
administrator (root) access is not available, see the usage info from
``python setup.py install --help`` for options to install to user-writable
directories.


What next?
============

Explore the SrMise
`tutorial <https://diffpy.github.io/diffpy.srmise/tutorial/index.html>`_!

.. toctree::
   :hidden:

   SrMiselicense
