"""Simple rule-based baseline for LVI extraction."""

import re

POSITIVE = [
    r"lymphovascular invasion is present",
    r"lymphovascular invasion identified",
    r"positive for lymphovascular invasion",
    r"lvi present",
]

NEGATIVE = [
    r"no lymphovascular invasion",
    r"lymphovascular invasion is not identified",
    r"lymphovascular invasion not identified",
    r"negative for lymphovascular invasion",
    r"lvi absent",
]


def predict_lvi(text: str) -> int | None:
    """Return 1=present, 0=absent, None=uncertain."""
    text = str(text).lower()
    positive = any(re.search(p, text) for p in POSITIVE)
    negative = any(re.search(p, text) for p in NEGATIVE)

    if positive and not negative:
        return 1
    if negative and not positive:
        return 0
    return None
