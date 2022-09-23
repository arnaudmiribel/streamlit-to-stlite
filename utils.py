import json
from dataclasses import dataclass
from pathlib import Path

import streamlit as st

cd = Path(__file__).parent.absolute()


def escape_tick(string: str) -> str:
    return string.replace("`", "`")


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


# def export_to_stlite(
#    entrypoint: str = "streamlit_app.py",
#    files: Union[str, list] = "**/*.py",
#    requirements_filename: str = "requirements.txt",
# ):


@dataclass
class File:
    name: str
    code: str


def export_to_stlite(files: list[File], requirements: list[str] = None) -> str:
    # requirements_path = (cd / requirements_filename).resolve()
    # requirements = requirements_path.read_text()

    if requirements is None:
        requirements = []

    files_dict = {f.name: escape_tick(f.code) for f in files}

    # Make the footer sexy
    add_stlite_in_footer()

    data = {
        "requirements": "\n".join(requirements),
        "entrypoint": files[0].name,
        "files": files_dict,
    }
    html = Path("stlite_template.html").read_text()
    return html.format(data=json.dumps(data))
