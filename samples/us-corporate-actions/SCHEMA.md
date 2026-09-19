# Corporate Actions Schema Notes

This is a public documentation summary, not a copy of provider records.

## Dividend fields

Key research fields include:

- `event_id` — deterministic provider-record identity digest.
- `powaka_security_id` — opaque pinned snapshot Security Master surrogate; not independently verified historical economic identity.
- `powaka_listing_id` — opaque pinned snapshot listing surrogate; not proof of historical listing continuity.
- `provider_symbol` — exact requested provider code.
- `event_date` — provider dividend ex-date.
- `available_at` — always null; historical provider availability is unknown.
- `observed_at` — operational response time, not historical known-at time.
- `amount` — exact provider value string; adjustment basis is not independently verified.
- `unadjusted_amount` — exact provider unadjustedValue string; no recomputation.
- `currency` — provider-supplied three-uppercase-letter code; no inferred FX/listing-currency fallback.
- `declaration_date`, `record_date`, `payment_date` — nullable provider dates.

## Split fields

Key research fields include:

- `event_id`
- `powaka_security_id`
- `powaka_listing_id`
- `provider_symbol`
- `event_date` — provider split endpoint reported action date; no invented exchange-session or entitlement assertion.
- `available_at` — always null.
- `observed_at` — operational response time only.
- `split_ratio_raw` — unchanged provider split string.
- `split_numerator` — positive reduced integer representing new shares.
- `split_denominator` — positive reduced integer representing old shares.

## Identity and timing

`listing_status_observed` describes the pinned 2026-08-30 registry snapshot, not status on the event date. `identity_temporal_status` is `SNAPSHOT_ONLY_UNVERIFIED_HISTORY`.

Do not reinterpret operational timestamps as historical information availability. Do not infer historical ticker continuity from snapshot identifiers.

## Precision

Amounts and rational integers are retained as exact strings. Research code should avoid silently converting exact decimal or rational semantics into lower-precision representations when that could change results.
