# US Corporate Actions — Research Contract Resource

This directory documents research semantics for the PowakaData US Corporate Actions Historical Data product without redistributing underlying provider records.

## Current validated scope

Release contract: `EODHD_US_CORPORATE_ACTIONS_PROVIDER_RECORD_HIST_20100101_20260831_R1_V2`

- 919,361 validated core provider records
- 894,446 dividend records
- 24,915 stock split records
- 871 additional source observations disclosed outside the positive-value core
- dividend source observations: 2010-01-02 through 2026-08-31
- split source observations: 2010-01-04 through 2026-08-31

These coverage bounds do not prove complete market-wide or per-security history.

## Important research semantics

This product is a deterministic, provenance-bound filtered snapshot of provider-reported historical split/dividend records. It does **not** claim:

- point-in-time-safe historical identity;
- survivorship-free universe membership;
- verified historical listing/security/ticker continuity;
- complete provider revision history;
- as-known-at-the-time availability;
- independently verified economic-action truth;
- complete adjustment methodology.

For dividends, `event_date` is the provider ex-date. For splits, `event_date` is the provider split endpoint's reported action date. `available_at` is null because historical information availability is unknown.

## Why no provider-row sample is committed here

The current product contract states that commercial license approval and separately authorized promotion remain required. Accordingly, this public repository documents schema and methodology only and does not redistribute provider records or licensed raw responses.

- [Corporate Actions Backtesting Guide](https://powakadata.com/us-corporate-actions-backtesting.html?utm_source=github&utm_medium=referral&utm_campaign=corporate_actions_methodology)
- [US Corporate Actions Dataset](https://powakadata.com/us-corporate-actions-historical-data.html?utm_source=github&utm_medium=referral&utm_campaign=corporate_actions_methodology)

See [SCHEMA.md](SCHEMA.md) and [EXAMPLE_WORKFLOW.md](EXAMPLE_WORKFLOW.md).
