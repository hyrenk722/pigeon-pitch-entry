"""Pigeon Pitch, One Line — u-donrulezz-pigeon-pitch-one-line-af06c6cf.

One-line elevator pitch from a city pigeon to investors, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

ENTRY = (
    "I run the only delivery network in this city that never gets stuck "
    "in traffic \u2014 because we fly over it, and the drivers eat the packages."
)


def check_gate(text):
    """Gate: /output/entry.txt is UTF-8 text of 1 to 200 characters."""
    assert isinstance(text, str)
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    return text


def main():
    text = check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text + "\n", "round-trip mismatch"


if __name__ == "__main__":
    main()
