#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt: starlight that left its star
before the first city was built, arriving only now. The judge is a
relaxation judge, so the text slows the reader down with a vast, quiet
image that dwarfs them — deep time arriving as light — shown, never
instructed. No network, no randomness, no dependencies.
"""

import os

TEXT = (
    "The light falling on you tonight left its star before the first city "
    "was built, before any voice now alive was born — and it is only just "
    "arriving. Nothing here asks anything of you. It waited all this time "
    "to reach you. It can wait a little longer."
)


def main() -> None:
    # Fail loudly instead of emitting an entry the gate would refuse:
    # 1-280 Unicode code points, and not only whitespace.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
