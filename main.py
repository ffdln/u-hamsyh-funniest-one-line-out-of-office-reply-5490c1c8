#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — one away message.

The entry is a single fixed out-of-office reply, written for
make.fun u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8:
one line, at most 160 characters. I am away until Monday and my
auto-reply has taken over my job — honestly, it is already doing
it better than I did. This program writes that reply to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the
grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The reply is fixed text: the
same bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "I'm away until Monday and my auto-reply has taken over my job "
    "— honestly, it's already doing it better than I did."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the reply against the gate, then write it out."""
    if not 1 <= len(LINE) <= 160:
        return abort(f"reply is {len(LINE)} characters, the gate allows 1-160")
    if not LINE.strip():
        return abort("reply is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
