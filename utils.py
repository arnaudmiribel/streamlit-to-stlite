from pathlib import Path
from typing import Union

import streamlit as st
from jinja2 import Environment, FileSystemLoader

cd = Path(__file__).parent.absolute()


def escape_tick(string: str) -> str:
    return string.replace("`", "\\`")


def format_files(files: dict) -> str:
    return "\n,".join(
        f"""
"{key}": `
{escape_tick(value)}
`"""
        for (key, value) in files.items()
    )


def add_stlite_in_footer():
    st.write(
        r"""
    <style>
    footer:after {
        content:" · Exported by stlite_exporter using stlite";
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


def export_to_stlite(
    entrypoint: str = "streamlit_app.py",
    files: Union[str, list] = "**/*.py",
    requirements_filename: str = "requirements.txt",
):

    requirements_path = (cd / requirements_filename).resolve()
    requirements = requirements_path.read_text()

    if isinstance(files, str):
        if "*" in files:  # Interpreted as a glob query
            files = list(cd.glob(files))
        else:  # Single file
            files = [files]

    # Get all file names and file content into a dictionary
    files_dict: dict = {
        str(file.relative_to(cd)): file.resolve().read_text() for file in files
    }

    # Make the footer sexy
    add_stlite_in_footer()

    # Templating
    env = Environment(
        loader=FileSystemLoader("./"),
    )
    template = env.get_template("stlite_template.html")
    Path("streamlit_app.html").write_text(
        template.render(
            entrypoint=entrypoint,
            files=format_files(files_dict),  # json.dumps(files),
            requirements=requirements,
        )
    )
