import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

# Load the config file
with open('config.json', 'r') as f:
    config = json.load(f)

# Load CSV files based on the config
def load_csvs(file_paths):
    return [pd.read_csv(file_path) for file_path in file_paths]

dataframes = {key: load_csvs(value) for key, value in config.items()}

# Streamlit app
st.title('Time Series Dashboard')

# Create a 2x2 grid for the plots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plotting the time series
for i, (key, dfs) in enumerate(dataframes.items()):
    row = i // 2
    col = i % 2
    
    for df in dfs:
        x = df.iloc[:, 0]
        y = df.iloc[:, 1]
        axs[row, col].plot(x, y, label=df.columns[1])
    
    axs[row, col].set_title(key)
    axs[row, col].set_xlabel(dfs[0].columns[0])  # Assuming x-label is same for both time series
    axs[row, col].legend()

plt.tight_layout()
st.pyplot(fig)
