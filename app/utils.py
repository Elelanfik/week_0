import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from windrose import WindroseAxes

# Load data
def load_data(file):
    """
    Load a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(file)

# Clean data
def clean_data(df):
    """
    Perform basic cleaning steps on the data, such as handling NaNs.
    """
    # Drop rows with missing values
    df = df.dropna()
    
    # Optional: Add additional cleaning steps as required
    # For example, ensure specific columns are numeric
    return df

# Plot histogram
def plot_histogram(df, column):
    """
    Plot a histogram for a given column in the DataFrame.
    """
    plt.figure(figsize=(6, 4))
    sns.histplot(df[column], kde=True, bins=30, color='skyblue')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

# Plot correlation matrix
def plot_correlation_matrix(df):
    """
    Plot a correlation matrix for the numerical columns in the DataFrame.
    """
    plt.figure(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    plt.title("Correlation Matrix")

# Plot scatter matrix
def plot_scatter_matrix(df, columns):
    """
    Plot a scatter matrix for selected columns in the DataFrame.
    """
    sns.pairplot(df[columns], diag_kind='kde', corner=True)
    plt.suptitle("Scatter Matrix", y=1.02)

# Plot wind rose
from windrose import WindroseAxes
import matplotlib.pyplot as plt
import numpy as np

def plot_wind_rose(df):
    # Ensure wind speed and direction are numeric
    df['WS (m/s)'] = pd.to_numeric(df['WS (m/s)'], errors='coerce')
    df['WD (°N (to east))'] = pd.to_numeric(df['WD (°N (to east))'], errors='coerce')
    
    # Extract wind speed and direction
    wind_speed = df['WS (m/s)']
    wind_direction = df['WD (°N (to east))']

    # Create the wind rose plot
    fig = plt.figure(figsize=(8, 8))
    ax = WindroseAxes.from_ax(fig=fig)
    ax.bar(wind_direction, wind_speed, bins=np.arange(0, 15, 1), 
           normed=True, opening=0.8, edgecolor='white')
    ax.set_title('Wind Rose: Wind Speed and Direction Distribution')
    
    return fig

# Plot bubble chart
def plot_gathered_data(df):
    """
    Create a bubble chart: GHI vs Tamb vs Wind Speed, with bubble size representing RH.
    """
    # Check if required columns exist
    required_columns = ['GHI', 'Tamb', 'wind_speed', 'RH']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' is missing from the data.")

    # Create a bubble chart using Plotly
    fig = px.scatter(
        df,
        x='GHI',
        y='Tamb',
        size='RH',
        color='wind_speed',
        hover_data=df.columns,
        labels={'GHI': 'Global Horizontal Irradiance (GHI)', 
                'Tamb': 'Ambient Temperature (°C)', 
                'wind_speed': 'Wind Speed (m/s)',
                'RH': 'Relative Humidity (%)'},
        title="GHI vs Tamb vs Wind Speed (Bubble Size = RH)"
    )
    fig.update_layout(template="plotly_white", title_x=0.5)
    return fig
