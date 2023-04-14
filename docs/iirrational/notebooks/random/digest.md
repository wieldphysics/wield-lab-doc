# fit_sequence version 1

> `v1.fit_sequence`

Version 1 smart fitter in wield.iirrational library. Uses SVD method with high order over-fitting, then switches to nonlinear fits with heuristics to remove poles and zeros down to a reasonable system order.

## `1` initial

### `1.1` initial_direct

> `fit_poles, fit_zeros`

initial guess without SVD technique

![](plot-1-1.png)

### `1.2` initial_poles

> `fit_poles_mod_zeros`

Performs the SVD for a rough initial guess

![](plot-1-2.png)

### `1.3` initial_zeros

> `fit_poles_mod_zeros`

Performs the SVD for a rough initial guess

![](plot-1-3.png)

### `1.4` choose zeros

> `if`

Chose the zeros SVD fitter as it had the smaller residual of 4.04e+00 vs. 4.46e+00 for the poles

### `1.5` seq_iter_3

> `RationalDiscFilter.fit_poles, RationalDiscFilter.fit_zeros`

First iterations, enforcing stabilized poles residual of 3.95e+00

![](plot-1-5.png)

### `1.6` seq_iter_4

> `RationalDiscFilter.fit_poles, RationalDiscFilter.fit_zeros`

First iterations, enforcing stabilized poles residual of 3.95e+00

![](plot-1-6.png)

### `1.7` Final

> `SVD_method`

create initial guess of fit for data, followed by several iterative fits
(see reference ???).
   * It is a linear method, finding global optimum (nonlocal). This makes it get stuck if systematics are bad. To prevent this,
it requires gratuitous overfitting to reliably get good fits.
   * It requires a nyquist frequency that is very low, near the last data point. This can cause artifacts due to phasing discontinuity near the nyquist.
   * The provided nyquist frequency is shifted up at the end, removing the real poles/zeros that are typically due to phasing discontinuity

![](plot-1-7.png)

## `2` nonlinear pre-reduce and optimize

> `MultiReprFilterZ.optimize`

initial conservative order reduction (for speed), followed by a nonlinear optimization.

![](plot-2.png)

## `3` optimize nonlinear after bandwidth limiting

> `MultiReprFilterZ.optimize`

ths limited in the nonlinear representation to half of the local average the frequency spacing.
Nonlinear optimization then applied.

![](plot-3.png)

## `4` order_reduce 1

### `4.1` duals_ID_1

> `MultiReprFilterZ.optimize`

ID Pairs for order reduction

![](plot-4-1.png)

### `4.2` duals_ID_2

> `MultiReprFilterZ.optimize`

ID Pairs for order reduction

![](plot-4-2.png)

## `5` remove_negroots

## `6` remove_weakroots

## `7` remove_negroots

## `8` remove_negroots

## `9` flip mindelay

## `10` final

> `MultiReprFilterZ.optimize`

ing nonlinear parameterizations,
TODO: describe as used

![](plot-10.png)

