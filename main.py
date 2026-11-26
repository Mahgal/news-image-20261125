"""news-image-20261125 entry (Python 3.13, standard library only).

Copies the bundled image assets/entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output/entry.png). Runs offline and writes identical bytes every run.
"""
import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    src = here / "assets" / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
