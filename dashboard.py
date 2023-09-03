import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

# Load the config file
with open('config.json', 'r') as f:
    config = json.load(f)

# Load CSV files based on the config
def load_csv(file_path):
    return pd.read_csv(file_path)

dataframes = {key: load_csv(value) for key, value in config.items()}

# Streamlit app
st.title('Time Series Dashboard')

# Create a 2x2 grid for the plots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plotting the time series
for i, (key, df) in enumerate(dataframes.items()):
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    row = i // 2
    col = i % 2
    axs[row, col].plot(x, y)
    axs[row, col].set_title(config[key])
    axs[row, col].set_xlabel(df.columns[0])
    axs[row, col].set_ylabel(df.columns[1])

plt.tight_layout()
st.pyplot(fig)
