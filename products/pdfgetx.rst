###############################
PDFgetX3, PDFgetN3 and PDFgetS3
###############################

.. include:: ../abbreviations.txt

PDFgetX3, PDFgetN3 and PDFgetS3 are command-line utilities
for automated batch processing of 1D powder diffraction data to obtain
PDFs. For an affordable GUI that allows for high throughput conversion of
multiple files with interactive graphics, please consider purchasing
:doc:`xPDFsuite <xPDFsuite>`.
A version of PDFgetX3 that processes electron diffraction data is available
by contacting NanoMegas (see `here <https://nanomegas.com/epdf/>`_ for more details)

PDFgetX3, PDFgetN3 and PDFgetS3 are easy to use, fast and convenient for automated batch processing. The interactive mode provides complete access to all
parameters and intermediate results, as well as live-plotting feature
that helps to tune conversion parameters and visualize their effect on the results.
PDFgetX3, PDFgetN3 and PDFgetS3 are distributed together with
Python library diffpy.pdfgetx, which provides the
underlying PDF-processing functions and can be
utilized in custom PDF-conversion scripts.

User PDFgetX3 for converting x-ray data, PDFgetN3 for neutron data (designed
for reactor data explicitly and not tested on neutron time-of-flight data), and
PDFgetS3 for converting correlation functions from nanoparticle assemblies in
small angle scattering data into superlattice assembly structures.

*The software is free for open academic research,
but requires paid license for commercial use.*


Download
========

.. should be easier to use redirected URLs instead of
   http://innovation.columbia.edu/technologies/m11-120

.. |m11-120| raw:: html

   <a href="https://columbia.resoluteinnovation.com/technologies/M11-120" target="_blank">
   https://columbia.resoluteinnovation.com/technologies/M11-120</a>

The PDFgetX3, PDFgetN3 and PDFgetS3 software can be obtained for free from
`Columbia Technology Ventures <https://techventures.columbia.edu>`__,
provided it will be used for open academic research
(please cite the relevant paper below).
If you plan to use the software in any other way, please contact
`<techtransfer@columbia.edu>`_ at Columbia Technology Ventures.

Use the following steps to obtain the academic license and download
the software:

1. Open new browser window at the licensing page |m11-120|.

2. Select "Request License"

3. Click on the link for the free or paid license that is appropriate
   for your needs and situation

