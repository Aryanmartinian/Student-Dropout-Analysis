import streamlit as st
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image 

st.title('Student Dropout Data Analytics')
st.subheader('Key performance Indicators')
# load the data
@st.cache_data
def load_data():
    path = "data/dataset.csv"
    data = pd.read_csv(path)
    return data

# Loading the data--
# call the load_data function-
with st.spinner('Loading Data...'):
    data = load_data()


cols = data.columns.tolist() # convert the options to list
selected_cols = st.multiselect('Select Columns',cols) # for multiple columns
st.write(f'You selected:{len(selected_cols)}columns')

st.metric(label= 'Average Dropout Students',value=round(data['Unemployment rate'].mean()),
          delta = round(data['Unemployment rate'].std()))

for col in selected_cols:
    st.subheader(f'Mean {col}')
    try:
        st.metric(label=f'Mean {col}',
                value=round(data[col].mean()),
                delta=round(data[col].std()))
        st.line_chart(data[col],use_container_width=True)
    except:
        st.error(f'Cannot display{col} numeric data')