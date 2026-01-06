#############
diffpy.mpdf
#############

.. include:: ../abbreviations.txt

The diffpy.mpdf package provides a convenient method for computing the magnetic PDF
(mPDF) from magnetic structures and performing fits to neutron total scattering
data. The mPDF is calculated by an MPDFcalculator object, which extracts the spin
positions and spin vectors from a MagStructure object that the MPDFcalculator
takes as input. The MagStructure object in turn can contain multiple MagSpecies
objects, which generate magnetic configurations based on a diffpy.structure object
and a set of propagation vectors and basis vectors provided by the user.
Alternatively, the user can manually define a magnetic unit cell that will be used
to generate the magnetic structure, or the magnetic structure can be defined simply
as lists of spin positions and spin vectors provided by the user.



.. figure:: ../images/mpdf_screenshot.png
   :align: center

   Example usage of diffpy.mpdf


Reference
=========

If you use diffpy.mpdf in scientific research, please acknowledge it by citing:

   Frandsen et al., "diffpy.mpdf: open-source software for magnetic pair distribution function analysis", 
   J. Appl. Cryst. (2022) 55, 1377-1382. https://doi.org/10.1107/S1600576722007257

Installation
============

For the most up-to-date installation instructions, please refer to the
`diffpy.mpdf README on GitHub <https://github.com/FrandsenGroup/diffpy.mpdf>`_.

Tutorials
=========

For tutorials on how to use diffpy.mpdf, please visit: https://github.com/FrandsenGroup/mPDF-tutorial.

Documentation
=============

Full documentation for diffpy.mpdf is available at:  
`https://frandsengroup.github.io/diffpy.mpdf/index.html <https://frandsengroup.github.io/diffpy.mpdf/index.html>`_


