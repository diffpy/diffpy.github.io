##########
|diffpycmi|
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
For the most up-to-date installation instructions, please refer to the
`diffpy.cmi README page on GitHub <https://github.com/diffpy/diffpy.cmi>`_.

Pack and Profile Installation
=============================

Diffpy.cmi is designed to be modular and extensible through the use of optional
dependencies known as `packs`. Additionally, users can define custom workflows
that combine multiple packs with optional post-installation steps, known as `profiles`.

For more information on packs and profiles please refer to the
`diffpy.cmi overview page <https://www.diffpy.org/diffpy.cmi/overview.html>`_.

For information how to install packs and profiles, please refer to the
`diffpy.cmi command-line interface page <https://www.diffpy.org/diffpy.cmi/cli-commands.html#cmi-install-command>`_.


Tutorials
=========

Many examples exist for diffpy.cmi. Using the command-line interface (CLI), these
examples can be copied directly to your computer.
For information on how to use the command-line interface to access the examples,
please refer to the 
`diffpy.cmi CLI documentation <https://www.diffpy.org/diffpy.cmi/cli-commands.html#cmi-copy-command>`_.
Additionally, here are some direct links to other tutorials and examples,

* A step-by-step tutorial on using diffpy.cmi to `fit a nickel PDF <https://www.diffpy.org/diffpy.cmi/tutorials/pdf.html#ni-pdf-fitting-tutorial>`_.

* Worked examples and experimental data from the book *Atomic Pair Distribution Function Analysis: A Primer* are freely available at our
  `GitHub repository <https://github.com/Billingegroup/pdfttp_data>`_.

* Worked examples from ADD2019 school and conference --
  https://github.com/diffpy/add2019-diffpy-cmi.

Documentation
=============

Documentation for diffpy.cmi is available at https://www.diffpy.org/diffpy.cmi. 


Reference
=========

If you use this software in a research work which leads to publication,
we ask you to acknowledge the use of diffpy.cmi by citing the following
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
