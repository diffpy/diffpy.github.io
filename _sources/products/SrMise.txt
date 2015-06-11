##########
SrMise
##########

SrMise is the DiffPy tool for peak extraction and peak fitting from atomic
pair distribution functions (PDFs). It implements a powerful
information-theoretic multimodeling approach based on the  Akaike information
criterion (AIC) to generate and rank physically plausible sets of peaks even in
the absence of a constraining structural model.  This approach to peak
extraction is premised upon PDFs reporting accurate experimentally-determined
uncertainties, and when these are unavailable results are contingent on a
user-specified *ad hoc* uncertainty.

The software aids rapid analysis of crystalline and nanostructured
materials. Reasonable values for nearly all program parameters can be
estimated directly from the data, although the PDF baseline of non-crystalline
materials requires user judgment.  Crystalline (linear) and spherical
nanoparticles baselines are included, but SrMise also supports arbitrary
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
------------------------------------------------------------------------

The diffpy.srfit package requires Python 2.6 or 2.7 and the following software:

* ``setuptools`` - software distribution tools for Python
* ``NumPy`` - numerical mathematics and fast array operations for Python
* ``SciPy`` - scientific libraries for Python
* ``matplotlib`` - python plotting library

On Ubuntu Linux, the required software can easily be installed using
the system package manager::

   sudo apt-get install \
      python-setuptools python-numpy python-scipy python-matplotlib

For Mac OS X systems with the MacPorts package manager, the required
software can be installed with ::

   sudo port install \
      python27 py27-setuptools py27-numpy py27-scipy py27-matplotlib

When installing for MacPorts, make sure the MacPorts bin directory is the first
in the system PATH and that python27 is selected as the default Python version
in MacPorts::

   sudo port select --set python python27

For Windows systems, the easiest way to obtain ``setuptools`` if not already 
installed is downloading the ``pip`` setup script `get-pip.py 
<https://bootstrap.pypa.io/get-pip.py>`_ and running :: 

    python get-pip.py
    
It is recommended to install all other dependencies using prebuilt binaries.  
Visit http://www.scipy.org and http://www.matplotlib.org for instructions.  
Alternately, install a full Python distribution such as Python(x,y) or 
Enthought Canopy which already includes the required components. 

Installation
------------------------------------------------------------------------

The simplest way to obtain diffpy.srmise on Unix, Linux, and Mac systems
(see the :doc:`license <SrMiselicense>` for terms and conditions of use) is 
using ``pip`` to download and install the latest release from the
`Python Package Index <https://pypi.python.org>`_ (PyPI). :: 

   sudo pip install diffpy.srmise

If you prefer to install from sources, download them from the
`GitHub <https://github.com/diffpy/diffpy.srmise/releases>`_ or
`PyPI <https://pypi.python.org/pypi/diffpy.srmise>`_ pages for SrMise.  Then
run ::

   sudo python setup.py install

This installs diffpy.srmise for all users in the default system location. If 
administrator (root) access is not available, see the usage info from 
``python setup.py install --help`` for options to install to user-writable 
directories.

To install on Windows run either of the commands above omitting ``sudo``.  


What next?
----------

Explore the SrMise tutorial
`examples <http://diffpy.github.io/diffpy.srmise/examples.html>`_!

.. toctree::
   :hidden:

   SrMiselicense


