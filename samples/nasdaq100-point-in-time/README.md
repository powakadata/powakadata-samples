# Nasdaq-100 Point-in-Time Membership — Public Sample

This directory contains a small public excerpt from PowakaData release `PIT-NDX100-R4.2-CONT-20260915-D1`, whose customer coverage ends 2026-09-15.

The full release contains 207 membership intervals (208 CSV lines including the header) and 113 membership events (114 CSV lines including the header). The files here are intentionally small excerpts for inspecting schema and interval/event semantics; they are not a substitute for the commercial dataset.

## Files

- `INTERVAL_SAMPLE.csv` — five real membership-interval rows illustrating exact, window-censored and right-censored boundaries.
- `EVENT_SAMPLE.csv` — five real quarterly-change event rows effective 2026-06-22.
- `../../examples/reconstruct_nasdaq100_universe.py` — minimal example for reconstructing eligibility from the interval sample.

## Interval semantics

Membership authority uses half-open intervals. In practical terms, an `effective_to` boundary marked `EXACT` is not an eligible date for that interval. A blank `effective_to` with `RIGHT_CENSORED` means the interval remains open through the release's observed coverage; it is not proof of indefinite future membership.

`research_security_id` is the stable research identity. `security_lineage_label` may be retrospective and should not automatically be treated as the actual traded symbol for every historical session.

## Important scope notes

The current continuation release carries historical rows and known limitations forward; it is not presented as a historical repair. Canonical D1 has a separate field contract. In that contract, provider OHLC is unadjusted price, adjusted fields are supplementary, and the legacy `raw_volume` field has specific provider semantics documented in the full release.

No licensed raw provider responses or full Canonical D1 rows are redistributed in this public sample.

- [Technical guide](https://powakadata.com/nasdaq100-historical-constituents-backtesting.html?utm_source=github&utm_medium=referral&utm_campaign=nasdaq100_sample)
- [Dataset page](https://powakadata.com/nasdaq100-point-in-time-membership.html?utm_source=github&utm_medium=referral&utm_campaign=nasdaq100_sample)
