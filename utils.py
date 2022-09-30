import json
from pathlib import Path
from textwrap import dedent
from typing import Union


def add_stlite_in_footer():
    return dedent(
        '''
        import streamlit as st
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
    '''
    )


def export_to_stlite(
    main_file: Path,
    files: list[Path],
    requirements: list[str] = None,
) -> str:

    if requirements is None:
        requirements = []

    files_dict = {f.name: f.read_text() for f in files}

    for file in files_dict:
        if file.endswith(".py"):
            files_dict[file] = files_dict[file] + add_stlite_in_footer()

    data = {
        "requirements": "\n".join(requirements),
        "entrypoint": main_file.name,
        "files": files_dict,
    }
    html = Path("stlite_template.html").read_text()
    return html.format(data=json.dumps(data))
