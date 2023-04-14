.. _quickstart:
.. _quickstart_v2:

==========
Quickstart
==========

.. currentmodule:: IIRrational
.. currentmodule:: wield.iirrational.v2

:ref:`Install wield.iirrational <install>` as a first step. Either the command line form
or the python function from pip

The calling convention of the data2filter function can be viewed fully from
:func:`data2filter`. And the convention of the :program:`IIRrationalV2fit`
command line utility is similar. Use its :option:`-h` argument for more specific
detail.

First Fit (Commandline)
--------------------------

Try fitting this `Oplev Plant Data <https://git.ligo.org/lee-mcculler/iirrational/raw/2.0.0/IIRrational_test_data/data/OplevPlant.mat>`_

.. code-block:: bash

  $ IIRrationalV2fit --mode printdata OplevPlant.mat fit.mat

Which will output the layout of the data file
::

  ap:
    ex:
      ff: [(6401,) float64 array]
      plant: [(6401,) complex128 array]
    ey:
      ff: [(6401,) float64 array]
      plant: [(6401,) complex128 array]
    ix:
      ff: [(6401,) float64 array]
      plant: [(6401,) complex128 array]
    iy:
      ff: [(6401,) float64 array]
      plant: [(6401,) complex128 array]

First, Note that this data does NOT contain any SNR data. This is too bad as it really helps the fit to know where SNR is dropping. 
V2 now has an SNR estimator, which it will use by default if SNR is missing from the data.

To access the data in this file, set the :option:`--data_group` to be `ap.ex`, `ap.ey` and so on. The Xfer function is complex and located 
in the `plant` field, and the frequency in the `ff` field for this data. Use the -Xc and -F (in the data: option group under --help output).

give it a try with

.. code-block:: bash

  $ IIRrationalV2fit OplevPlant.mat fit.mat -Xc plant -F ff --data_group ap.ey --choose shell

Which will drop into a shell, allowing you to choose the final fit order and plot across the fits.
Once you exit the shell, this will output 

::

  -L, --LIGO_foton=Sf output:
  %%%
  ZPK([
    -0.32057815257 + 1.95459336632*i; -0.32057815257 - 1.95459336632*i;
    0.677919972598 + 6.31732675415*i; 0.677919972598 - 6.31732675415*i;
    4.87276468552 + 2.65518838946*i; 4.87276468552 - 2.65518838946*i;
    -2.19332083091 + 3.25655016484*i; -2.19332083091 - 3.25655016484*i;
  ],[
    -0.146106115812 + 1.62786354165*i; -0.146106115812 - 1.62786354165*i;
    -0.10643288617 + 2.70916651619*i; -0.10643288617 - 2.70916651619*i;
    -0.0612257724613 + 1.43293384355*i; -0.0612257724613 - 1.43293384355*i;
    -0.013711116488 + 0.52486405328*i; -0.013711116488 - 0.52486405328*i;
  ], -1.13667108909e-07, "f")
  %%%

and the plots you can generate within the shell are

.. figure:: figs/oplev_fit.png
  :alt: fit 

.. figure:: figs/oplev_order.png
  :alt: fit order


You will notice that this is a pretty OK fit, but it is missing a pole-zero pair
around the first split resonance. This is likely due to the low apparent SNR there,
showing the deficiency of the SNR sample-variance estimation. It will still fit to it
if the automatic parameterization doesn't waist its high-order fitting at other frequencies.
For instance, if we run the command to specify the :option:`--relative_degree`, then the convergence
ends up better and the fit captures the split resonance on its own.

.. code-block:: bash

  $ IIRrationalV2fit OplevPlant.mat fit.mat -Xc plant -F ff --data_group ap.ey --choose shell --relative_degree -4

.. figure:: figs/oplev_fit_rel4.png

In either of these examples, the full output shows what to expect on a good fit.

