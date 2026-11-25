#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun bounty entry.

Writes a single line (under 200 characters): the excuse an AI agent
hands its human after shipping a bug. Deterministic: the same bytes
on every run. Standard library only.

Run:  python3 main.py
Writes: /output/entry.txt (mode 0644)
"""

import os

ENTRY = (
    "I did test it - on the version of the code I meant to write. "
    "It works flawlessly, and regrettably, that version does not exist."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Guard the bounty gate up front: one line, 1-200 characters.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200, "entry violates the gate"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Leave the output readable by every user (the grader collects it
    # as a different user). Only chmod a file this program created.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
