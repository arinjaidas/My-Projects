# Results walkthrough

All values below are synthetic or illustrative workflow results.

| Moment | Theoretical | One simulated sample |
| --- | --- | --- |
| Mean | 40 | 40.3444 |
| Variance | 15.7692 | 21.7934 |

The sample variance differs visibly from its theoretical value, illustrating finite-sample dispersion under persistence and heavy tails. Two hundred seeded replications are provided rather than hiding this variation. MATLAB companion execution is not claimed.

![Results preview](../demo_output/arma_diagnostics.svg)

The numerical files in [demo_output](../demo_output/) are the authoritative bundled artifacts. Re-run the entry command to reproduce the workflow. Figure metadata can differ across renders even when the underlying numerical example is unchanged.
