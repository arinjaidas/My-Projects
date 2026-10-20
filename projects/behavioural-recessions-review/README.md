![Behavioural Responses to Economic Recessions](assets/header.svg)

# Behavioural Responses to Economic Recessions

Narrative research review of saving, consumption and risk-taking across recessions, with the full draft and reproducible descriptive figures.

**Research question:** Why can stronger precautionary motives produce additional saving for some households and dissaving or essential-spending cuts for others?

**Public edition:** Full Markdown review draft, six figures, four appendix datasets and a Python figure-reproduction script.

The appendix reproduction ran successfully and its numerical consistency checks passed.

Read the [complete review draft](paper/REVIEW_DRAFT.md), including its 35 references and six archived figures.

## What you can inspect

- Integrate precautionary-saving, liquidity, reference-dependence and experience-effect mechanisms.
- Compare cases while preserving institutional and measurement differences.
- Retain a complete narrative-review draft with 35 source references.
- Reproduce the archived appendix's aggregate data figures and check reported index arithmetic.
- Separate descriptive evidence from causal identification and new empirical estimation.

## Results preview

These are archived published aggregate observations retained from the review appendix, with their original source vintages.

![Behavioural Responses to Economic Recessions results preview](demo_output/review_appendix.svg)

| Arithmetic check | Maximum absolute index discrepancy |
| --- | --- |
| US consumption index | 0.00357317 |
| India consumption index | 0.00476848 |

Both discrepancies lie within the 0.015-point rounding tolerance. This verifies appendix arithmetic; it does not establish a common saving measure or a causal recession effect.

## Run the example

Use Python 3.12. From this project's directory:

```bash
python -m pip install -r requirements.txt
python reproduce_figures.py --output demo_output
```

For an isolated environment, run `python -m venv .venv` first. Activate it with `source .venv/bin/activate` on Linux/macOS or `.venv\Scripts\activate` on Windows. The standard example runs offline after dependencies are installed.

The [notebook walkthrough](notebooks/01_results_walkthrough.ipynb) explains the saved outputs. Exact command-line options appear in [CLI.txt](docs/CLI.txt).

## Documentation

| Guide | What it covers |
| --- | --- |
| [Methods](docs/METHODS.md) | Formulas, assumptions and interpretation |
| [Data dictionary](docs/DATA_DICTIONARY.md) | Variables, units and validation rules |
| [Results](docs/RESULTS.md) | Actual bundled output and how to read it |
| [Reproducibility](REPRODUCIBILITY.md) | Commands, checks and the recorded environment |
| [Provenance and attribution](docs/PROVENANCE.md) | Historical context, reconstruction and contribution |
| [Roadmap](docs/ROADMAP.md) | Specific extensions, with unfinished work labelled |
| [References](docs/REFERENCES.md) | Method documentation and source links |

## Limits of interpretation

- This is a narrative review and portfolio draft, not a peer-reviewed publication or exhaustive systematic review.
- The cross-country measures use different concepts and denominators.
- Source vintages are retained; the appendix is not a fresh download of the latest official data.
- The reproduction checks verify arithmetic and transcription consistency rather than independently validating every claim in the literature.

## Contribution and research context

September 2026 narrative-review draft comparing the United States, Greece and India and discussing experience effects.

Portfolio owner: Arinjai Das. Generative AI assisted with restructuring, drafting, source checking and document preparation. The source manuscript declares that it collected no new survey data and estimated no new regressions.

**Skills demonstrated:** Literature review, behavioural economics, household finance, evidence synthesis, data definitions, Python visualisation.

[Portfolio](https://github.com/arinjaidas/My-Projects) · [GitHub profile](https://github.com/arinjaidas)
