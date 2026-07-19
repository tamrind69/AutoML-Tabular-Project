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

            st.session_state["uploaded_csv"] = df
            st.success("File uploaded successfully!")
            st.write("Here is a preview of your dataset:")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading the CSV file: {e}")

    st.divider()

    if st.session_state["uploaded_csv"] is not None:
        
        col1 , col2 = st.columns(2)

        with col1:
            st.metric(
                label = "Rows",
                value = df.shape[0])
        with col2:
            st.metric(
                label = "Columns",
                value = df.shape[1])
            
        st.write("Missing Values")
        missing = df.isnull().sum()
        missing = missing[missing>0]
        missing = missing.reset_index()
        missing.columns = ['Columns' , 'Missing Values']

        if missing.shape[0] == 0:
            st.write("No missing values")
        else:
            st.dataframe(missing)

