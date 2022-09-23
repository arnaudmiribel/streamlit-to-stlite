import streamlit as st

from utils import cd, export_to_stlite

x = st.slider("Hey", 0, 100)

st.write(f"Try out this {x}")

export = st.button("Export to stlite")
if export:
    export_to_stlite(
        files=[
            cd / "streamlit_app.py",
            cd / "pages/01_😎_Page_1.py",
            cd / "pages/02_🚀_Page_2.py",
            cd / "utils.py",
        ]
    )
