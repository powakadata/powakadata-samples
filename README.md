# S&P 500 Point-in-Time Membership Sample

This directory contains a **pre-purchase sample** from the PowakaData S&P 500 Point-in-Time Historical Membership Dataset.

Release represented: **PIT-SP500-20260818-R3**

Full commercial coverage: **2016-08-01 through 2026-08-18**

The sample is intentionally incomplete. It is provided so researchers can inspect the schema, interval semantics, event structure, and reconstruction logic before purchasing the full dataset.

## Files

- `INTERVAL_SAMPLE.csv` — selected membership intervals
- `EVENT_SAMPLE.csv` — selected constituent and ticker-change events
- `INTERVAL_CONTRACT.json` — machine-readable interval contract
- `METHODOLOGY.txt` — authoritative methodology for this release

## Critical interval semantics

`effective_from` is inclusive for every supported start semantics value.

For the end boundary:

- `end_semantics = EXACT` means `effective_to` is **exclusive**
- `end_semantics = RIGHT_CENSORED` means `effective_to` is **inclusive** at the commercial coverage boundary
- `end_semantics = WINDOW_CENSORED` is supported for legacy compatibility and is inclusive at the coverage boundary
- unknown semantics must **fail closed**

In other words, do **not** apply this rule to every row:

```python
effective_from <= D <= effective_to
```

That naive predicate is wrong for `EXACT` intervals.

## Concrete boundary example

The sample includes the 2026-08-18 S&P 500 transition where:

- `AVB` ends with `end_semantics = EXACT`
- `RDDT` begins on 2026-08-18
- therefore `AVB` is absent on 2026-08-18
- and `RDDT` is present on 2026-08-18

The full commercial release has **503 unique securities** in the 2026-08-18 closing state. Treating every `effective_to` as inclusive would incorrectly retain AVB and produce a 504th row.

## Security identity

`security_id` identifies a supported security lineage.

Ticker symbols are time-varying labels and should not be treated as permanent security identifiers. A ticker change can end one symbol interval and begin another on the same `security_id`.

## Example code

See:

`../../examples/reconstruct_sp500_universe.py`

The example:

- loads the interval contract;
- validates supported interval semantics;
- fails closed on unknown semantics;
- reconstructs active sample rows for a requested date;
- verifies the AVB/RDDT and EA/FERG boundary examples included in this sample.

Because this repository contains only a **selected sample**, the script does not attempt to reproduce the complete 503-security index state from the sample files alone.

## Full dataset

The complete PowakaData S&P 500 Point-in-Time Historical Membership Dataset is available at:

https://powakadata.com/

**Price:** USD 49 one-time

No subscription is required.
