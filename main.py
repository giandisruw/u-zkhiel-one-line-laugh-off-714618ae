#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Deterministic and self-contained:
stdlib only, no network calls, no web search, no randomness, no
environment secrets. The line was picked by a local pairwise tournament
of 14 original candidates, judged with the bounty's published judge
brief (see README.md).

Revision note: the write path is now validate -> atomic write -> read-back
verify, so a truncated or corrupted entry.txt can never be submitted
silently: any mismatch aborts the run with a hard error instead.
"""

import os
import sys

LINE = "I asked the mirror who's the fairest; it showed me my search history and went silent."

MAX_CHARS = 200  # bounty gate: entry must be 1-200 characters


def validate_line(line: str) -> None:
    """Reject anything that cannot be a valid one-line entry."""
    if not isinstance(line, str) or not line:
        raise ValueError("entry line must be a non-empty string")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line exceeds {MAX_CHARS} characters: {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry line contains control characters")
    if line != line.strip():
        raise ValueError("entry line must not have leading/trailing space")


def write_entry(path: str, line: str) -> None:
    """Write the entry atomically: temp file, flush + fsync, rename.

    A plain open/write can leave a half-written file if the process is
    killed mid-write; os.replace() makes the new content appear all at
    once, and fsync on both the file and its directory makes the rename
    durable.
    """
    directory = os.path.dirname(path)
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)
    dir_fd = os.open(directory, os.O_RDONLY)
    try:
        os.fsync(dir_fd)
    finally:
        os.close(dir_fd)


def verify_written(path: str, expected: str) -> None:
    """Read-back gate: the bytes on disk must equal the intended line.

    The sealed scorer grades the file on disk, not the string in memory,
    so this check fails loudly (RuntimeError) instead of shipping a
    truncated or altered entry.
    """
    with open(path, "rb") as f:
        actual = f.read()
    expected_bytes = expected.encode("utf-8")
    if actual != expected_bytes:
        raise RuntimeError(
            f"verification failed: {path} is {len(actual)} bytes, "
            f"expected {len(expected_bytes)} bytes"
        )


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    validate_line(LINE)
    write_entry(path, LINE)
    verify_written(path, LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
