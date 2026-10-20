# Verification

Verified 20 October 2026.

| Separate analytical project | Functional checks | Hosted example and checks |
| --- | --- | --- |
| [BHARAT-FX](https://github.com/arinjaidas/bharat-fx) | 10 | [passed](https://github.com/arinjaidas/bharat-fx/actions/runs/39382101501) |
| [India External-Sector Forecasting](https://github.com/arinjaidas/india-external-sector-forecasting) | 10 | [passed](https://github.com/arinjaidas/india-external-sector-forecasting/actions/runs/39382232920) |
| [Econometrics Research Toolkit](https://github.com/arinjaidas/econometrics-research-toolkit) | 5 | [passed](https://github.com/arinjaidas/econometrics-research-toolkit/actions/runs/39380706337) |
| [Gold versus Equities in India](https://github.com/arinjaidas/gold-vs-equities-india) | 5 | [passed](https://github.com/arinjaidas/gold-vs-equities-india/actions/runs/39380667412) |
| [Derivatives and Portfolio Risk Lab](https://github.com/arinjaidas/derivatives-and-portfolio-risk-lab) | 8 | [passed](https://github.com/arinjaidas/derivatives-and-portfolio-risk-lab/actions/runs/39380829351) |
| [Digital Payments and Default Choice](https://github.com/arinjaidas/digital-payments-choice-experiment) | 3 | [passed](https://github.com/arinjaidas/digital-payments-choice-experiment/actions/runs/39380971553) |
| [ARMA with Student-t Innovations](https://github.com/arinjaidas/arma-student-t-simulation) | 8 | [passed](https://github.com/arinjaidas/arma-student-t-simulation/actions/runs/39382453458) |
| [LSTM Time-Series Lab](https://github.com/arinjaidas/lstm-time-series-lab) | 8 | [passed](https://github.com/arinjaidas/lstm-time-series-lab/actions/runs/39382707193) |

**Total: 57 functional checks and eight complete standalone analytical examples.**

The complete recession-review appendix also passed in the [nine-project portfolio workflow](https://github.com/arinjaidas/My-Projects/actions/runs/39377582458), at code commit 7ac2682e5c2351b497065760996fdd3d7d2ad489. It checks two consumption-index calculations and bounds on the Greek survey percentages. Those assertions are separate from the 57 unit checks.

The review repository is an index linking the already-public full package. It does not claim an additional independent empirical study or a second numerical workflow.

Tests include independent option-price comparisons, ARMA moments against statsmodels, LSTM derivatives against finite differences, chronological leakage checks, accounting identities, transaction costs and malformed-input rejection. Walkthrough notebooks retain locally executed result-reading cells; a separate Jupyter-kernel execution is not claimed.

The tests establish implementation consistency. They do not certify future forecast accuracy, causal identification or historical investment performance. MATLAB companions and the optional downloader remain unexecuted. Original macroeconomic bundles and participant-level payment inputs are excluded.

Tested commits, run IDs and file counts appear in [standalone_verification.json](standalone_verification.json). Later documentation-only hub changes preserve the tested numerical source files.
