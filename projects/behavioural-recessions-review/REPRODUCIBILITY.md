# Reproducibility

Full Markdown review draft, six figures, four appendix datasets and a Python figure-reproduction script.

## Execute from this project directory

```bash
python -m pip install -r requirements.txt
python reproduce_figures.py --output demo_output
```

The appendix reproduction ran successfully and its numerical consistency checks passed.

Public verification used Python **3.12.14**. Package versions are recorded in [environment.json](docs/environment.json). Requirements specify compatible minimums rather than a fully locked cross-platform environment.

Randomised examples use explicit seeds. The recorded numerical output is inspectable; small library/platform differences can affect optimisation and floating-point results. SVG creation timestamps and internal element identifiers can vary between renders.

The standalone package includes a GitHub Actions workflow. It has been parsed locally; a successful hosted run is not claimed before that workflow actually executes. The CI uses Python 3.12 and read-only repository contents permission.

The review reproduction retains archived statistical vintages rather than downloading fresh observations. It was rerun successfully on 20 October 2026. Its numerical checks concern appendix arithmetic and bounds; they do not establish cross-country comparability or independently validate every literature claim.
