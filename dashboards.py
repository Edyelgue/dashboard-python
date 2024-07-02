import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(layout="wide")

# Load your Excel file into a DataFrame
df = pd.read_excel("Base Vendas - 2020.xlsx")

# Display the DataFrame
st.write(df)


