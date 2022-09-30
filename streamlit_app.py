from pathlib import Path

import streamlit as st

from utils import export_to_stlite, get_app_url

st.title("Random app")

st.write("Hey")

app_url = get_app_url()

if "localhost" in app_url:
    path_prefix = Path("")
elif "streamlitapp" in app_url:
    path_prefix = Path("/app/")


html_file = st.text_input("html file", path_prefix / "test.html")
export = st.button("Export to stlite")
if export:
    data = dict(
        main_file=path_prefix / Path("streamlit_app.py"),
        files=[
            path_prefix / Path("streamlit_app.py"),
            path_prefix / Path("pages/01_😎_Page_1.py"),
            path_prefix / Path("pages/02_🚀_Page_2.py"),
            path_prefix / Path("utils.py"),
        ],
        requirements=(path_prefix / Path("requirements.txt")).read_text().splitlines(),
    )

    st.write("Exporting with the following data:", data)

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
