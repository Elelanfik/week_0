# main.py
import streamlit as st
import pandas as pd
from utils import load_data, clean_data, plot_histogram, plot_correlation_matrix, plot_scatter_matrix, plot_wind_rose, plot_gathered_data

# Title and description for the app
st.title('Solar and Weather Data Analysis')
st.write("""
    This dashboard allows you to visualize and analyze solar radiation, weather data, and sensor readings.
    You can explore relationships between variables such as GHI, DNI, temperature, wind conditions, and more.
""")

# File uploader for CSV file
uploaded_file = st.file_uploader("Upload your data CSV file", type=["csv"])

if uploaded_file is not None:
    # Load and clean the data
    df = load_data(uploaded_file)
    df = clean_data(df)
    
    st.write("Data Loaded and Cleaned Successfully")

    # Display a sample of the cleaned data
    st.subheader("Cleaned Data Sample")
    st.write(df.head())

    # Create and display histograms for key columns
    st.subheader("Distribution of GHI, DNI, DHI, and Temperature")
    
    col1, col2 = st.columns(2)
    with col1:
        plot_histogram(df, 'GHI')
        st.pyplot()

    with col2:
        plot_histogram(df, 'DNI')
        st.pyplot()

    st.subheader("Correlation Matrix")
    plot_correlation_matrix(df)
    st.pyplot()

    # Scatter matrix to explore relationships between multiple variables
    st.subheader("Scatter Matrix")
    plot_scatter_matrix(df, ['GHI', 'DNI', 'ModA', 'ModB', 'Tamb'])
    st.pyplot()

    # Wind Rose
    st.subheader("Wind Rose Analysis")
    wind_rose = plot_wind_rose(df)
    st.plotly_chart(wind_rose)

    # Bubble chart for GHI vs Tamb vs Wind Speed with bubble size representing RH
    st.subheader("Bubble Chart: GHI vs Tamb vs Wind Speed")
    bubble_chart = plot_gathered_data(df)
    st.plotly_chart(bubble_chart)
