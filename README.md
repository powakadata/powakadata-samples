# PowakaData — Market Data Samples

**Historical market data for backtesting and quantitative research.**

PowakaData provides inspectable historical datasets for quantitative researchers, systematic traders, developers, and anyone who wants to verify the data behind a backtest.

This repository contains **free data samples and reproducible examples** for selected PowakaData datasets.

## Why PowakaData?

Backtests are only as reliable as the data and assumptions behind them.

PowakaData focuses on research-ready datasets that can be inspected directly rather than hidden behind a proprietary API.

- Inspectable files
- Free samples before purchase
- Historical equities, futures, forex, crypto, commodities and more
- Point-in-time S&P 500 and Nasdaq-100 membership data
- Data designed for backtesting and quantitative research
- One-time purchase — no subscription required

## Point-in-Time Equity Research

A common source of bias in historical equity research is using today's index constituents to test strategies in the past.

For example, a 2018 S&P 500 backtest built from today's membership can implicitly use information that was not available in 2018.

Point-in-time membership data allows the research universe to be reconstructed using the constituents applicable to each historical period.

This repository includes examples showing how to:

- load point-in-time membership data;
- reconstruct a historical index universe;
- avoid using future membership information;
- join membership data to historical market data;
- build reproducible research inputs.

## Available Data

PowakaData currently provides historical datasets across:

- US equities
- UK / LSE equities
- S&P 500 point-in-time membership
- Nasdaq-100 point-in-time membership
- Futures
- Forex
- Crypto
- Commodities
- Indices
- ETFs
- Macro and economic data

## Free Samples

Free samples are available so researchers can inspect file structure, columns, timestamps, and data format before purchasing a complete dataset.

**Website:** https://powakadata.com/
## Featured Sample — S&P 500 Point-in-Time Membership

Explore a real pre-purchase sample of the PowakaData S&P 500 Point-in-Time Historical Membership Dataset.

- [Inspect the S&P 500 Point-in-Time sample](samples/sp500-point-in-time/)
- [View the interval sample](samples/sp500-point-in-time/INTERVAL_SAMPLE.csv)
- [View constituent events](samples/sp500-point-in-time/EVENT_SAMPLE.csv)
- [Read the interval contract](samples/sp500-point-in-time/INTERVAL_CONTRACT.json)
- [Read the methodology](samples/sp500-point-in-time/METHODOLOGY.txt)
- [Run the Python reconstruction example](examples/reconstruct_sp500_universe.py)

### Why interval semantics matter

On **2026-08-18**, the sample contains a real S&P 500 membership transition:

- **AVB** is no longer active.
- **RDDT** becomes active.

An `EXACT` `effective_to` boundary is exclusive. Treating every interval end as inclusive would incorrectly keep AVB in the historical universe.

The included Python example implements the interval contract and verifies this boundary automatically.

**[Browse the full PowakaData catalog →](https://powakadata.com/)**
## Repository Structure

```text
powakadata-samples/
├── README.md
├── examples/
│   └── reconstruct_sp500_universe.py
└── samples/
    └── sp500-point-in-time/
        ├── README.md
        ├── INTERVAL_SAMPLE.csv
        ├── EVENT_SAMPLE.csv
        ├── INTERVAL_CONTRACT.json
        └── METHODOLOGY.txt
