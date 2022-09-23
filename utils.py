import json
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Union

import streamlit as st

cd = Path()


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
    return dedent('''
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
    ''')


# def export_to_stlite(
#    entrypoint: str = "streamlit_app.py",
#    files: Union[str, list] = "**/*.py",
#    requirements_filename: str = "requirements.txt",
# ):


# def export_to_stlite(files: list[File], requirements: list[str] = None) -> str:
def export_to_stlite(
    main_file: Union[str, Path],
    files: list[Union[str, Path]],
    requirements: list[str] = None,
) -> str:

    if requirements is None:
        requirements = []

    files_dict = {str(f): Path(f).read_text() for f in files}

    for file in files_dict:
        if file.endswith(".py"):
            files_dict[file] =  files_dict[file] + add_stlite_in_footer()

    data = {
        "requirements": "\n".join(requirements),
        "entrypoint": str(main_file),
        "files": files_dict,
    }
    html = Path("stlite_template.html").read_text()
    return html.format(data=json.dumps(data))
