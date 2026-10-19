# Methods

## Process and moments

The recurrence is `y_t = c + phi*y_(t-1) + epsilon_t + theta*epsilon_(t-1)`. For absolute phi below one, the unconditional mean is `c/(1-phi)`. With innovation variance s², the process variance is `s²*(1+theta²+2*phi*theta)/(1-phi²)`.

Lag-one autocorrelation is `(phi+theta)*(1+phi*theta)/(1+theta²+2*phi*theta)`. At later lags it decays geometrically as `phi^(k-1)*rho_1`. These formulas are checked against the independently implemented statsmodels ArmaProcess.

## Heavy tails and initialisation

A standard Student-t draw has variance nu/(nu-2) when nu exceeds two. Multiplying by `sqrt(s²*(nu-2)/nu)` gives the requested innovation variance. At nu=4 the fourth moment is infinite, so sample-variance dispersion should not be interpreted with routine finite-fourth-moment approximations.

The simulator starts at the theoretical mean and includes a pre-sample innovation for the moving-average term. Python uses 500 discarded observations to reduce initialisation effects for the highly persistent default phi=0.95. The companion MATLAB example retains the historically documented 50-observation setting. Different generators and initialisation conventions prevent an assumption of bitwise cross-language equality.
