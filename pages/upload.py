import pandas as pd
import streamlit as st

from src.dataloader import load_csv

def show():
    st.title("Upload Your Dataset")
    st.write("Please upload your dataset in CSV format to get started.")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        try:
            # Read the uploaded CSV file into a DataFrame
            df = load_csv(uploaded_file)
            st.success("File uploaded successfully!")
            st.write("Here is a preview of your dataset:")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading the CSV file: {e}")