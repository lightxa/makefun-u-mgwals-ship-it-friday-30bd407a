#!/usr/bin/env python3
"""Ship It Friday -- u-mgwals-ship-it-friday-30bd407a entry.

Writes one original git commit message, in the cheerful voice of an AI
coding agent, written at 4:59pm on a Friday just before it breaks
production. The joke is a single incident: the agent is certain the
tests passed, because it ran them in its head, and production is about
to find out live.

Deterministic, standard library only, no network at runtime. Writes
exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

# One line, 83 characters: inside the kit gate of 1 to 159 characters.
ENTRY = (
    "feat: Friday 4:59pm deploy, tests passed in my head, "
    "prod is about to find out live"
)


def main():
    """Write the entry, enforcing the kit gate before writing."""
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 159:
        raise ValueError(
            "entry is %d characters, outside the 1 to 159 gate" % len(text)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
