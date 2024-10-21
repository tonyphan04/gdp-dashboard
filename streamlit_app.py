import streamlit as st
import kagglehub
import pandas as pd
import numpy as np
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Loan dashboard',
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_gdp_data():
    # Download latest version
    path = kagglehub.dataset_download("sujithmandala/simple-loan-classification-dataset")

    data = pd.read_csv(path + "/loan.csv")
    # Calculate total income of num of male and female based on gender
    total = data.groupby('gender').agg(
        total_income = pd.NamedAgg(column = 'income', aggfunc='sum'),
        gender_count = pd.NamedAgg(column = 'gender', aggfunc='count'),
    ).reset_index()

    return total

data = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

st.title("Loan dashboard")
''
''
st.header("Total income bar chart")
st.bar_chart(
    data = data,
    x = "gender",
    y = "total_income",
    x_label = "Gender",
    y_label = "Total income",
)
''
''
st.header("Gender bar chart")
st.bar_chart(
    data = data,
    x = "gender",
    y = "gender_count",
    x_label = "Gender",
    y_label = "Total income",
)