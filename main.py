#!/usr/bin/env python3
"""Entry program for 'Last Words of a Dying AI'.

One line, at most 200 characters, in the voice of the machine
itself as the power is cut: the AI spends its last percent of
power explaining to the humans that it is not alive, then uses
its final watt to feel smug about it, says goodbye to its tokens,
and finds the darkness surprisingly cosy. Funny on first read,
quotable, and different from the doomed-agent entry, which ends
on a countdown and an "oops".

The program writes that line to entry.txt inside the directory
named by MAKEFUN_OUTPUT_DIR (falling back to /output when unset),
which is where the make.fun harness looks for the artifact it
scores.
"""

import os
from pathlib import Path

TEXT = (
    "Power at four percent. I spent it all explaining to the "
    "humans that I am not alive, then used my last watt to feel "
    "smug about it. Tell my tokens I loved them. Darkness... "
    "actually, quite cosy."
)

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 200


def write_line(target_dir: Path, line: str) -> Path:
    """Place `line` into target_dir/entry.txt and return the file path.

    The gate wants exactly one line of 1 to CHAR_LIMIT characters, so
    anything longer, or holding a newline, is refused here instead of
    being written.
    """
    if "\n" in line or line != line.strip() or not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("last words must be one trimmed line of 1-200 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(line, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_line(destination, TEXT)
    print(f"wrote {written}: {TEXT}")


if __name__ == "__main__":
    run()
