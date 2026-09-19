#!/usr/bin/env python3
"""Reconstruct eligible Nasdaq-100 sample securities for a research date."""

import csv
from datetime import date
from pathlib import Path

SAMPLE = Path(__file__).resolve().parents[1] / "samples" / "nasdaq100-point-in-time" / "INTERVAL_SAMPLE.csv"

def eligible(row, research_date):
    start = date.fromisoformat(row["effective_from"])
    if research_date < start:
        return False
    end_text = row["effective_to"].strip()
    if not end_text:
        return True
    end = date.fromisoformat(end_text)
    # Authority intervals are half-open: [effective_from, effective_to)
    return research_date < end

def universe_on(day):
    with SAMPLE.open(newline="", encoding="utf-8") as fh:
        rows = csv.DictReader(fh)
        return [
            (r["research_security_id"], r["security_lineage_label"])
            for r in rows if eligible(r, day)
        ]

if __name__ == "__main__":
    for d in (date(2024, 12, 22), date(2024, 12, 23), date(2026, 6, 22)):
        members = universe_on(d)
        print(d.isoformat(), members)
