import streamlit as st
import pandas as pd
from utils import load_data, clean_data, plot_histogram, plot_correlation_matrix, plot_scatter_matrix, plot_wind_rose, plot_gathered_data

# Title and description for the app
st.title('EDA Analysis for Moonlight Energy Solution')
st.write("""
    This dashboard allows you to visualize and analyze solar radiation, weather data, and sensor readings.
    You can explore relationships between variables such as GHI, DNI, temperature, wind conditions, and more.
""")

# File uploader for CSV file
uploaded_file = st.file_uploader("Upload your data CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Load and clean the data
        df = load_data(uploaded_file)
        
        # Debug: Ensure data is loaded
        st.write("Data Loaded Successfully!")
        st.write(f"Dataset Shape: {df.shape}")

        df = clean_data(df)

        # Debug: Ensure data is cleaned
        st.write("Data Cleaned Successfully!")
        st.write(f"Dataset Shape After Cleaning: {df.shape}")

        # Display a sample of the cleaned data
        st.subheader("Cleaned Data Sample")
        st.write(df.head())

        # Create and display histograms for key columns
        st.subheader("Distribution of GHI, DNI, DHI, and Temperature")
        
        col1, col2 = st.columns(2)
        with col1:
            plot_histogram(df, 'GHI (W/m²)')
            st.pyplot()

        with col2:
            plot_histogram(df, 'DNI (W/m²)')
            st.pyplot()


        # Wind Rose
        st.subheader("Wind Rose Analysis")
        wind_rose = plot_wind_rose(df)
        st.plotly_chart(wind_rose)

        # Correlation Heatmap
        st.subheader("Correlation Heatmap")
        columns_of_interest = ['GHI (W/m²)', 'DNI (W/m²)', 'DHI (W/m²)', 'TModA (°C)', 'TModB (°C)']
        heatmap_fig = plot_correlation_heatmap(df, columns_of_interest)
        st.pyplot(heatmap_fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a CSV file to get started.")
