"""Reconstruction of the documented December 2024 ARMA(1,1) exercise.

Student-t innovations are rescaled to the requested innovation variance.
The Python reference is executable; accompanying MATLAB files are unexecuted
in this release because MATLAB/Octave is unavailable in the release runtime.
"""
from pathlib import Path
import argparse
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def theoretical(c=2, phi=.95, theta=.25, innovation_variance=1.0, lags=20):
    if not np.isfinite([c, phi, theta, innovation_variance]).all() or abs(phi) >= 1 or innovation_variance <= 0:
        raise ValueError('Finite parameters, |phi| < 1 and positive innovation variance required.')
    if not isinstance(lags, int) or lags < 1:
        raise ValueError('Positive integer lag count required.')
    denominator = 1 + theta ** 2 + 2 * phi * theta
    variance = innovation_variance * denominator / (1 - phi ** 2)
    rho1 = (phi + theta) * (1 + phi * theta) / denominator
    acf = np.r_[1., rho1 * phi ** np.arange(lags)]
    return {'mean': c / (1 - phi), 'variance': variance, 'acf': acf,
            'stationary': True, 'invertible': abs(theta) < 1}


def from_innovations(innovations, c=2, phi=.95, theta=.25, initial=None):
    """Innovations include one pre-sample epsilon for the MA term."""
    eps = np.asarray(innovations, dtype=float)
    if eps.ndim != 1 or len(eps) < 2 or not np.isfinite(eps).all():
        raise ValueError('At least two finite scalar innovations required.')
    theory = theoretical(c, phi, theta)
    last = theory['mean'] if initial is None else float(initial)
    if not np.isfinite(last): raise ValueError('Initial value must be finite.')
    values = np.empty(len(eps) - 1)
    for t in range(1, len(eps)):
        last = c + phi * last + eps[t] + theta * eps[t - 1]
        values[t - 1] = last
    return values


def simulate(c=2, phi=.95, theta=.25, nu=4, n=800, burn=500, seed=20261019, innovation_variance=1):
    theoretical(c, phi, theta, innovation_variance)
    if not np.isfinite(nu) or nu <= 2:
        raise ValueError('nu must exceed two for finite innovation variance.')
    if not isinstance(n, int) or not isinstance(burn, int) or n < 3 or burn < 0:
        raise ValueError('Use n >= 3 and nonnegative integer burn-in.')
    eps = np.random.default_rng(seed).standard_t(nu, n + burn + 1)
    eps *= np.sqrt(innovation_variance * (nu - 2) / nu)
    return from_innovations(eps, c, phi, theta)[burn:]


def sample_acf(values, lags=20):
    x = np.asarray(values, dtype=float)
    if x.ndim != 1 or len(x) <= lags or not np.isfinite(x).all():
        raise ValueError('Finite one-dimensional sample longer than lag count required.')
    x = x - x.mean(); denominator = x @ x
    if denominator <= 0: raise ValueError('Sample must vary.')
    return np.array([x @ x / denominator] + [x[k:] @ x[:-k] / denominator for k in range(1, lags + 1)])


def run(output, replications=200):
    if not isinstance(replications, int) or replications < 2:
        raise ValueError('At least two replications required.')
    out = Path(output); out.mkdir(parents=True, exist_ok=True)
    params = {'c': 2, 'phi': .95, 'theta': .25, 'nu': 4, 'n': 800, 'burn': 500}
    y = simulate(**params)
    theory = theoretical()
    pd.DataFrame({'t': np.arange(1, len(y) + 1), 'synthetic_y': y}).to_csv(out / 'sample.csv', index=False)
    acf = pd.DataFrame({'lag': np.arange(21), 'sample_acf': sample_acf(y), 'theoretical_acf': theory['acf']})
    acf.to_csv(out / 'acf.csv', index=False)
    rows = []
    for r in range(replications):
        sample = simulate(**params, seed=20261019 + r)
        rows.append({'replication': r, 'sample_mean': sample.mean(), 'sample_variance': sample.var(ddof=1)})
    pd.DataFrame(rows).to_csv(out / 'monte_carlo_moments.csv', index=False)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    axes[0].plot(np.arange(1, len(y) + 1), y, color='#238c83', lw=.8)
    axes[0].axhline(theory['mean'], color='#a56b25', ls='--', label='Theoretical mean')
    axes[0].set(title='Synthetic ARMA(1,1) with t innovations', xlabel='Observation', ylabel='Simulated level')
    axes[0].legend(fontsize=8)
    acf.plot(x='lag', y=['sample_acf', 'theoretical_acf'], marker='o', markersize=3, ax=axes[1])
    axes[1].set(title='Sample and theoretical autocorrelation', ylabel='Autocorrelation')
    for ax in axes: ax.grid(alpha=.2)
    fig.tight_layout(); fig.savefig(out / 'arma_diagnostics.svg'); plt.close(fig)
    meta = {'synthetic': True, 'parameters': params, 'seed': 20261019, 'replications': replications,
            'theoretical_mean': theory['mean'], 'theoretical_variance': theory['variance'],
            'sample_mean': float(y.mean()), 'sample_variance': float(y.var(ddof=1)),
            'original_exercise_burn_in': 50,
            'public_revision': 'Uses 500 burn-in observations; MATLAB example retains the documented 50-observation setting.',
            'innovation_scaling': 'Student-t rescaled to unit variance; nu=4 has no finite fourth moment.',
            'matlab_execution': 'Not run; MATLAB/Octave is unavailable.',
            'provenance': 'New October 2026 reconstruction; original 2024 local files were not recovered.'}
    (out / 'run_metadata.json').write_text(json.dumps(meta, indent=2))
    return meta


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', default='demo_output'); p.add_argument('--replications', type=int, default=200)
    a = p.parse_args(); print(json.dumps(run(a.output, a.replications), indent=2))
