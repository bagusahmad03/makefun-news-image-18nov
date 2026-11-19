"""news-image-20261118 entry: copy the poster beside this file to the output dir.

The image is the entry: entry.png, a 1024x1024 editorial poster summing up
the world news of Wednesday 18 November 2026. This program only copies it,
byte for byte, so two runs always write the same bytes.

The grader runs `python3 -P -s /bot/main.py` with the output directory at
/output. Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    source = HERE / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"entry image missing: {source}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # A straight byte copy: no timestamps, no recompression, no randomness,
    # so every run writes exactly the bytes the judge reviewed.
    shutil.copyfile(source, OUTPUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
