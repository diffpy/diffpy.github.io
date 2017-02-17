How to Update to the Latest Sources
===================================

In order to update and build the source code you must have all the
dependencies installed. In addition to the dependencies listed in the
:doc:`installation instructions <install>`, you will need ``mercurial``
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
installation script that was packaged with the release bundle.

To update the codes::

    ./install --update[=steps]

This will perform all or selected software updates from online source repositories.
Update steps are comma separated integers or ranges such as '1,3,5-6'.

To rebuild the source code::

    ./install --build[=steps]

This will rebuild all or specified packages from sources in the src folder. In both
cases, you could use option -n to display the build steps.

.. note::

   If your installed version of Python came from a Python distribution
   other than system Python (e.g. the Enthought Python Distribution) it
   may be incompatible with the system boost library and the build may
   fail. To resolve the problem, you should rebuild the boost library
   against Enthought Python and then rebuild all DiffPy-CMI modules.
