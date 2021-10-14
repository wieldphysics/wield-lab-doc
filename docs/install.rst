.. _install:
Installation
============

.. _installing:

----------------------
Installing IIRrational
----------------------

Builds to use the command line utility
--------------------------------------
For first trials, and for users not intending to use the python interface, several
prebuilt versions of the command line utility exist. These versions should just be
unzipped and run in linux/mac/win. They may not stay as up to data as the version
in the repository.

https://git.ligo.org/lee-mcculler/iirrational-pkg/wikis/home

Pip
----------------

The recommended method of installation is through `pip <http://www.pip-installer.org/>`_.
The version 2 is not currently available on PyPI, so the install should be from the compressed sources
at `<https://git.ligo.org/lee-mcculler/iirrational/tree/2.0.2>`_ (current version is |version|).

To get the compressed sources from the gitlab interface, check that the tag is on a
newest version, then click the cloud to download

.. figure:: figs/IIRrational-web.png
  :alt: Click here on the web interface

From those sources, pip can install with ::

    $ pip install IIRrational-2.0.2.tar.gz --user

or if you are not administrator, you may do a --user install::

    $ pip install IIRrational-2.0.2.tar.gz --user

note that by default, this will not install the dependencies needed for the
command line utility. Tagging the install for those dependencies requires calling
pip like::

    $ pip install IIRrational-2.0.2.tar.gz[cmd]

    $ pip install IIRrational-2.0.2.tar.gz[matlab]

----------------------
Faster dependencies
----------------------

The numpy and scipy libraries used for the fitting both use linear algebra libraries
to vectorize their operations. Some systems have the option of installing multithreaded
versions of these libraries. If during a fit you do not see the processor usage go
above 100%, then you should check if you can upgrade or install a
BLAS (basic linear algebra) library.
Numpy/scipy will fallback to using much slower and single threaded internal
implementations if these are missing.

On linux, use openblas-threads or openblas-openmp. High performance machines may
potentiall have the Intel optimized math kernel library (MKL) to use.

----------------------------------
Manual or Development installation
----------------------------------

Once you have a copy of the source, you can embed it in your Python package, or install it into your site-packages. ::

    $ python setup.py install

note that setup.py is not as intelligent as pip and will not install dependencies

to adjust the source and run from the code directory, install via::

    $ python setup.py develop

.. warning::
    Installing using setup.py develop will not expose the package to Matlab paths.
    Use the PYTHONPATH install instead if using the matlab interface.

or better yet, use pip for this and get the dependencies as well::

    $ pip install -e ./

alternatively, add to PYTHONPATH (be sure to also install or add the dependencies)::

    $ export PYTHONPATH="/path/to/IIRrational:$PYTHONPATH"

