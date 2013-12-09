.. sphinxTestRun documentation master file, created by
   sphinx-quickstart on Fri Nov  8 15:28:37 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to the DiffPy project.
==============================

.. include:: abbreviations.txt

This is an open-source project to develop python software modules for diffraction 
and the study of atomic structure of materials. DiffPy is developed as part of DANSE_, 
a software construction project funded by the `National Science Foundation`_ to provide 
data analysis software tools for neutron scattering experiments that will be carried 
out at the `Spallation Neutron Source`_ at `Oak Ridge National Laboratory`_.

.. _danse: http://danse.us/

.. _national science foundation: http://www.nsf.gov/

.. _spallation neutron source: http://neutrons.ornl.gov/

.. _oak ridge national laboratory: http://www.ornl.gov/


News
====

- 2013-02-05 - initial release of the PDFgetX3 program.


Products
========

**DiffPy-CMI**

DiffPy-CMI is a highly flexible library of Python modules for carrying out customizable structure 
analysis tasks from diffraction data. `DiffPy-CMI installation instructions <downloads/diffpycmi.html>`_


**PDFgetX3**

PDFgetX3 is a command-line utility for converting X-ray powder diffraction data to 
atomic pair distribution functions (PDF). PDFgetX3 is easy to use, fast and convenient 
for automated batch processing. The interactive mode provides complete access to all 
parameters and intermediate results, as well as live-plotting feature for parameters 
tuning and visualization of their effects on the results. PDFgetX3 can be used either 
as a standalone application or as a Python library of PDF-processing functions. *The 
software is free for open academic research, but requires paid license for commercial use.*
`PDFgetX3 installation instructions <downloads/pdfgetx3.html>`_

**PDFgui** 

For users who do not have the expertise or necessity for command line analysis, PDFgui is
a convenient and easy to use graphical front end for the PDFfit2 refinement program. It is 
capable of full-profile fitting of the atomic pair distribution function (PDF) 
derived from x-ray or neutron diffraction data 
and comes with built in graphical and structure visualization capabilities.
`PDFgui installation instructions <downloads/pdfgui.html>`_

References
==========

PDFgui and PDFfit2 are intended for scientific research that will be published in 
the open literature and are free to use. Please cite the following paper in your 
scientific publications using one of these programs:

    |citeFarrowJpcm07|

For publications using the PDFgetX3 program please cite

    |citeJuhasJac13|


Acknowledgements
================


**Developers**

The active DiffPy team is Pavol Juhás, Chris Farrow, Emil Božin, Simon Billinge, Wenduo Zhou, 
Peng Tian and Timur Davis. The project was started at the Department of Physics and Astronomy, 
Michigan State University. The development team has now mostly relocated to the Department of 
Applied Physics and Applied Mathematics at Columbia University in the city of New York. The 
former members of the project while at Michigan State were Jiwu Liu and Dmitriy Bryndin.

**Funding**

This software was developed as part of the Distributed Data Analysis of Neutron Scattering 
Experiments (DANSE) project funded by the US National Science Foundation under grant DMR-0520547. 
More information on DANSE can be found at http://danse.us. The early developments of PDFfit2 were 
funded by NSF grant DMR-0304391 in the Billinge-group, and with support from Michigan State 
University. Any opinions, findings, and conclusions or recommendations expressed in this material 
are those of the author(s) and do not necessarily reflect the views of the respective funding bodies.


.. toctree::
   :hidden:

   community
   documentation
   download
   NSFnugget
