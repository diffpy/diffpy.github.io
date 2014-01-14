DiffPy-CMI
==========

Platforms
=========

DiffPy-CMI is currently only available to Linux and Unix users.
:ref:`linux`

License
=======

By downloading and using this software you are agreeing to the following conditions.

  .. include:: CMI_LICENSE.txt
    :literal:


.. _linux:

Unix, Linux
===========

To install DiffPy-CMI follow the steps below:

#. The following libraries must be installed in order for DiffPy-CMI to
   work properly:

   **libgsl0-dev**

   **libboost-all-dev**

   **python-dev**

   **python-setuptools**

   **python-numpy**

   **python-scipy**

   **python-matplotlib**

   **python-lxml**

   **ipython**

   All the required dependencies can be installed from the command line
   by using ``apt-get`` or a similar package manager::

    sudo apt-get install \
        libgsl0-dev \
        libboost-all-dev \
        python-dev \
        python-setuptools \
        python-numpy \
        python-scipy \
        python-matplotlib \
        python-lxml \
        ipython 

#. Download and extract the most recent 
   `diffpy-CMI tarball <http://slapper.apam.columbia.edu/diffpy-daily-builds/>`_ 
   into a directory of your choice.

#. Create a symbolic link to the diffpy-CMI directory inside the Python
   directory for user files.

   For a one-user installation determine the Python directory for user
   files, create it if it does not exist yet, and put a symbolic
   link to the diffpy-1.0.pth file inside this folder. This can be done 
   by executing the follwing code from within your diffpy-CMI directory::

    D="$(python -c 'import site; print site.USER_SITE')"
    mkdir -p "$D"
    ln -si $PWD/diffpy-1.0.pth "$D"/

   For a system-wide installation create symbolic link in the directory
   for system-wide Python packages. Again, the following code should be
   executed from within your diffpy-CMI directory::

    sudo ln -si $PWD/diffpy-1.0.pth /usr/local/lib/python2.7/dist-packages/

   Note that it is essential to use a symbolic link.  Making a copy of the
   pth file will not work.

#. Test the installation by running::

   ./runtests.sh
