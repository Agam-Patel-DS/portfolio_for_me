import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

st.write("##")
st.subheader("Welcome!")
st.title("AGAM PATEL")
st.write("""

""")
st.write("[Github](https://github.com/Agam-Patel-DS/)")
st.write("---")

with st.container():
  selected=option_menu(
    menu_title=None,
    options=["About","Projects","Contact"],
    icons=['person','code-slash','chat-left-text-fill'],
    orientation='horizontal'
  )
