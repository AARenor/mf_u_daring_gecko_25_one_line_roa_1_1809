"""Write the make.fun bounty entry text to entry.txt.

Standard library only, no network.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 characters, got {len(TEXT)}"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    entry = out_dir / "entry.txt"
    entry.write_bytes(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters written to {entry}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
