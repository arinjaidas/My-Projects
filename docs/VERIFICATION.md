# Verification

Release date: 19 October 2026.

| Public edition | Functional checks | Complete example run |
| --- | --- | --- |
| Gold versus Equities in India | 5 | passed |
| Econometrics Research Toolkit | 5 | passed |
| Derivatives and Portfolio Risk Lab | 8 | passed |
| Digital Payments and Default Choice | 3 | passed |
| BHARAT-FX | 10 | passed |
| India External-Sector Forecasting | 10 | passed |
| ARMA Simulation with Student-t Innovations | 8 | passed |
| LSTM Time-Series and Trading Workflow | 8 | passed |
| Behavioural Responses to Economic Recessions | Public overview only | Full package prepared separately |

**Total: 57 functional checks and 8 complete public example runs.**

The review's separately prepared index-arithmetic checks are not counted as public unit tests. Eight public walkthrough notebooks read the verified result files; their cells were executed locally with Python and retain that output. A separate Jupyter-kernel execution is not claimed.

The checks include independent option-pricing comparisons, ARMA moments against statsmodels, LSTM derivatives against finite differences, temporal leakage checks, accounting identities, transaction costs and malformed-input rejection.

Verification used Python 3.12.14. Exact package versions and per-project status are in [release_verification.json](release_verification.json). The code was checked locally; hosted CI is a separate status. MATLAB companion execution, the optional downloader, excluded original archives and a full source audit of the review are outside this record.

## Hosted CI

All eight GitHub Actions jobs passed for code commit 4a4541aef69df813b8da826e0284a8e8a1d0ec13. The jobs ran the public functional checks and complete examples using Python 3.12. [View the verified run](https://github.com/arinjaidas/My-Projects/actions/runs/39230105357). Later documentation-only changes leave those tested project files unchanged.
