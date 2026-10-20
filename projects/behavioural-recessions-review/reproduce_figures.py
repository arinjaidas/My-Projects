"""Reproduce the archived review appendix; retain each source's distinct concept."""
from pathlib import Path
import argparse
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def run(output, data_dir=None):
    data_dir = Path(data_dir) if data_dir else Path(__file__).parent / 'data'
    output = Path(output); output.mkdir(parents=True, exist_ok=True)
    us = pd.read_csv(data_dir / 'us_households.csv')
    gr = pd.read_csv(data_dir / 'greece_saving_indicator.csv')
    saving = pd.read_csv(data_dir / 'india_saving_components.csv')
    india = pd.read_csv(data_dir / 'india_consumption.csv')
    us['calculated_pce_index'] = 100 * us.real_pce_bn_chained_2017_usd / us.loc[us.year == 2007, 'real_pce_bn_chained_2017_usd'].iloc[0]
    india['calculated_pfce_index'] = 100 * india.real_pfce_crore_2011_12_inr / india.loc[india.fiscal_year == '2019-20', 'real_pfce_crore_2011_12_inr'].iloc[0]
    assert np.allclose(us.calculated_pce_index, us.reported_pce_index_2007_100, atol=.015, rtol=0), 'US appendix index mismatch'
    assert np.allclose(india.calculated_pfce_index, india.reported_pfce_index_2019_20_100, atol=.015, rtol=0), 'India appendix index mismatch'
    assert ((gr[['share_2009_pct', 'share_2014_pct']] >= 0) & (gr[['share_2009_pct', 'share_2014_pct']] <= 100)).all().all()
    us.to_csv(output / 'us_reproduction.csv', index=False); india.to_csv(output / 'india_reproduction.csv', index=False)
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    us.plot(x='year', y='saving_rate_pct_dpi', marker='o', legend=False, ax=axes[0, 0], color='#238c83')
    axes[0, 0].set(title='US personal saving', ylabel='Percent of disposable personal income', xlabel='Year')
    gr.plot.bar(x='income_group', y=['share_2009_pct', 'share_2014_pct'], ax=axes[0, 1], rot=0, color=['#18354a', '#63b9a9'])
    axes[0, 1].set(title='Greece: expenditure below income', ylabel='Share of households in each income group (%)', xlabel='Income percentile group')
    axes[0, 1].legend(['2009', '2014'], fontsize=8)
    saving.plot(x='fiscal_year', y=['net_financial_pct_gndi', 'physical_assets_pct_gndi'], ax=axes[1, 0], marker='o')
    axes[1, 0].set(title='India: selected saving components', ylabel='Percent of GNDI', xlabel='Fiscal year')
    axes[1, 0].legend(['Net financial', 'Physical assets'], fontsize=8)
    india.plot(x='fiscal_year', y='calculated_pfce_index', marker='o', ax=axes[1, 1], legend=False, color='#238c83')
    axes[1, 1].set(title='India: real aggregate consumption', ylabel='Index: 2019-20 = 100', xlabel='Fiscal year')
    for ax in axes.ravel(): ax.grid(alpha=.2); ax.tick_params(axis='x', labelsize=8)
    fig.suptitle('ARCHIVED REVIEW APPENDIX: DISTINCT MEASURES AND VINTAGES', fontsize=12)
    fig.tight_layout(); fig.savefig(output / 'review_appendix.svg'); plt.close(fig)
    # Redraw the manuscript's empirical figures with sufficient label margins.
    for number in range(2, 7):
        fig, ax = plt.subplots(figsize=(8, 4.8))
        if number == 2:
            us.plot(x='year', y='saving_rate_pct_dpi', marker='o', legend=False, ax=ax, color='#18354a')
            ax.set(title='US personal saving rate', ylabel='Percent of disposable personal income', xlabel='Year')
        elif number == 3:
            us.plot(x='year', y='calculated_pce_index', marker='o', legend=False, ax=ax, color='#18354a')
            ax.set(title='US real personal consumption', ylabel='Index: 2007 = 100', xlabel='Year')
        elif number == 4:
            gr.plot.barh(x='income_group', y=['share_2009_pct', 'share_2014_pct'], ax=ax, color=['#91a9b3', '#18354a'])
            ax.set(title='Greece: households spending less than income', xlabel='Share of households in each group (%)', ylabel='Income percentile group')
            ax.legend(['2009', '2014']); ax.invert_yaxis()
        elif number == 5:
            saving.plot(x='fiscal_year', y=['net_financial_pct_gndi', 'physical_assets_pct_gndi'], marker='o', ax=ax)
            ax.set(title='India: selected household saving components', ylabel='Percent of GNDI', xlabel='Fiscal year')
            ax.legend(['Net financial saving', 'Saving in physical assets'])
        else:
            india.plot(x='fiscal_year', y='calculated_pfce_index', marker='o', legend=False, ax=ax, color='#18354a')
            ax.set(title='India: real aggregate private consumption', ylabel='Index: 2019-20 = 100', xlabel='Fiscal year')
        ax.grid(alpha=.2); fig.tight_layout()
        fig.savefig(output / f'figure-{number}.png', dpi=160, bbox_inches='tight'); plt.close(fig)
    meta = {'synthetic': False, 'data_type': 'Published aggregate observations transcribed in the original review appendix',
            'us_index_max_abs_difference': float((us.calculated_pce_index - us.reported_pce_index_2007_100).abs().max()),
            'india_index_max_abs_difference': float((india.calculated_pfce_index - india.reported_pfce_index_2019_20_100).abs().max()),
            'comparability': 'US personal saving, Greek survey saving indicator and Indian saving components have different definitions and denominators. Do not rank them as one common saving rate.',
            'verification': 'Arithmetic and appendix consistency checked; no fresh source download or causal inference.',
            'manuscript_figures': 'Five empirical figures redrawn from the archived appendix to avoid clipped axis labels; original conceptual figure retained.'}
    (output / 'run_metadata.json').write_text(json.dumps(meta, indent=2))
    return meta


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__); p.add_argument('--output', default='demo_output')
    a = p.parse_args(); print(json.dumps(run(a.output), indent=2))
