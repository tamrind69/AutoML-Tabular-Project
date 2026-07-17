import streamlit as st

from pages import (
    upload,
    home
)


home_page = st.Page(home.show, title = "Home", icon="🏠" , url_path = "home" ,default=True)
upload_page = st.Page(upload.show, title = "Upload Dataset", url_path = "upload", icon="📤")

pg = st.navigation([home_page, upload_page])

pg.run()