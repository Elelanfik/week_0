EDA Analysis for Solar Irradiance Dataset
This repository contains the Exploratory Data Analysis (EDA) conducted on a dataset related to solar irradiance, weather, and sensor measurements. The analysis aims to uncover patterns, clean the data, and gain insights for further modeling or use cases.

Main Branch: Contains the finalized code and results for the EDA analysis.
task-1 Branch: Dedicated to Day 1 analysis, focusing on initial EDA tasks like summary statistics, data cleaning, and plotting.

Summary Statistics:

Compute mean, median, standard deviation, and other statistical measures for numeric columns like GHI, DNI, DHI, Tamb, etc.
Data Quality Check:

Identify missing values and outliers.
Handle incorrect entries (e.g., negative values in solar radiation or wind speed columns).
Time Series Analysis:

Analyze trends and seasonal patterns in variables like GHI, DNI, DHI, and Tamb.
Evaluate the effect of cleaning (Cleaning column) on sensor readings (ModA, ModB).
Correlation Analysis:

Explore relationships between variables like solar radiation components (GHI, DNI, DHI), module temperatures (TModA, TModB), and wind conditions (WS, WSgust, WD).
Wind Analysis:

Create wind roses or radial bar plots to identify wind speed and direction patterns.
Temperature Analysis:

Investigate how relative humidity (RH) influences temperature readings (Tamb, TModA, TModB) and solar radiation (GHI, DNI, DHI).
Histograms:

Generate histograms for variables like GHI, DNI, WS, and temperatures to visualize data distributions.
Z-Score Analysis:

Use Z-scores to detect and flag anomalies in the data.
Bubble Charts:

Explore relationships between GHI, Tamb, WS, and additional variables like RH or BP.
Data Cleaning:

Handle missing values and anomalies, especially in key columns like Comments.
Steps to Reproduce
