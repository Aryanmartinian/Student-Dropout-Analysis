import streamlit as st
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image 


st.set_page_config(layout="wide")
st.header("Student Dropout Analysis using Streamlit")
st.sidebar.title("Dropout Analysis")
data = pd.read_csv("data/dataset.csv")
if st.checkbox("Show Data"):
    st.write(data.head(100))

markdown=("""
      This application basically demonstrates the Data Analysis of Student dropout database
            provided in the dataset.

""")
st.sidebar.info(markdown)
logo = "8d238e04-1eb1-4221-ae6f-9ca9401d438d.png"
st.sidebar.image(logo)
