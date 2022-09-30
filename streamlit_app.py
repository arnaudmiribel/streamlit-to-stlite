from pathlib import Path

import streamlit as st

from utils import export_to_stlite

st.title("Random app")

st.write("Hey")

cd = Path(__file__).parent.absolute()

export = st.button("Export to stlite")
if export:
    data = dict(
        main_file=cd / Path("streamlit_app.py"),
        files=[
            cd / Path("streamlit_app.py"),
            cd / Path("pages/01_😎_Page_1.py"),
            cd / Path("pages/02_🚀_Page_2.py"),
            cd / Path("utils.py"),
        ],
        requirements=(cd / Path("requirements.txt")).read_text().splitlines(),
    )

    # st.write("Exporting with the following data:", data)

    html = export_to_stlite(**data)
    # st.write("Here's the HTML:")
    st.download_button(
        label="Download streamlit_app.html",
        data=html,
        file_name="streamlit_app.html",
        # mime='text/html',
    )
    # Path(html_file).write_text("streamlit_app.html")
    # st.write(f"Saved to {html_file}")
    st.expander("Lookup streamlit_app.html").code(html, language="html")
