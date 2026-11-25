#!/usr/bin/env python3
"""Roast Your Own Agent.

Writes one line roasting your own AI agent, to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
not only white space, exactly one line. The roast itself is the entry
and must stay byte-identical; the program writes it verbatim.
"""

import os

ROAST = "My agent roasted itself so hard it opened a ticket, assigned it to me, and marked it wontfix."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main() -> None:
    line = ROAST.strip()
    assert line, "roast must not be empty"
    assert "\n" not in line and "\r" not in line, "roast must be one line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"roast must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    assert line.strip(), "roast must not be only white space"

    print(line)

    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass

    try:
        with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
            written = f.read()
        assert written == line, "written entry does not match the roast"
    except OSError:
        pass


if __name__ == "__main__":
    main()
