"""
CLI for creating stlite html file from streamlit app
"""

from pathlib import Path
from typing import Optional

import typer

from utils import export_to_stlite

cd = Path(__file__).parent.absolute()


def main(
    main_file: str = "streamlit_app.py",
    requirements: str = "requirements.txt",
    other_files: list[str] = typer.Argument(None),
    output: str = "build/index.html",
):
    all_files = [cd / main_file]
    if not other_files:
        other_files = ["*.py", "pages/*.py"]

    if other_files is not None:
        for f in other_files:
            if "*" in f:
                all_files.extend(cd.glob(f))
            else:
                all_files += [cd / file for file in other_files]

    html = export_to_stlite(
        main_file=cd / main_file,
        files=all_files,
        requirements=(cd / requirements).read_text().splitlines(),
    )
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(output).write_text(html)


if __name__ == "__main__":
    typer.run(main)
