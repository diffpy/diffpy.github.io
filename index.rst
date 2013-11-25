.. sphinxTestRun documentation master file, created by
   sphinx-quickstart on Fri Nov  8 15:28:37 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to the DiffPy project.
==============================

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

**PDFgetX3**

PDFgetX3 is a command-line utility for converting X-ray powder diffraction data to 
atomic pair distribution functions (PDF). PDFgetX3 is easy to use, fast and convenient 
for automated batch processing. The interactive mode provides complete access to all 
parameters and intermediate results, as well as live-plotting feature for parameters 
tuning and visualization of their effects on the results. PDFgetX3 can be used either 
as a standalone application or as a Python library of PDF-processing functions. *The 
software is free for open academic research, but requires paid license for commercial use.*

**DiffPy library**

A library of Python modules for carrying out structure analysis tasks from diffraction data. 
The modules are at different stages of development and some are not yet ready for usage by 
non-experts. Nevertheless, the components listed below should be stable enough and hopefully 
useful to a broader non-expert community.

**DiffPy components**

- **PDFgui** - a program for full-profile fitting of the atomic pair distribution function (PDF) 
  derived from x-ray or neutron diffraction data. This is a graphical front end for the 
  PDFfit2 refinement program, with built in graphical and structure visualization capabilities.
- **PDFfit2** - the structure refinement engine for fitting structural models to experimentally 
  derived PDFs. It is used as calculation engine for PDFgui, but can be used separately 
  in simple Python scripts or as a command-line program.
- **Structure** - simple storage and manipulation of crystal structure data. Supports reading 
  and writing in several structure formats, coordinate transformations, symmetry expansion 
  and generation of symmetry constraints.


References
==========

PDFgui and PDFfit2 are intended for scientific research that will be published in 
the open literature and are free to use. Please cite the following paper in your 
scientific publications using one of these programs:

    C. L. Farrow, P. Juhás, J. W. Liu, D. Bryndin, E. S. Božin, J. Bloch, Th. Proffen and 
    S. J. L. Billinge, `PDFfit2 and PDFgui: computer programs for studying nanostructure in 
    crystals <http://iopscience.iop.org/0953-8984/19/33/335219/>`_, *J. Phys.: Condens. 
    Mat.* **19**, 335219 (2007) |downloadImageFarrow|
 
.. |downloadImageFarrow| image:: pdficon_small.png
   :target: _static/Farrow-jpcm-2007.pdf

For publications using the PDFgetX3 program please cite

    P. Juhás and T. Davis, C. L. Farrow, S. J. L. Billinge, `PDFgetX3: A rapid and highly 
    automatable program for processing powder diffraction data into total scattering pair 
    distribution functions <http://scripts.iucr.org/cgi-bin/paper?S0021889813005190>`_, 
    *J. Appl. Crystallogr.* **46**, 560-566 (2013) |downloadImageJuhas| 

.. |downloadImageJuhas| image:: pdficon_small.png
   :target: _static/Juhas-jac-2013.pdf



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
