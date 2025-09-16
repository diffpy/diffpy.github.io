.. highlight:: bash

DiffPy.CMI installation from sources
====================================

Downloaded the most recent `DiffPy.CMI tarball
<https://github.com/diffpy/diffpy-release/releases/latest>`__
and follow the steps below.

1 Install system software
------------------------------------------------------------------------

DiffPy.CMI requires the :ref:`system software dependencies <dependencies>`
which can be installed from command line using a suitable package manager.
Here are installation commands for several supported systems.

Ubuntu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For Ubuntu or other Debian-based Linux distributions use ``apt-get``::

    sudo apt-get install \
        libgsl0-dev libboost-all-dev python-dev \
        python-setuptools python-numpy python-scipy \
        python-matplotlib python-lxml ipython \
        build-essential scons git zsh

Fedora
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``yum`` for Fedora or RedHat Linux::

    sudo yum install \
        gsl-devel boost-devel python-devel \
        python-setuptools numpy scipy  \
        python-matplotlib python-lxml \
        python-ipython-notebook \
        gcc-c++ scons git zsh

Mac OS X
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For Mac OS X the system dependencies can be installed using the
`MacPorts <https://www.macports.org>`_ software manager.  A similar
package system `Homebrew <https://brew.sh>`_ works as well, but has
been considerably less tested with DiffPy.CMI.

For best results with MacPorts follow these tips:

* We recommend to upgrade to the `latest version of OS X
  <https://www.apple.com/osx/>`_.
* Install `Xcode <https://developer.apple.com/xcode/>`_.
  If already present, we recommend to upgrade to the latest version.
* Be patient, it may take several hours to install all the dependencies
  using MacPorts.
* Installation command may fail on the first run, but usually works
  when repeated.  See MacPorts
  `FAQ <https://trac.macports.org/wiki/FAQ#buildfails>`_
  for more help.

To install system dependencies with MacPorts, use::

    sudo port install \
        python27 py27-setuptools py27-ipython py27-lxml \
        gsl boost py27-numpy py27-scipy py27-matplotlib scons git

Make sure the MacPorts versions of IPython and Python are active by
running the following commands::

    sudo port select --set ipython ipython27
    sudo port select --set python python27


**Important:** When finished installing the Mac OS X dependencies, adjust
the shell environment so that MacPorts Python is the first in the
PATH.  This can be accomplished by adding the following line to either
of ``.profile`` or ``.zshenv`` file in your HOME directory ::

    export PATH="/opt/local/bin:$PATH"


2 Install DiffPy.CMI
------------------------------------------------------------------------

Unzip the DiffPy.CMI tarball into a directory of your choice.
Execute the included :file:`install` script and follow the prompts. ::

   # replace VERSION to match the actual filename
   tar xzf diffpy_cmi-VERSION.tar.gz
   cd diffpy_cmi-VERSION
   ./install

The install process may take a while and produce a plentiful output,
but should work if all required software is in place.


3 Test
------------------------------------------------------------------------

Execute the included test script, which should report no warnings
nor errors::

   ./runtests.sh

If there are failures they are most likely due to missing software or
incorrect versions of Python or other libraries being used together.
After addressing these issues it may be necessary to recompile the
sources by running ``./install --build``.


Remarks
------------------------------------------------------------------------

The expanded diffpy_cmi directory can be renamed or moved
to a different location and the software should still work.
The only requirement is to update the :file:`diffpy_cmi.pth`
symbolic link so it points to the new location.  This can be
done by running the ``./install`` script again or by following
the steps below.

The Python interpreter must have a symbolic link pointing to the
:file:`diffpy_cmi.pth` file in one of the directories where it
looks for :file:`.pth` files.  This is normally set up by the
install script.  If that process somehow fails, the preferred
:file:`pth` directory for a single-user installation can be
found using ::

   python -c 'import site; print site.USER_SITE'

For a system-wide installation the standard :file:`pth` locations are ::

   python -c 'import site; print site.getsitepackages()'

Once the :file:`pth` directory has been established, navigate to
the base diffpy_cmi directory and create the symbolic link with ::

   ln -si $PWD/diffpy_cmi.pth /path/to/the/pth/directory/

.. note::

   It is essential to use a symbolic link.  Making a copy of the
   :file:`diffpy_cmi.pth` file will not work.

.. note::

   The installation of DiffPy.CMI is entirely contained under the
   expanded diffpy_cmi directory.  The software can be completely
   uninstalled by deleting that directory and removing the symbolic
   link.

Contacts
------------------------------------------------------------------------

If you need help with installing this software, please check discussions
or post your question to the
`diffpy-dev <https://groups.google.com/d/forum/diffpy-dev>`_
group.

----

.. _dependencies:

List of software dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
