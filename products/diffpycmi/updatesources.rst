How to Update to the Latest Sources
===================================

Before you update and build the source code. Please instal the necessary
libraries. On Ubuntu Linux, the required software can easily be installed 
using the system package manager::

   sudo apt-get install \
        git libboost-all-dev libgsl0-dev mercurial python-dev \
        python-numpy python-setuptools scons wget zsh

Then the easiest way for updating and recompiling the latest sources is using 
script in the release bundle, by running (Currently the update script only 
supports Linux system)::

    ./update.zsh

This will first fetch the latest released version of source code, and then
build the all sources codes. You don't need to re-install the .pth file
if you build everything in-place. 

If you only would like to recompile all existing sources codes, run::

    ./update.zsh --compile

To update and compile the source codes manually, please refer to the project 
pages on https://github.com/diffpy and the README file in each projects.

**Note:**

If the python installed is coming from a python distribution other than system
python, (for example, Enthought Python Distribution), it may not compatible with
the system boost library and the build may fail. The update script will check the 
python version and build the boost from source if the python installed is not 
system python. And if you would like to build everything manually, please remember 
you may need to rebuild boost library. 

