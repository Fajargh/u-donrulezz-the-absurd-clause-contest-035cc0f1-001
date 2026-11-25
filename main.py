#!/usr/bin/env python3
"""Entry for The Absurd Clause Contest.

Writes one absurd terms-of-service clause (a single line, at most
200 characters) to /output/entry.txt.
"""

import os

CLAUSE = (
    "Users acknowledge that the moon is the exclusive property of the "
    "Company, and that moonlight viewed through this application is "
    "licensed, not owned, and may be revoked without notice."
)


def main() -> None:
    text = CLAUSE.strip()
    # The sealed gate requires 1-200 characters of UTF-8 text, not only
    # whitespace; fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(text) <= 200:
        raise ValueError(f"clause is {len(text)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
