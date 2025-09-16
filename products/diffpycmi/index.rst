##########
DiffPy.CMI
##########

Diffpy.cmi is designed as an extensible complex modeling infrastructure. 
Users and developers can readily integrate novel data types and constraints 
into custom workflows. While widely used for advanced analysis of structural 
data, the framework is general and can be applied to any problem where model 
parameters are refined to fit calculated quantities to data.

Diffpy.cmi is a community-driven project that supports Unix, Linux, macOS, 
and Windows platforms. It is designed to be used in Python scripts enabling 
flexible scripting and automation for advanced and reproducible workflows. 
Users are encouraged to leverage the software for their modeling needs and 
to contribute feedback, use cases, and extensions through the project 
community.


.. figure:: ../../images/diffpycmi_screenshot.png
   :align: center



Installation
============
To install ``diffpy.cmi``, create a new conda environment or activate an existing environment and install the package from the conda-forge channel.

.. code-block:: bash

    conda create -n diffpy.cmi-env
    conda install -c conda-forge diffpy.cmi
    conda activate diffpy.cmi-env

To confirm that the installation was successful, type

.. code-block:: bash

        cmi --version

The output should print the latest version.

If the above does not work, you can use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``diffpy.cmi_env`` environment, type

.. code-block:: bash

        pip install diffpy.cmi

Pack and Profile Installation
-----------------------------

Use the `cmi` command-line interface to install and manage modular optional dependencies, known as `packs`,
and to configure or execute user-defined workflows that combine multiple packs with optional post-installation steps,
known as `profiles`. To use `cmi`, you can run the following example commands:

Show available commands and options with,

.. code-block:: bash

    cmi -h

List installed and available packs and profiles,

.. code-block:: bash

    cmi pack list
    cmi profile list

Show details of a specific pack or profile,

.. code-block:: bash

    cmi pack show <pack_name>
    cmi profile show <profile_name>

Install a pack or profile (by name or path),

.. code-block:: bash

    cmi install <pack_name>
    cmi install <profile_name>
    cmi install </absolute/path/to/profile>

.. admonition:: Example installation

    For example, to install the pack for PDF modeling, type,

    .. code-block:: bash

        cmi install pdf

    To check to see if the pack was installed, type,

    .. code-block:: bash

        cmi pack list

    The output should look something like this,

    .. code-block:: bash

        Installed:
            - core
            - pdf
        Available to install:
            - plotting
            - tests
            - docs


Download examples
-----------------

To list and copy example scripts and data to your working directory, type,

.. code-block:: bash

    cmi example list
    cmi example copy <example_name>

.. admonition:: Example

    For example, to see the example scripts for PDF fitting, type,

    .. code-block:: bash

        cmi example list

    The output should look something like this,

    .. code-block:: bash

        ch03NiModelling
        ch05Fit2Phase
        ch06RefineCrystalStructureGen
        ch07StructuralPhaseTransitions
        ch08NPRefinement
        ch11ClusterXYZ

    To copy the example for bulk Ni PDF fitting, type,

    .. code-block:: bash

        cmi example copy ch03NiModelling

    This will copy the example directory ``ch03NiModelling`` to your current working directory. Within this directory exists
    the scripts and data to fit the bulk Ni PDF.

    You can then run the fitting script with,

    .. code-block:: bash

        python ch03NiModelling/solutions/diffpy-cmi/fitBulkNi.py

What next?
==========

* `Explore CMI exchange
  <https://github.com/diffpy/cmi_exchange#cmi-exchange>`__,
  our collection of example scripts and tutorials

* :doc:`Get tips on using the CMI exchange <cmi_exchange>`

* :doc:`Contribute code <contributecode>`


Tutorials
=========

* A step-by-step tutorial on using diffpy.cmi for PDF analysis is available at the documentation site for
  ``DiffPy.CMI`` -- https://www.diffpy.org/diffpy.cmi/tutorials/index.html.

* Worked examples and experimental data from the book *Atomic Pair Distribution Function Analysis: A Primer* are freely available at our
  `GitHub repository <https://github.com/Billingegroup/pdfttp_data>`_.

* ADD2019 school and conference --
  https://github.com/diffpy/add2019-diffpy-cmi.

Documentation
=============

Documentation for packages developed by the DiffPy team is available
at the links below.

* |doc-diffpy.srfit|_ -- configuration and control of data-fitting problems
* |doc-diffpy.srreal|_ -- calculators for pair distribution function, bond
  valence sums, etc.
* |doc-diffpy.structure|_ -- light-weight representation of crystal
  structures
* |doc-pyobjcryst|_ -- Python interface to ObjCryst++ crystallographic
  library
* |doc-diffpy.utils|_ -- general purpose utilities for the diffpy libraries
* |doc-libdiffpy|_ -- C++ library for calculation of PDF and other real-space
  quantities

See :ref:`DiffPy.CMI contents <contents>` for a complete list
of open-source libraries that are included in DiffPy.CMI and
their respective project pages.


Reference
=========

If you use this software in a research work which leads to publication,
we ask you to acknowledge the use of DiffPy.CMI by citing the following
paper:

* |citeJuhasAca15|

.. URL definitions below -----------------------------------------------

.. |doc-diffpy.srfit| replace:: diffpy.srfit
.. |doc-diffpy.srreal| replace:: diffpy.srreal
.. |doc-diffpy.structure| replace:: diffpy.structure
.. |doc-diffpy.utils| replace:: diffpy.utils
.. |doc-pyobjcryst| replace:: pyobjcryst
.. |doc-libdiffpy| replace:: libdiffpy

.. include:: ../../abbreviations.txt
