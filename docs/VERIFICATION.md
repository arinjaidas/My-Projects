# Verification

Release date: 20 October 2026.

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
| Behavioural Responses to Economic Recessions | Separate appendix arithmetic and percentage bounds | passed |

**Total: 57 functional checks, 8 complete analytical/model examples and 1 full review-appendix reproduction.**

The review checks two independently calculated consumption indices against the archived reported indices and verifies the bounds of the Greek survey percentages. Those assertions are not included in the 57 unit-check count. Nine public walkthrough notebooks read verified result files; their cells were executed locally with Python and retain that output. A separate Jupyter-kernel execution is not claimed.

The checks include independent option-pricing comparisons, ARMA moments against statsmodels, LSTM derivatives against finite differences, temporal leakage checks, accounting identities, transaction costs and malformed-input rejection.

Verification used Python 3.12.14. Exact package versions and per-project status are in [release_verification.json](release_verification.json). The code was checked locally; hosted CI is a separate status. MATLAB companion execution, the optional downloader, excluded original archives and a full source audit of the review are outside this record.

## Hosted CI

All eight GitHub Actions jobs passed for code commit 4a4541aef69df813b8da826e0284a8e8a1d0ec13. The jobs ran the public functional checks and complete examples using Python 3.12. [View the verified run](https://github.com/arinjaidas/My-Projects/actions/runs/39230105357). Later documentation-only changes leave those tested project files unchanged.

The recession reproduction was rerun successfully on 20 October 2026. The maximum absolute consumption-index differences were 0.00357317 for the US and 0.00476848 for India, both within the 0.015-point rounding tolerance. This checks appendix arithmetic and does not independently validate every literature claim. The new workflow includes the review as its ninth job; its hosted result is recorded only after completion.
