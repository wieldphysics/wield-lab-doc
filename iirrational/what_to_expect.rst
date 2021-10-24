.. _expect:

==============
What to expect
==============

wavestate.iirrational works in two stages:
  * an initial (rational) stage which develops an initial fit without requiring a guess from the user
  * a fit optimizer, combined with order reduction trials

Fitting without an initial guess is an intrinsically ill-posed problem, so the
success rate of the initial guess system is not 100%. That aspect is a work in progress.
The initial stage also generates fits of excessive order, which requires the optimize/reduce step to be
both good and reasonably efficient.

On the other hand, the optimizer works quite well and provides strong guarantees
about the roots in the fit.
  * Starting roots in the optimizer will cross the imaginary line or
    otherwise change from being stable roots to unstable roots
  * Roots will not have excessively low bandwidth. Roots cannot have bandwidths substantially
    more narrow than the spacing between data points.
  * The rolloff or asymptotic response is guaranteed to be within 2x the last
    data point (configurable). This ensures that the fits aren't good at low
    frequencies only to be poorly behaved at high frequencies.

For this reason, the version 2.0.0 has a "mode" flag to switch between how automated
the fitting should be:
  * full: uses initial guess plus reduce
  * reduce: only the fitting and reduce, using initial poles/zeros given as arguments.
  * fit: only optimize the given roots 
  * rational: only attempt the high-order initial guess

So even if the guessing system is failing for a fit, try giving an initial guess
