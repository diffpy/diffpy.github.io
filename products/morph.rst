############
diffpy.morph
############

Diffpy.morph is a Python software package designed to allow researchers
the ability to compare experimental datasets to identify structural changes.

Diffpy.morph makes use of several data manipulation techniques to correct
for benign effects such as thermal expansion (peak shift) and increased
thermal motion (peak broadening) or a change in scale due to differences
in incident flux, for example. diffpy.morph will do its best to correct
for these benign effects before computing and plotting a difference
curve.

One dataset is identified as the "target" and the second is "morphed"
by "stretching" (changing the x-axis to simulate a uniform 
expansion), "smearing" (broadening peaks through a uniform convolution),
and "scaling" (self-explanatory). diffpy.morph will vary
amplitude of morphing transformations to obtain the best fit between
morphed and target datasets, then plot them along with the difference curve
plotted below.

There are also a few other morphing transformations in the program.

Note that diffpy.morph should work on other spectra, not just pair distribution functions (PDFs).

.. diffpy.morph will soon be included in :doc:`xPDFsuite <xPDFsuite>`, a powerful end-to-end software for X-ray PDF analysis. xPDFsuite is designed for flexible, high throughput PDF analyses and contains many features for interrogating, comparing, and modeling data as well as simply doing data reduction.

.. figure:: ../images/pdfmorph.png
	:align: center

	diffpy.morph transformation techniques (scale, smear, and stretch)
	applied sequentially to a PDF from NaCl sample


Installation
============

For the most up-to-date installation instructions, please refer to the installation section of the
`diffpy.morph README page on GitHub <https://github.com/diffpy/diffpy.morph>`_.

Tutorials
=========

Tutorials on how to use diffpy.morph can be found
at the `diffpy.morph documentation <https://www.diffpy.org/diffpy.morph/>`_.


Documentation
=============

Documentation for diffpy.morph is available at https://www.diffpy.org/diffpy.morph. 
