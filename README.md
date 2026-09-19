# PowakaData — Market Data Samples

**Historical market data for backtesting and quantitative research.**

This repository contains free samples, methodology notes, and reproducible examples for selected PowakaData research datasets.

## Research Data Suite

### S&P 500 Point-in-Time Membership + Canonical D1
Historical membership intervals for reconstructing the S&P 500 universe as it existed through time, with a documented point-in-time research contract.

- [Free S&P 500 PIT sample](samples/sp500-point-in-time/)
- [Python universe reconstruction example](examples/reconstruct_sp500_universe.py)
- [Technical guide](https://powakadata.com/sp500-historical-constituents-backtesting.html?utm_source=github&utm_medium=referral&utm_campaign=research_suite)
- [Dataset page](https://powakadata.com/sp500-point-in-time-membership.html?utm_source=github&utm_medium=referral&utm_campaign=research_suite)

### Nasdaq-100 Point-in-Time Membership + Canonical D1
Historical Nasdaq-100 membership and canonical daily research data for point-in-time universe construction.

- [Technical guide](https://powakadata.com/nasdaq100-historical-constituents-backtesting.html?utm_source=github&utm_medium=referral&utm_campaign=research_suite)
- [Dataset page](https://powakadata.com/nasdaq100-point-in-time-membership.html?utm_source=github&utm_medium=referral&utm_campaign=research_suite)
- Public sample: **not yet published in this repository**. No synthetic or unapproved provider data is substituted.

### US Corporate Actions Historical Data
Historical US dividend and stock split provider records for research workflows that need explicit event-date, adjustment, coverage, and provenance semantics.

- [Corporate actions backtesting guide](https://powakadata.com/us-corporate-actions-backtesting.html?utm_source=github&utm_medium=referral&utm_campaign=research_suite)
- [Dataset page](https://powakadata.com/us-corporate-actions-historical-data.html?utm_source=github&utm_medium=referral&utm_campaign=research_suite)
- Public sample: **not yet published in this repository**. No synthetic or unapproved provider data is substituted.

## Why point-in-time data matters

Using today's index constituents to backtest the past can introduce survivorship and universe-selection bias. A point-in-time membership contract separates historical eligibility from what is known today.

The included S&P 500 sample demonstrates interval semantics around a real membership transition and includes the contract needed to interpret interval boundaries correctly.

## Corporate actions require a separate research contract

Historical dividends and stock splits are not automatically point-in-time. Event date, information availability, historical security identity, and price-adjustment semantics are separate questions. Applying an action to a series that already embeds the adjustment can also double count the transformation.

The Corporate Actions guide documents these issues without claiming that the historical provider-record product is point-in-time or survivorship-safe.

## Available Data

PowakaData also provides historical datasets across US equities, UK/LSE equities, futures, forex, crypto, commodities, indices, ETFs, and macro/economic data.

[Browse the PowakaData catalog](https://powakadata.com/?utm_source=github&utm_medium=referral&utm_campaign=research_suite)

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
```

## Sample policy

Only approved public samples are committed here. Full customer packages and unapproved provider records are not published. Where a public sample has not yet been approved, this repository links to the methodology/technical guide instead of fabricating example rows.
