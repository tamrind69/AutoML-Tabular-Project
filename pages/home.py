import streamlit as st

def show():
    st.set_page_config(
        page_title="AutoML Tabular Predictor", 
        layout="wide"
        )

    st.title("AutoML Tabular Predictor")
    st.write("Welcome to my app! This app allows you to perform automated machine learning on tabular data.")