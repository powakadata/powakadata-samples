#!/usr/bin/env python3
"""Illustrative corporate-actions research contract.

This example contains no provider records. It demonstrates guardrails that a
research pipeline can enforce before joining corporate actions to market data.
"""

from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Optional


@dataclass(frozen=True)
class Dividend:
    event_date: str
    amount: str
    currency: str
    available_at: Optional[str] = None

    def exact_amount(self) -> Decimal:
        return Decimal(self.amount)


@dataclass(frozen=True)
class Split:
    event_date: str
    numerator: str
    denominator: str
    available_at: Optional[str] = None

    def exact_ratio(self) -> Fraction:
        return Fraction(int(self.numerator), int(self.denominator))


def require_point_in_time_availability(available_at: Optional[str]) -> None:
    """Reject records when a strategy requires known-at-time availability."""
    if available_at is None:
        raise ValueError(
            "Historical availability is unknown; do not treat event_date or "
            "observed_at as a substitute for available_at."
        )


def require_unadjusted_prices(price_semantics: str) -> None:
    """Simple guard against accidental double adjustment."""
    if price_semantics != "unadjusted":
        raise ValueError(
            "Confirm the market-data adjustment contract before applying "
            "corporate-action transformations."
        )


if __name__ == "__main__":
    # Schema-only examples: these are illustrative values, not provider rows.
    dividend = Dividend("YYYY-MM-DD", "1.25", "USD")
    split = Split("YYYY-MM-DD", "2", "1")

    print("Exact dividend amount:", dividend.exact_amount())
    print("Exact split ratio:", split.exact_ratio())
    print("No provider records are embedded in this example.")
