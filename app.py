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
    with st.container():
      selected1=option_menu(
      menu_title=None,
      options=["Machine Learning","Object Detection","NLP", "Gen AI"],
      orientation='horizontal'
    )
    if selected=="Gen AI":
      with st.container():
      col5,col6=st.columns((1,2))
      with col5:
        st.write("##")
        st.subheader("RAG QnA Chatbot with history")
        st.write("Using Langchain and LLM")
        st.write("This chatbot integrates the Groq API for session creation and allows users to upload a PDF document. Powered by the Google Gemma 2b LLM model, it enables users to ask questions based on the document content and keeps track of the chat history for a seamless experience.")
        st.write("[Github Link](https://github.com/Agam-Patel-DS/RAG-Document-Q-A-Chatbot-with-Chat-History)")
      with col6:
        st_lottie(lottie_coder,height=300)

      with st.container():
      col9,col10=st.columns((1,2))
      with col9:
        st.write("##")
        st.subheader("Youtube and Website URL Summarizer")
        st.write("Using Langchain")
        st.write("This app makes it easy to quickly summarize YouTube videos and web pages by simply entering the URL. Whether you're short on time or need a concise overview, the summarizer uses a map-reduce technique to break down content and deliver accurate summaries, helping you get the key insights without going through the entire video or article. Built using the Groq API for speed and precision, this tool is perfect for students, researchers, and content consumers looking for quick takeaways.")
        st.write("[Github Link](https://github.com/Agam-Patel-DS/Youtube-Video-and-Webpage-Summarizer-using-AI-and-Langchain)")
      with col10:
        st_lottie(lottie_coder,height=300)

      with st.container():
      col11,col12=st.columns((1,2))
      with col11:
        st.write("##")
        st.subheader("Chatbot with SQL Database")
        st.write("Using Langchain")
        st.write("Powered by open-source LLM models, this chatbot can write, run, and explain SQL queries effortlessly. Whether you're fetching data, updating tables, or analyzing databases, the chatbot understands your commands and translates them into accurate SQL code, making it perfect for developers, data analysts, and anyone looking to streamline their database operations. This project leverages the latest advancements in AI to make working with SQL easier, faster, and more intuitive!")
        st.write("[Github Link](https://github.com/Agam-Patel-DS/Chatbot-with-SQL-Database-using-Langchain)")
      with col12:
        st_lottie(lottie_coder,height=300)

      with st.container():
      col13,col14=st.columns((1,2))
      with col13:
        st.write("##")
        st.subheader("Mathbot using Langchain")
        st.write("Using Langchain LLMMathChain")
        st.write("Powered by LLM Chain and LLMMathChain via LangChain, this bot can understand mathematical queries, break them down, and provide accurate solutions in real time. Whether it's algebra, calculus, or complex equations, Mathbot simplifies the process by converting text-based problems into structured solutions, making it an ideal tool for students, teachers, and math enthusiasts looking for quick and reliable answers. Built to enhance productivity, it brings the power of AI to mathematical problem-solving!")
        st.write("[Github Link](https://github.com/Agam-Patel-DS/MathBot-using-LLMMathChain---Langchain)")
      with col14:
        st_lottie(lottie_coder,height=300)
        
    if selected=="Object Detection":  
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
          
      with st.container():
        col15,col16=st.columns((1,2))
        with col15:
          st.write("##")
          st.subheader("Crop Disease Detection")
          st.write("Using CNN Oject Detection")
          st.write("This deep learning model analyzes images of plant leaves, identifying various diseases with high accuracy. By leveraging the lightweight and efficient MobileNet model, this tool is designed to run smoothly on mobile and edge devices, making it accessible in the field. The project incorporates a pre-trained MobileNet as the base model, combined with a global average pooling layer, dropout for regularization, and a softmax output layer to classify diseases. Ideal for improving crop health monitoring, this model empowers users with a fast, efficient solution for managing plant diseases and enhancing agricultural productivity.")
          st.write("[Github Link](https://github.com/Agam-Patel-DS/Crop-Disease-Prediction)")
        with col16:
          st_lottie(lottie_coder,height=300)

      with st.container():
        col17,col18=st.columns((1,2))
        with col17:
          st.write("##")
          st.subheader("Face Mask Detection")
          st.write("Using CNN Oject Detection")
          st.write("The system can distinguish between images of individuals wearing masks, not wearing masks, and even incorrectly wearing masks, making it ideal for public safety monitoring in areas like airports, workplaces, and public transport. This lightweight and high-performance model helps enhance compliance with health protocols by providing an easy-to-deploy solution for mask detection.")
          st.write("[Github Link](https://github.com/AgamPatel108/Face-Mask-Detection)")
        with col18:
          st_lottie(lottie_coder,height=300)

    if selected=="NLP":
      with st.container():
        col19,col20=st.columns((1,2))
        with col19:
          st.write("##")
          st.subheader("Next Word Predictor")
          st.write("Using LSTM and Early Stopping")
          st.write("This model processes text input and accurately predicts the most likely next word, making it a powerful tool for language modeling, text generation, and auto-completion tasks. By leveraging Long Short-Term Memory (LSTM) networks, which excel at capturing long-range dependencies in text, and Early Stopping to prevent overfitting, the model ensures high accuracy and efficiency. Ideal for applications in NLP tasks such as predictive typing, content generation, and chatbots, this project brings advanced AI capabilities to language processing in an easy-to-use framework.")
          st.write("[Github Link](https://github.com/Agam-Patel-DS/Next-Word-Predictor-Using-LSTM-RNN-and-Early-Stopping)")
        with col20:
          st_lottie(lottie_coder,height=300)

      with st.container():
        col21,col22=st.columns((1,2))
        with col21:
          st.write("##")
          st.subheader("Sentiment Analysis")
          st.write("Using RNN")
          st.write("This model captures the sequential nature of text data, making it ideal for understanding the emotions and opinions expressed in reviews, social media posts, and other textual content. By leveraging RNNs, which excel at processing sequences, the model effectively analyzes the context and patterns within the text to predict the underlying sentiment. Whether you're analyzing customer feedback or monitoring brand sentiment, this project provides a robust and efficient solution for real-time sentiment classification, enabling deeper insights into text data.")
          st.write("[Github Link](https://github.com/AgamPatel108/Sentiment-Anaylisis-RNN-Deploy)")
        with col22:
          st_lottie(lottie_coder,height=300)

        with st.container():
        col23,col24=st.columns((1,2))
        with col23:
          st.write("##")
          st.subheader("Text Summarizer")
          st.write("Using Transformers")
          st.write("Text Summarizer, powered by Transformers, designed to generate concise and coherent summaries from long-form text. This model utilizes the powerful attention mechanism in transformer architectures, such as BERT or GPT, to capture the most important information and provide an accurate summary while preserving the meaning of the original text. Whether summarizing articles, research papers, or reports, this tool delivers high-quality results quickly and efficiently. Ideal for anyone looking to distill large amounts of information into digestible summaries, this project showcases the cutting-edge capabilities of transformer-based models for text summarization tasks.")
          st.write("[Github Link](https://github.com/AgamPatel108/Text-Summarizer-Project-using-NLP)")
        with col24:
          st_lottie(lottie_coder,height=300)
          
    if selected=="Machine Learning":
      with st.container():
        col25,col26=st.columns((1,2))
        with col25:
          st.write("##")
          st.subheader("Diabetes Predictor")
          st.write("By analyzing key health indicators such as age, BMI, glucose levels, and more, the model can accurately assess the risk of diabetes in individuals. Built using a combination of data preprocessing, feature engineering, and classification algorithms, this tool is ideal for early detection and preventive healthcare. Whether used by healthcare professionals or researchers, the Diabetes Predictor helps provide insights into a patient's risk profile, aiding in better decision-making and early intervention for diabetes management.")
          st.write("[Github Link](https://github.com/AgamPatel108/Diabetes-Predictor)")
        with col26:
          st_lottie(lottie_coder,height=300)
          
      with st.container():
        col25,col26=st.columns((1,2))
        with col25:
          st.write("##")
          st.subheader("Credit Card Fraud Detection")
          st.write("By employing algorithms such as decision trees, random forests, and neural networks, the model efficiently processes vast amounts of transaction data, adapting to new patterns of fraud. This tool is essential for financial institutions aiming to enhance security and protect customers from fraud, enabling rapid detection and response to suspicious transactions.")
          st.write("[Github Link](https://github.com/AgamPatel108/Credit-Card-Fraud-Detect-Notebook-Only)")
        with col26:
          st_lottie(lottie_coder,height=300)
          
      with st.container():
        col25,col26=st.columns((1,2))
        with col25:
          st.write("##")
          st.subheader(Fire Weather Index Prediction")
          st.write("This model leverages historical weather data, including temperature, humidity, wind speed, and precipitation, to generate an accurate fire weather index. By using machine learning algorithms like regression analysis and time series forecasting, it predicts fire risk levels, helping authorities and land managers make informed decisions regarding fire prevention and resource allocation. This tool is vital for enhancing community safety and protecting natural resources by providing timely insights into potential fire hazards.")
          st.write("[Github Link](https://github.com/AgamPatel108/FWI-predictor)")
        with col26:
          st_lottie(lottie_coder,height=300)

st.write("---")
with st.container():
  st.subheader("Contact")
  st.write("[Email](agampatel75@gmail.com)")
