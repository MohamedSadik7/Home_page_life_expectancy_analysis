
import streamlit as st
import plotly.express as px
import pandas as pd

# Set the page configuration
st.set_page_config(
    layout="wide",
    page_title='Life Expectancy Homepage',
    page_icon='🏠'
)

# Load the dataset
df = pd.read_csv("cleaned_life_expectancy.csv")
df.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')

st.sidebar.success('Select Page Above!')
st.sidebar.title("Life Expectancy Stats Project")
x = st.sidebar.toggle("Show Data & Insights")

# Sidebar: Dataset Overview

st.sidebar.subheader("📄 Dataset Overview")
st.sidebar.write("This dataset brings together years of structured data, making it possible to explore how life expectancy and socio-economic factors have evolved over time. Each record captures a specific country in a given year, painting a detailed picture of global health and economic conditions. Through this analysis, I aim to uncover meaningful insights into what truly impacts life expectancy worldwide.")
st.sidebar.markdown(f"**Total Records:** {len(df)} | **Total Features:** {len(df.columns)}")
    

st.markdown('<h1 style="text-align: center; color : darkblue; font-size: 36px;">📉 Life Expectancy Dashboard</h1>', unsafe_allow_html=True)


col1, col2 = st.columns([4, 2])


with col1:
    if x:
        st.markdown('<h3 style="text-align: center; color : MediumAquaMarine;">Dataset Overview</h3>', unsafe_allow_html=True)
        st.dataframe(df, height=500)


with col2:
    if x:
        st.subheader("🔢 Key Statistics")
        st.metric(label="📝 Total Rows", value=len(df), delta=None, help="Total number of records in the dataset", delta_color="normal")
        st.metric(label="📊 Total Columns", value=len(df.columns), delta=None, help="Number of columns in the dataset", delta_color="normal")
        st.metric(label="🗺️ Total Countries", value=df['Country Name'].nunique(), delta=None, delta_color="normal")
        st.metric(label="⬇ Earliest Year", value=int(df['Year'].min()), delta=None, delta_color="normal")
        st.metric(label="⬆ Latest Year", value=int(df['Year'].max()), delta=None, delta_color="normal")


