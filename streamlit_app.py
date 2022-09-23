from pathlib import Path

import streamlit as st

from utils import export_to_stlite

x = st.slider("Hey", 0, 100)

st.write(f"Try out this {x}")

from streamlit.components.v1 import html

# Lol. Imagine this would work and throw the download. Kidding. But just imagine
# html(
#     """
# <script>

# window.addEventListener('load', function() {
#     let newButton = '<button id="export" class="css-9s5bis"><img src="https://img.icons8.com/fluency-systems-regular/344/export.png" width="20" height="20"></button>';
#     let mainMenu = window.parent.document.getElementById('MainMenu');
#     console.log(mainMenu);
#     let currentMenu = mainMenu.innerHTML;
#     console.log(currentMenu);
#     mainMenu.innerHTML = newButton + currentMenu;

#     window.parent.document.getElementById('export').addEventListener("click", () => alert('yo'), );
# });


# </script>
# """
# )

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
