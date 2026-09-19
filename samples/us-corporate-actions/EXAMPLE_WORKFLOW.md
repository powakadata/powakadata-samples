# Example Corporate Actions Research Workflow

No provider records are included in this example.

A defensible workflow separates four questions:

1. **Event semantics** — what does the provider-reported date/value represent?
2. **Historical identity** — which security/listing should the action be joined to on that date?
3. **Price semantics** — are the market prices raw, split-adjusted, dividend-adjusted, or otherwise transformed?
4. **Information timing** — was the record actually known before the simulated decision?

## Avoid double adjustment

Do not automatically apply split or dividend transformations to an already-adjusted price series. First establish the adjustment contract of the market-data source.

## Do not manufacture point-in-time availability

The product's `available_at` field is null because historical provider availability is unknown. `observed_at` is an operational acquisition timestamp and must not be substituted for historical known-at time.

## Preserve exact values

Dividend amounts and split rational components are represented as strings under the product contract. Parse them using exact decimal/integer arithmetic where precision matters.

## Keep provenance

A production research pipeline should retain the release identifier and relevant provenance/coverage assumptions alongside backtest outputs so results can be audited later.

For a broader discussion, see the [Corporate Actions Backtesting Guide](https://powakadata.com/us-corporate-actions-backtesting.html?utm_source=github&utm_medium=referral&utm_campaign=corporate_actions_methodology).
