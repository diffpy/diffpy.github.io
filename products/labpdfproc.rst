######################
diffpy.labpdfproc
######################


Tools for processing x-ray powder diffraction data from laboratory 
sources.

PDFgetX3 has revolutionized how pair distribution function (PDF) methods 
can be applied to solve 
nanostructure problems. However, the program was designed for use with 
Rapid Acquisition PDF (RAPDF) data from synchrotron sources. A key 
approximation inherent in the use of PDFgetX3 for RAPDF data is that 
absorption effects are negligible. This is typically not the case for 
laboratory x-ray diffractometers, where absorption effects can be 
significant.

This app is designed to preprocess data from laboratory x-ray 
diffractometers before using PDFgetX3 to obtain PDFs. The app currently 
carries out an absorption correction assuming a parallel beam capillary 
geometry which is the most common geometry for lab PDF measurements.

Installation
============

For the most up-to-date installation instructions, please refer to the installation section of the
`diffpy.labpdfproc README page on GitHub <https://github.com/diffpy/diffpy.labpdfproc>`_.

Running labpdfproc
======================

To run diffpy.labpdfproc after installation, type the command::
 
   labpdfproc

Tutorials
=========
Tutorials on how to use diffpy.labpdfproc can be found
at the `diffpy.labpdfproc documentation <https://www.diffpy.org/diffpy.labpdfproc/>`_.

Documentation
=============

Documentation for diffpy.labpdfproc is available at https://www.diffpy.org/diffpy.labpdfproc.