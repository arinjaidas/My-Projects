# Gold versus Equities: Investment and Asset Allocation in India

An investment-analysis workflow comparing gold, Indian equities and an international equity benchmark from an INR perspective.

## Research question

How do growth, volatility, drawdowns and diversification change across assets and gold-equity allocations? The documented original project was developed in December 2025. Its original local source files were not recoverable, so this is a clearly labelled October 2026 public reconstruction.

## Methods

- Currency-consistent S&P 500 conversion through USD/INR.
- Calendar-time CAGR, cumulative returns, volatility, drawdowns, Sharpe/Sortino ratios and lower-tail returns.
- Correlations and a grid of gold-equity allocations.
- Explicit daily-rebalanced and buy-and-hold portfolio comparisons.
- Calendar-based rolling CAGR, with no fabricated values before a complete window exists.

![Synthetic example](demo_output/growth.svg)

## Run

```bash
python -m pip install -r requirements.txt
python -m unittest -v test_analysis.py
python analysis.py --demo --output demo_output
```

The included output is synthetic, not historical investment performance. For a permitted CSV:

```bash
python analysis.py --prices your_prices.csv --output results
```

Required columns are Date, GOLD_INR, NIFTY_INR, SP500_USD and USDINR. Prices must be positive, complete and aligned on observed common dates. The optional --download mode uses yfinance; market-data retrieval was not exercised during release verification.

## Assumptions

The default risk-free rate is zero and volatility annualisation uses 252 observations per year; both are configurable. Transaction costs and taxes are not modelled. Gold/equity ETF proxies and a US price index have different fee and distribution characteristics, which must be considered when interpreting real-data comparisons.

## Attribution

Arinjai Das. Original research scope: December 2025. Reconstructed public implementation: October 2026, developed with ChatGPT assistance.
