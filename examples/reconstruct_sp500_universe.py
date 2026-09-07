#!/usr/bin/env python3
"""
Reconstruct active S&P 500 membership rows from the PowakaData PIT interval schema.

This example is written against the public pre-purchase sample for:
PIT-SP500-20260818-R3

Important:
- effective_from is inclusive.
- EXACT effective_to is exclusive.
- RIGHT_CENSORED / WINDOW_CENSORED effective_to is inclusive at the coverage boundary.
- Unknown semantics fail closed.
- The public sample is incomplete, so this script validates sample boundary behavior
  rather than reconstructing the full 503-security commercial state.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path
from typing import Dict, Iterable, List


SUPPORTED_START = {"EXACT", "OBSERVED", "LEFT_CENSORED", "WINDOW_CENSORED"}
SUPPORTED_END = {"EXACT", "RIGHT_CENSORED", "WINDOW_CENSORED"}


def parse_date(value: str) -> date:
    return date.fromisoformat(value)


def load_contract(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        contract = json.load(f)

    if contract.get("unknown_semantics") != "ERROR_FAIL_CLOSED":
        raise ValueError("Contract does not require fail-closed handling for unknown semantics.")

    return contract


def load_intervals(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def active_on(day: date, row: Dict[str, str], coverage_start: date, coverage_end: date) -> bool:
    start_semantics = row["start_semantics"]
    end_semantics = row["end_semantics"]

    if start_semantics not in SUPPORTED_START:
        raise ValueError(f"Unsupported start_semantics={start_semantics!r}")
    if end_semantics not in SUPPORTED_END:
        raise ValueError(f"Unsupported end_semantics={end_semantics!r}")

    if day < coverage_start or day > coverage_end:
        raise ValueError(
            f"{day.isoformat()} is outside dataset coverage "
            f"{coverage_start.isoformat()}..{coverage_end.isoformat()}"
        )

    effective_from = parse_date(row["effective_from"])
    effective_to = parse_date(row["effective_to"])

    if day < effective_from:
        return False

    if end_semantics == "EXACT":
        # EXACT means effective_to is the first absent date.
        return day < effective_to

    # RIGHT_CENSORED and legacy WINDOW_CENSORED are inclusive at the coverage boundary.
    return day <= min(effective_to, coverage_end)


def active_rows(day: date, rows: Iterable[Dict[str, str]], contract: dict) -> List[Dict[str, str]]:
    coverage_start = parse_date(contract["coverage"]["start"])
    coverage_end = parse_date(contract["coverage"]["end"])
    return [row for row in rows if active_on(day, row, coverage_start, coverage_end)]


def symbol_state(day: date, symbol: str, rows: List[Dict[str, str]], contract: dict) -> bool:
    return any(row["symbol"] == symbol for row in active_rows(day, rows, contract))


def run_sample_checks(rows: List[Dict[str, str]], contract: dict) -> None:
    checks = [
        ("2026-08-04", "AVB", True),
        ("2026-08-04", "EA", True),
        ("2026-08-04", "FERG", False),
        ("2026-08-04", "RDDT", False),
        ("2026-08-05", "EA", False),
        ("2026-08-05", "FERG", True),
        ("2026-08-17", "AVB", True),
        ("2026-08-17", "RDDT", False),
        ("2026-08-18", "AVB", False),
        ("2026-08-18", "RDDT", True),
    ]

    failures = []
    for day_text, symbol, expected in checks:
        actual = symbol_state(parse_date(day_text), symbol, rows, contract)
        if actual != expected:
            failures.append((day_text, symbol, expected, actual))

    if failures:
        lines = ["Sample boundary checks failed:"]
        for day_text, symbol, expected, actual in failures:
            lines.append(
                f"  {day_text} {symbol}: expected active={expected}, got active={actual}"
            )
        raise AssertionError("\n".join(lines))

    print("Sample boundary checks: PASS")
    print("  2026-08-17: AVB active, RDDT inactive")
    print("  2026-08-18: AVB inactive, RDDT active")
    print("  2026-08-04: EA active, FERG inactive")
    print("  2026-08-05: EA inactive, FERG active")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--date",
        default="2026-08-18",
        help="Membership date in YYYY-MM-DD format (default: 2026-08-18)",
    )
    parser.add_argument(
        "--sample-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "samples"
        / "sp500-point-in-time",
        help="Directory containing INTERVAL_SAMPLE.csv and INTERVAL_CONTRACT.json",
    )
    args = parser.parse_args()

    contract_path = args.sample_dir / "INTERVAL_CONTRACT.json"
    interval_path = args.sample_dir / "INTERVAL_SAMPLE.csv"

    contract = load_contract(contract_path)
    rows = load_intervals(interval_path)

    run_sample_checks(rows, contract)

    day = parse_date(args.date)
    active = active_rows(day, rows, contract)

    print()
    print(f"Active rows in the PUBLIC SAMPLE on {day.isoformat()}: {len(active)}")
    print("security_id,symbol,company_name,membership_type")
    for row in sorted(active, key=lambda r: (r["symbol"], r["security_id"])):
        print(
            f'{row["security_id"]},{row["symbol"]},'
            f'{row["company_name"]},{row["membership_type"]}'
        )

    print()
    print(
        "Note: this is a selected pre-purchase sample, not the full commercial dataset. "
        "Do not interpret the sample row count as the S&P 500 constituent count."
    )


if __name__ == "__main__":
    main()
