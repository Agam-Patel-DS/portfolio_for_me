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
# lottie_contact=load_lottieurl("")
# # project1=load_lottieurl("")
# project2=load_lottieurl("")
# project3=load_lottieurl("")

st.write("##")
st.subheader("Welcome!")
st.title("AGAM PATEL")
st.write("""

""")
st.write("[Github](https://github.com/Agam-Patel-DS/) | [Linked In](https://in.linkedin.com/in/iagampatel)")
st.write("---")

with st.container():
  selected=option_menu(
    menu_title=None,
    options=["About","Projects"],
    icons=['person','code-slash'],
    orientation='horizontal'
  )

if selected=='About':
  with st.container():
    col1,col2=st.columns(2)
    with col1:
      st.write("##")
      st.title("I'm Agam Patel")
      st.subheader("Undergrad at Sri Ram Institute of Technology")
      st.write("""
      Agam Patel is a dedicated Data Scientist and AI Engineer currently pursuing his Bachelor of Technology in Computer Science. He has a deep passion for developing AI-powered solutions to address complex real-world challenges. With expertise in Large Language Models (LLMs), LangChain, and advanced machine learning techniques, Agam's work spans a variety of domains, including NLP, predictive modeling, and deep learning.
      He has built projects like crop disease prediction, speech-to-text conversion, and intelligent chatbots, demonstrating his ability to combine AI and data science to create impactful, innovative solutions. Agam is continuously pushing the boundaries of what’s possible, with a focus on machine learning, NLP, and generative AI to stay ahead in this rapidly evolving field.
      """)
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

if selected=="Projects":
  with st.container():
    st.header("My Projects")
    st.write("##")
    col5,col6=st.columns((1,2))
    with col5:
      st.write("##")
      st.subheader("RAG QnA Chatbot")
      st.write("Using Langchain and LLM")
      st.write("This chatbot integrates the Groq API for session creation and allows users to upload a PDF document. Powered by the Google Gemma 2b LLM model, it enables users to ask questions based on the document content and keeps track of the chat history for a seamless experience.")
      st.write("[Github Link]()")
    with col6:
      st_lottie(lottie_coder,height=300)
      
  with st.container():
    col7,col8=st.columns((1,2))
    with col7:
      st.write("##")
      st.subheader("Finger Detection")
      st.write("Using CNN Oject Detection")
      st.write("The Number of Finger Detection project aims to develop a system that can accurately detect and recognize the number of fingers shown in an image using TensorFlow. The system uses Convolutional Neural Networks (CNN) to process images and classify the number of fingers displayed. This project is useful for applications in gesture recognition and human-computer interaction.")
      st.write("[Github Link]()")
    with col8:
      st_lottie(lottie_coder,height=300)

st.write("---")
with st.container():
  st.subheader("Contact")
  st.write("[Email](agampatel75@gmail.com)")
