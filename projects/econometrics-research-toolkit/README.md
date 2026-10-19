# Automated Econometrics and Research Toolkit

Reusable Python workflows for empirical-research preparation, OLS specification comparisons, diagnostics and reporting.

## Provenance

The original 2023-24 research-internship work supported historical numeracy and health-outcome research at the University of Tübingen under Prof. Jörg Baten. It involved data preparation, OLS specifications, predictor-combination searches, VIF diagnostics, plots and text/CSV exports.

Original local source files were not recoverable. This is a new October 2026 public reconstruction of the reusable workflow. Institutional data and unpublished collaborative findings are not included.

## Public implementation

- Explicit numeric validation and common complete-case samples across specifications.
- Required base predictors and bounded control-combination searches.
- OLS with HC3 standard errors, adjusted R-squared, AIC/BIC and VIF.
- Transparent reporting of rank-deficient specifications.
- Coefficient tables, model summaries and fitted-versus-observed plots.

The common complete-case approach is a deliberate revision of the mean-imputation workflow described in the historical project.

![Synthetic research example](demo_output/fit.svg)

## Run

```bash
python -m pip install -r requirements.txt
python -m unittest -v test_toolkit.py
python toolkit.py --demo --output demo_output
```

The demonstration compares fifteen specifications on 388 complete synthetic observations. For another permitted dataset, use --csv, --outcome, --base and --controls; see --help.

## Interpretation

Specification searches are exploratory. Good in-sample fit does not establish predictive performance or causality. HC3 standard errors do not correct for multiple-model selection. Synthetic health-like variables are demonstrations, not actual research findings.

## Attribution

Portfolio owner: Arinjai Das. Original research context: University of Tübingen economic history internship and the relevant research team. The reconstruction demonstrates analytical tooling rather than claiming sole ownership of collaborative empirical research.