4. Follow the link to sign in (or sign up if you don't already have a login)

5. Follow the prompts to submit the license request and wait for license confirmation email.
   Make a note of the URL so you can easily navigate back to this page.

6. Once the license is approved, the download link on the product page will become live and
   you can download the software to your local computer.

7. The download will be a zip file that contains versions of the software for all
   available Python versions and platforms.  Extract the files from the zip file, open
   ``INSTRUCTIONS.txt`` in a text editor and follow the instructions for installation.


Documentation
=============

Version 2.4.0 - Latest
----------------------

* `installation instructions <../doc/pdfgetx/2.4.0/install.html>`__
* `user manual <../doc/pdfgetx/2.4.0/index.html>`__
* `tutorial files <../doc/pdfgetx/2.4.0/pdfgetxn3-examples.zip>`__

**Added:**

* New ``transformterminationfunctions`` infrastructure to allow non-trivial termination functions
* Added ``Lorch`` termination function option
* Description of terminationfunctions to docs

**Fixed:**

* Build docs using the correct scikit-package script name
* Reapply the Sphinx dependency `m2r` to `m2r2` fix that seems to have inadvertently been lost

Previous Versions
=================
Please reach out to `<techtransfer@columbia.edu>`_ if you need one of these versions

Version 2.3.0
-------------

**Added:**

* Support for Python 3.11, 3.12, 3.13.
* Added Cython build support.
* Added `.gitattribute` for github release export.
* Use bg-mpl-stylesheets as a style for matplotlib plots.
* test for the Q-array issue
* Added instructions in wheels bundle.
* Added `pdfgetx3 --list-examples` and `pdfgetx3 --example` commands to list available examples and copy example dir into pwd.

**Changed:**

* Changed build process. Now build `*.c` sdist and c binary wheels for each platform and python version.
* Updated :code:`tuneconfig.py` to use the latest api from matplotlib.
* Renamed get_atol() to get_atol_from_rtol() in test_pdfgetter.py
* Standardized checking if a variable is an iterable.
* Removed `docs/source` directory and makefiles in installation.
* Changed `twothetazerofit.ipy` to output `.png` files instead of `.pdf`and `.svgz` files.

**Fixed:**

* Refactored code for prefer_nodisplay_backend and suppress warnings.
* Support scikit-package Level 5 standard (https://scikit-package.github.io/scikit-package/).
* Replaced :code:`setup.py` with :code:`pyproject.toml` for releases.
* Fixed example import errors `diffpy.structure` because of `Structure` deprecation.
* Fixed tutorial missing image file.

**Removed:**

* Removed deprecated support for `loadData`, `pdfgetxApplication.processFiles`, `pdfgetxApplication.clearSession`, `pdfgetxApplication.loadData`.
* Removed unused `.coveragerc`, `.gitarchive.cfg`, `.gitattributes`.
* Support for Python 2.7, and Python <= 3.10
* :code:`six`, and other Py2 legacy code\
* Removed pre-commit run in merge-to-main workflow

Version 2.2.1 - latest
----------------------

* `installation instructions <../doc/pdfgetx/2.2.1/install.html>`__
* `user manual <../doc/pdfgetx/2.2.1/index.html>`__,
  `printable manual <../doc/pdfgetx/2.2.1/PDFgetXNS3_manual.pdf>`__
* `tutorial files <../doc/pdfgetx/2.2.1/pdfgetxn3-examples.zip>`__
* `release notes <../doc/pdfgetx/2.2.1/release.html>`__

Version 2.2.0
----------------------

* `installation instructions <../doc/pdfgetx/2.2.0/install.html>`__
* `user manual <../doc/pdfgetx/2.2.0/index.html>`__,
  `printable manual <../doc/pdfgetx/2.2.0/PDFgetXNS3_manual.pdf>`__
* `tutorial files <../doc/pdfgetx/2.2.0/pdfgetxn3-examples.zip>`__
* `release notes <../doc/pdfgetx/2.2.0/release.html>`__

Version 2.1.2
----------------------

* `installation instructions <../doc/pdfgetx/2.1.2/install.html>`__
* `user manual <../doc/pdfgetx/2.1.2/index.html>`__,
  `printable manual <../doc/pdfgetx/2.1.2/PDFgetXNS3_manual.pdf>`__
* `tutorial files <../doc/pdfgetx/2.1.2/pdfgetxn3-examples.zip>`__
* `release notes <../doc/pdfgetx/2.1.2/release.html>`__


Version 2.1.1
----------------------

* `installation instructions <../doc/pdfgetx/2.1.1/install.html>`__
* `user manual <../doc/pdfgetx/2.1.1/index.html>`__,
  `printable manual <../doc/pdfgetx/2.1.1/PDFgetXNS3_manual.pdf>`__
* `tutorial files <../doc/pdfgetx/2.1.1/pdfgetxn3-examples.zip>`__
* `release notes <../doc/pdfgetx/2.1.1/release.html>`__


Version 2.1.0
----------------------

* `installation instructions <../doc/pdfgetx/2.1.0/install.html>`__
* `user manual <../doc/pdfgetx/2.1.0/index.html>`__,
  `printable manual <../doc/pdfgetx/2.1.0/PDFgetXNS3_manual.pdf>`__
* `tutorial files <../doc/pdfgetx/2.1.0/pdfgetxn3-examples.zip>`__
* `release notes <../doc/pdfgetx/2.1.0/release.html>`__


Version 2.0.0
-------------

* `installation instructions <../doc/pdfgetx/2.0.0/install.html>`__
* `user manual <../doc/pdfgetx/2.0.0/index.html>`__,
  `printable manual <../doc/pdfgetx/2.0.0/PDFgetXN3_manual.pdf>`__
* `tutorial files <../doc/pdfgetx/2.0.0/pdfgetxn3-examples.zip>`__
* `release notes <../doc/pdfgetx/2.0.0/release.html>`__


Version 1.2
-----------

* `user manual <../doc/pdfgetx/1.2/index.html>`__,
  `printable manual <../doc/pdfgetx/1.2/PDFgetX3_manual.pdf>`__
* `tutorial files <../doc/pdfgetx/1.2/pdfgetx3-examples.zip>`__
* `release notes <../doc/pdfgetx/1.2/release.html>`__


References
==========

If you use this software for a scientific research that leads
to publication, we ask that you acknowledge the use of the software
by citing the following paper in your publication:

* |citeJuhasJac13|

For publications that use this software to process neutron
diffraction data we ask you to also cite:

* |citeJuhasJac18|
