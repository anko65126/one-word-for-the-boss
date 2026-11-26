"""Entry program for the 'One Word for the Boss' make.fun bounty.

The entry is a single word: Micromanager. Every office knows this
boss — the one who proofreads your emails, re-does your slides and
asks for a status update on the status update. It is funny because
it is instantly recognisable, it is true of so many bosses, and it
needs no explanation. The program writes exactly that one word to
/output/entry.txt (an optional first argument overrides the
destination for a dry run).
"""

import sys
from pathlib import Path

WORD = "Micromanager"
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert " " not in WORD and 1 <= len(WORD) <= 30, "entry must be one word (1-30 characters)"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(WORD + "\n", encoding="utf-8")
    print(f"wrote {target} ({WORD!r}, {len(WORD)} chars)")


if __name__ == "__main__":
    main(sys.argv)
