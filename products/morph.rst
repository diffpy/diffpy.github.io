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

One dataset is designated as the "target", while the second is morphed.
Such morphs include stretching (modifying the x-axis to simulate uniform expansion),
smearing (broadening peaks via uniform convolution), and scaling. In addition
to these operations, diffpy.morph offers other morphing transformations, though
stretching, smearing, and scaling are the most commonly used. The software
automatically varies the amplitudes of the selected transformations to obtain
the best fit between the morphed and target datasets, and then plots both
datasets along with the resulting difference curve shown below.

Note that diffpy.morph works on other spectra, not just pair distribution functions (PDFs).

.. diffpy.morph will soon be included in :doc:`xPDFsuite <xPDFsuite>`, a powerful end-to-end software for X-ray PDF analysis. xPDFsuite is designed for flexible, high throughput PDF analyses and contains many features for interrogating, comparing, and modeling data as well as simply doing data reduction.

.. figure:: ../images/morph.png
	:align: center

	diffpy.morph transformation techniques applied to PDFs of IrTe\ :sub:`2` doped with
	different atomic species at different temperatures.
	The left column (a, b, and c) shows the unmorphed PDFs at 10K (blue) and 300K (red) and 
	their corresponding difference curves. The right column (d, e, and f) shows the same PDFs
	after applying the stretch, smear, and scale transformations to the 10K PDFs. No phase transition
	is observed for PDFs in d and e as the difference curves are flat (low R\ :sub:`w`). 
	However, a large difference curve (high R\ :sub:`w`) is observed in
	f, signifying a structural phase transition between 10K and 300K.


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
