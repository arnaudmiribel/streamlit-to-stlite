from pathlib import Path

import streamlit as st

from utils import export_to_stlite

x = st.slider("Hey", 0, 100)

st.write(f"Try out this {x}")

html_file = st.text_input("html file", "test.html")
export = st.button("Export to stlite")
if export:
    data = dict(
        main_file="streamlit_app.py",
        files=[
            "streamlit_app.py",
            "pages/01_😎_Page_1.py",
            "pages/02_🚀_Page_2.py",
            "utils.py",
        ],
        requirements=Path("requirements.txt").read_text().splitlines(),
    )

    st.write("Exporting with the following data:", data)

    html = export_to_stlite(**data)
    st.write("Here's the HTML:")
    st.code(html, language="html")

    Path(html_file).write_text(html)
    st.write(f"Saved to {html_file}")
