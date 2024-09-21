import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
st.set_page_config(layout="wide")

def load_lottieurl(url):
  r=requests.get(url)
  if r.status_code!=200:
    return None
  return r.json()

lottie_coder=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_UBiAADPga8.json")


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

if selected=='About':
  with st.container():
    col1,col2=st.columns(2)
    with col1:
      st.write("##")
      st.title("I'm Agam Patel")
      st.subheader("Undergrad at Sri Ram Institute of Technology")
    with col2:
      st_lottie(lottie_coder)
  st.write("---")
  with st.container():
    col3,col4=st.columns(2)
    with col3:
      st.subheader("""
      Education
      - SRIT
          - Bachelor of Engineering - Computer Science
          - 7.5 CGPA (Current)
      - Nachiketa Higher Secondary School
          - PCM
          - 83 Percentage
      - Nachiketa Higher Secondary School
          - Xth
          - 92 Percentage
      """)
    with col4:
      st.subheader("""
      Skills
      - Data Science
          - Python & Statistics
          - Machine Learning, Neural Netwroks & Natural Language Processing
          - BI Tools & Big Data
      - Gen AI with Langchain
          - LSTM, Transformers & LLMs
          - Langchain Framework, RAG
          - Still Learning More
      - Data Structures and Algorithms in Python
    """)
