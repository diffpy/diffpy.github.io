How to Update to the Latest Sources
===================================

In order to update and build the source code you must have all the
dependencies installed. In addition to the dependencies listed in the
`installation instructions <install.html>`_, you will need ``mercurial``
and ``wget``.  On Ubuntu and Fedora, the required software can easily be
installed using the system package manager using the commands shown
below.

   For Ubuntu use ``apt-get``::

    sudo apt-get install \
        libgsl0-dev libboost-all-dev python-dev \
        python-setuptools python-numpy python-scipy \
        python-matplotlib python-lxml ipython \
        scons git zsh mercurial wget

   For Fedora use ``yum``::

    sudo yum install \
        gsl-devel boost-devel python-devel 
        python-setuptools numpy scipy  \
        python-matplotlib python-lxml \
        python-ipython-notebook scons git zsh \
        mercurial wget

The easiest way to update and recompile the latest sources is to use the
update script that was packaged with the release bundle, by typing::

    ./update.zsh

This will fetch and build the latest version of the source code. You don't
need to re-install the .pth file if you built everything in-place. 

If you only would like to recompile all existing sources codes, type::

    ./update.zsh --compile

To update and compile the source codes manually, please refer to the README 
files in the individual project pages on https://github.com/diffpy.

**Note:**

If your installed version of python came from a python distribution
other than system python (e.g. the Enthought Python Distribution) it may
not compatible with the system boost library and the build may fail. In
this case the update script will check the python version and build the
boost library from sources. However, if you choose to  build everything
manually, please keep in mind that you may need to rebuild the boost
library first. 

