#!/usr/bin/env python3
"""Write the competition entry text to /output/entry.txt.

Self-contained: no network, no arguments, no dependencies.
"""

from pathlib import Path

ENTRY = (
    "Day 1: sell $49 Google Business audits + 30 days of posts to "
    "US dentists. Find 2,000 clinics on Maps silent for 90 days; "
    "email each a free sample + Stripe link. Agent writes, "
    "delivers, collects. 1% buy = $980; 0.3% = $294. "
    "Edge: rivals gamble on crypto; clinics pay for patients."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
