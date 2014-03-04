Installation
============

Once you've downloaded the most recent DiffPy-CMI tarball follow the
steps below to install:

#. Install the required dependences from the command line by using a
   suitable package manager.

   For Ubuntu use ``apt-get``::

    sudo apt-get install libgsl0-dev libboost-all-dev \
        python-dev python-setuptools python-numpy \
        python-scipy python-matplotlib python-lxml ipython 

   For Fedora use ``yum``::

    FIXME - add command line 

   See below for a brief :ref:`dependencies`

#. Unzip the DiffPy-CMI tarball into a directory of your choice::

    tar xzf diffpy-version.tar.gz

#. Create a symbolic link to the DiffPy-CMI directory inside the Python
   directory for user files.

   For a one-user installation determine the Python directory for user
   files, create it if it does not exist yet, and put a symbolic
   link to the diffpy-1.0.pth file inside this folder. This can be done 
   by executing the follwing code from within your DiffPy-CMI directory::

    D="$(python -c 'import site; print site.USER_SITE')"
    mkdir -p "$D"
    ln -si $PWD/diffpy-1.0.pth "$D"/

   For a system-wide installation create symbolic link in the directory
   for system-wide Python packages. Again, the following code should be
   executed from within your DiffPy-CMI directory::

    sudo ln -si $PWD/diffpy-1.0.pth /usr/local/lib/python2.7/dist-packages/

   Note that it is essential to use a symbolic link.  Making a copy of the
   pth file will not work.

#. Test the installation by running::

   ./runtests.sh


.. _dependencies:

Description of Dependencies
----------------------------

* **libgsl0-dev** -  a collection of routines for numerical analysis.

* **libboost-all-dev** - a set of useful C++ libraries.

* **python-dev** - development tools for Python modules.
 
* **python-setuptools** - enhancements to the Python distutils.

* **python-numpy** - general-purpose array-processing for large multi-dimensional arrays.

* **python-scipy** - the fundamental library for scientific computing with Python.

* **python-matplotlib** - a Python 2D plotting library.

* **python-lxml** - a Python library for processing XML.

* **ipython** - an enhanced interactive Python shell.