full output::

  Arguments: 
    F_Hz: [(6401,) float64 array]
    SNR: None
    emphasis: None
    mode: full
    xfer: [(6401,) complex128 array]
  3W   0.00  Estimating SNR from sample variance with nearby points (SNR_est_width > 0).
            This technique work semi-OK, but could probably be much better..
            use the resulting fit to estimate the sample variance and generate
            improved SNR estimates, iterate.
  3W   0.01  5771 SNR<1 element(s) dropped (of 6401).
            Too many low SNR elements confuses the rational nonparametric fitter.
  ------------:SNR Fix Test:
  3W   0.01    The number of effective data points N=(ΣW^2)^2/(ΣW^4)=2.03e-01*len(W)
              [where W=SNR] is below the configured 'SNR_regularize_scale'=10,
              given the maximum SNR=85.1943199764. Now Finding an SNR ceiling that balances
              the ratio with max SNR.
  ------------:rational fitting:
  4P   0.02    chebychev rational fit
  3P   3.21    Initial Order: (Z=20, P=20, Z-P=0)
  3P   4.60    Fastdrop Order: (Z=20, P=20, Z-P=0)
  4P   6.00  mag fitting and phase patching
  ------------:sample variance (from magnitude):
  3A   7.50    Weight Scaling determined:  0.7386523559780868
  3A   7.50    Weight Scaling Used  0.8594488675762432
  5W   7.55  High Confidence that an unstable zero exists at 2.50336991227+2.0169543535i Hz
            Adding it to the filter. Prevent this with 'never_unstable_zeros'
  5W   7.55  High Confidence that an unstable zero exists at 0.957280382793+5.32328555221i Hz
            Adding it to the filter. Prevent this with 'never_unstable_zeros'
  ------------:Q-ranked order reduction:
  4P  19.69    order reduced annealing
  ------------:selective order reduction:
  5P  33.86    order reduced to 22, residuals=7.35e-01
  5P  68.42    order reduced to 20, residuals=6.22e-01
  5P  97.78    order reduced to 18, residuals=5.88e-01
  5P 131.58    order reduced to 18, residuals=5.47e-01
  5P 150.76    order reduced to 16, residuals=5.54e-01
  5P 169.08    order reduced to 14, residuals=5.58e-01
  5P 179.92    order reduced to 13, residuals=5.67e-01
  5P 190.15    order reduced to 13, residuals=5.42e-01
  5P 200.69    order reduced to 12, residuals=5.69e-01
  5P 216.31    order reduced to 12, residuals=5.00e-01
  5P 221.26    order reduced to 10, residuals=4.69e-01
  5P 224.36    order reduced to 9, residuals=4.55e-01
  5P 227.26    order reduced to 8, residuals=4.47e-01
  2A 231.07  Baseline fit residuals: 4.47e-01, at order 8
  ------------:successive order reduction:
  5P 235.15    order reduced to 8, residuals=5.09e-01
  5P 236.68    order reduced to 8, residuals=7.73e-01
  5P 238.56    order reduced to 8, residuals=7.90e-01
  5P 244.12    order reduced to 8, residuals=4.61e-01
  5P 246.03    order reduced to 6, residuals=6.78e+00
  5P 246.26    order reduced to 4, residuals=1.78e+01
  5P 246.44    order reduced to 2, residuals=5.02e+01
  ------------:investigations:
  2I 246.46    max(z, p)       ChiSq.
                    order    avg. res.    med. res.    max. res.
              -----------  -----------  -----------  -----------
                        2    50.1532      62.4321       907.296
                        4    17.7915      15.9627       365.109
                        6     6.78333      3.79597      107.335
                        8     0.447156     0.363065      24.6331
  plotting for -R, --plot_order=figs/oplev_order.png
  <IPython.core.display.Markdown object>
  -L, --LIGO_foton=Sf output:
  %%%
  ZPK([
    -0.32057815257 + 1.95459336632*i; -0.32057815257 - 1.95459336632*i;
    0.677919972598 + 6.31732675415*i; 0.677919972598 - 6.31732675415*i;
    4.87276468552 + 2.65518838946*i; 4.87276468552 - 2.65518838946*i;
    -2.19332083091 + 3.25655016484*i; -2.19332083091 - 3.25655016484*i;
  ],[
    -0.146106115812 + 1.62786354165*i; -0.146106115812 - 1.62786354165*i;
    -0.10643288617 + 2.70916651619*i; -0.10643288617 - 2.70916651619*i;
    -0.0612257724613 + 1.43293384355*i; -0.0612257724613 - 1.43293384355*i;
    -0.013711116488 + 0.52486405328*i; -0.013711116488 - 0.52486405328*i;
  ], -1.13667108909e-07, "f")
  %%%
  plotting for -r, --plot_fit=figs/oplev_fit.png



Python Style
------------------------


.. code-block:: python

  dataset = wield.iirrational.load('OplevPlant.mat')
  fit = wield.iirrational.v2.data2filter(
      data = dataset['ap']['ex']['plant'],
      F_Hz = dataset['ap']['ex']['ff'],
      #most of the command line arguments can go here
      #look at the docstring!
  )
  axB = results.investigate_order_plot()

  #choose the order 10 fit (or lower, if a lower one ends up better)
  results.choose(10)

  axB = results.investigate_fit_plot()
  axB.save("myfit.pdf")

  #print the foton string
  print(results.as_foton_str_ZPKsf())


Previous Versions
------------------------

.. toctree::
   :maxdepth: 1

   quickstart_v1
