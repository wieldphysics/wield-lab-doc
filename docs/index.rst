.. _index:

IIRrational: Rational Function fitting for System ID
====================================================

Release v\ |version|. (:ref:`Installation <install>`)

IIRrational is an function-fitting library for signal processing and system identification. Fitting both poles and zeros for a rational function is a nonlinear optimization problem and typical formulations require an initial guess for convergence.

This library uses a two stage approach, where the second stage is a typical gradient descent optimization, but the first is a linear technique with fast and reliable convergence, but requires gratuitous over-fitting.

Features and Conveniences
-------------------------

 - No initial guess required (most of the time)
 - Automatic order reduction (using heuristics)
 - guaranteed stable poles or zeros upon request.
 - uses SNR weight vector
 - generates fisher matrix / covariance matrix of parameterizations
 - propagates errorbars to the fit
 - S-domain for implementable filters
 - matlab support through the msurrogate package 

see :ref:`What to Expect <expect>` and :ref:`quickstart <quickstart>`


.. code-block:: python

  import IIRrational.v2
  from IIRrational.testing import IIRrational_data

  dataset = IIRrational_data('simple2')
  results = IIRrational.v2.data2filter(
      data = dataset.data,
      F_Hz = dataset.F_Hz,
      SNR  = dataset.SNR,
      F_nyquist_Hz = 16384,
  )
  axB = results.investigate_fit_plot()
  axB = results.investigate_order_plot()


.. figure:: figs/simple2_fit_example.png
  :alt: fit output

and to choose the order which should be used, the order plot will show the residuals

.. figure:: figs/simple2_fit_example_order.png
  :alt: fit order


Contents
------------

.. toctree::
   :maxdepth: 2

   install
   what_to_expect
   quickstart_v2
   quickstart_matlab
   development
   api_fitting
   advanced
   ideas


Example Output
---------------

Running the example above from the command line

.. code-block:: bash

  IIRrationalV2fit :simple2: simple2_fit.mat --plot_fit simple2_fit_example.png --plot_order simple2_fit_example_order.png --choose baseline

This uses a special file `:testdata:` to get its data. It can import data from
matlab data files, hdf5, yaml, json and CSV using the command line interface. Learn
more through help:

.. code-block:: bash

  IIRrationalV2fit -h

Which outputs on the commandline the logging and foton filter::

  Arguments: 
    F_Hz: [(1000,) float64 array]
    F_nyquist_Hz: None
    SNR: 10
    data: [(1000,) complex128 array]
    emphasis: None
    mode: full
    xfer: [(1000,) complex128 array]
  ------------:rational fitting:
  4P   0.01    chebychev rational fit
  3P   1.13    Initial Order: (Z=20, P=20, Z-P=0)
  3P   1.72    Fastdrop Order: (Z=12, P=12, Z-P=0)
  4P   2.32  mag fitting and phase patching
  ------------:sample variance (from magnitude):
  3A   3.78    Weight Scaling determined:  0.9740626973315305
  3A   3.78    Weight Scaling Used  0.9869461471283681
  ------------:Q-ranked order reduction:
  4P   5.84    order reduced annealing
  ------------:selective order reduction:
  5P  14.96    order reduced to 11, residuals=1.82e+01
  5P  20.46    order reduced to 9, residuals=1.83e+01
  5P  28.16    order reduced to 8, residuals=9.71e+00
  5P  40.08    order reduced to 7, residuals=2.17e+00
  5P  42.43    order reduced to 7, residuals=9.66e-01
  5P  43.46    order reduced to 6, residuals=9.64e-01
  2A  44.41  Baseline fit residuals: 9.64e-01, at order 6
  ------------:successive order reduction:
  5P  45.45    order reduced to 4, residuals=4.05e+00
  5P  46.23    order reduced to 4, residuals=1.02e+01
  5P  46.81    order reduced to 3, residuals=6.40e+00
  5P  47.02    order reduced to 3, residuals=3.16e+01
  5P  47.15    order reduced to 2, residuals=4.22e+01
  ------------:investigations:
  2I  47.16    max(z, p)       ChiSq.
                    order    avg. res.    med. res.    max. res.
              -----------  -----------  -----------  -----------
                        2    42.1719       39.7239      704.977
                        3     6.40444       2.9071      745.896
                        4     4.05173       1.85803     693.821
                        6     0.963768      1.28386      13.4802
  plotting for -R, --plot_order=simple2_fit_example_order.png
  -L, --LIGO_foton=Sf output:
  %%%
  ZPK([
    -0.104504805261 + 1.09613226443*i; -0.104504805261 - 1.09613226443*i;
    -0.98417325191 + 0.169021580444*i; -0.98417325191 - 0.169021580444*i;
  ],[
    -0.00956418703895 + 0.998886697835*i; -0.00956418703895 - 0.998886697835*i;
    -0.0981823932483 + 2.99528020808*i; -0.0981823932483 - 2.99528020808*i;
    -0.114527880324; -0.0817740982447;
  ], 39.3478656882, "f")
  %%%
  plotting for -r, --plot_fit=simple2_fit_example.png

You may notice that the initial residuals from the automated fit are poor. Try calling
it with the addiational argument `--relative-degree -2` and the intial guess will
have converged better.

.. note::
  when the library is installed, the command line tool may also be called via::
    python -m IIRrational.v2 [args...]




Alternatives
------------
.. TODO Links, add LIGO references

* Vectfit [matlab] https://www.sintef.no/projectweb/vectfit/
* python vectfit [python] https://github.com/PhilReinhold/vectfit_python
* fdident [matlab] https://www.mathworks.com/products/connections/product_detail/product_35570.html
* TFestimate [matlab] https://github.com/Nikhil-Mukund/TFestimate/blob/master/README.md

