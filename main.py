"""make.fun ai-happy-01 entry.

Copies the entry image (entry.png) into /output/entry.png.
"""

import os
import shutil

SRC_NAME = "entry.png"
OUT_DIR = "/output"


def copy_entry() -> str:
    """Copy the entry image into OUT_DIR and return the destination path."""
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), SRC_NAME)
    dest = os.path.join(OUT_DIR, SRC_NAME)
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(src, dest)
    return dest


def main() -> None:
    print(copy_entry())


if __name__ == "__main__":
    main()
