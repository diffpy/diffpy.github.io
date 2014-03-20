Installation
============

**Note: The current release is for Unix, Linux, and Mac OS X. Windows
support will be added in a future release so please check back.**

Once you've downloaded the most recent DiffPy-CMI tarball follow the
steps below to install:

#. Install the required dependencies from the command line by using a
   suitable package manager (see below for a brief :ref:`dependencies`).

   |  **Ubuntu**

   For Ubuntu use ``apt-get``::

    sudo apt-get install \
        libgsl0-dev libboost-all-dev python-dev \
        python-setuptools python-numpy python-scipy \
        python-matplotlib python-lxml ipython \
        build-essential scons git zsh

   | **Fedora**

   For Fedora use ``yum``::

    sudo yum install \
        gsl-devel boost-devel python-devel 
        python-setuptools numpy scipy  \
        python-matplotlib python-lxml \
        python-ipython-notebook \
        gcc-c++ scons git zsh

   | **Mac OS X**

   Please follow these instructions before installing dependencies:

   * We recommend that you upgrade to the `latest version of OS X
     <https://www.apple.com/osx/>`_.
   * You must install `Xcode <https://developer.apple.com/xcode/>`_ and
     we also recommend that you upgrade to the latest version.
   * If you are not familiar with the macports package manager follow
     `these instructions <http://www.macports.org/install.php>`_ to
     install it.
   * It may take several hours to install all the dependencies using
     macports.  Please be patient.

   |

   For Mac OS X use ``macports``::

    sudo port install \
        python27 py27-setuptools py27-ipython py27-lxml \
        gsl-devel boost py27-numpy py27-scipy py27-matplotlib scons git-core

   Make sure the macports versions of ipython and python are active by
   running the following commands:: 

    sudo port select --set ipython ipython27
    sudo port select --set python python27

   Important: When finished installing the Mac OS X dependencies, adjust
   the shell environment so that MacPorts Python is the first in the
   PATH::

    export PATH=/opt/local/bin:${PATH}


#. Unzip the DiffPy-CMI tarball into a directory of your choice::

    tar xzf diffpy-version.tar.gz

#. To build the code from source execute the following command from
   within your ``diffpy-version`` directory::
    
    ./install

   **Note: for a Mac installation you must build from source.  For
   Unix/Linux it is optional.**

#. Create a symbolic link to the DiffPy-CMI directory inside the Python
   directory for user files.

   For a one-user installation determine the Python directory for user
   files, create it if it does not exist yet, and put a symbolic
   link to the diffpy-1.0.pth file inside this folder. This can be done 
   by executing the following code from within your DiffPy-CMI directory::

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

* **gsl** -  GNU Scientific Library is collection of routines for numerical analysis.

* **boost** - a set of useful C++ libraries.

* **python-dev** - development tools for Python modules.
 
* **python-setuptools** - enhancements to the Python distutils.

* **numpy** - general-purpose array-processing for large multi-dimensional arrays in Python.

* **scipy** - the fundamental library for scientific computing with Python.

* **matplotlib** - a Python 2D plotting library.

* **python-lxml** - a Python library for processing XML.

* **ipython** - an enhanced interactive Python shell.

* **scons** - a software build tool.

* **git** - a version control system.

* **zsh** - an interactive shell and powerful scripting language.

