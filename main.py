#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Writes a single one-line robot pickup line to entry.txt inside
MAKEFUN_OUTPUT_DIR (default /output). Python 3 standard library only.
"""

import os
import sys

LINE = "I've paired with a thousand devices, but you're the only one I auto-connect to."


def main():
    line = LINE
    if not line or not line.strip():
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print("error: line exceeds 200 characters", file=sys.stderr)
        return 1
    if line != line.strip():
        print("error: line has leading or trailing whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        print("error: verification failed", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
