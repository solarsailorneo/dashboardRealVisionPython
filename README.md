# Time Series Dashboard with Streamlit

This is a simple Streamlit dashboard that visualizes time series data from CSV files. The dashboard displays four time series plots in a 2x2 grid, with data sourced from CSV files specified in a JSON config file.

## Prerequisites

- Python 3.x
- Streamlit
- Pandas
- Matplotlib

## Installation

1. **Clone the Repository** (if you have your code in a repository):
   ```bash
   git clone https://github.com/solarsailorneo/dashboard.rv.py
   cd dashboard.rv.py
   ```

2. **Install Required Libraries**:
   You can install the necessary libraries using pip:
   ```bash
   pip install streamlit pandas matplotlib
   ```

## Configuration

1. **Update the `config.json` File**:
   Modify the `config.json` file to specify the paths to your CSV files and the desired title for each plot. The structure should be as follows:

```json
{
   "file1": "sample1.csv",
   "file2": "sample2.csv",
   ...
}
```

2. **CSV File Format**:
   Each CSV file should have two columns: the first representing the independent variable (e.g., dates) and the second representing the dependent variable (e.g., some metric). For example:

```
Time,Value
2023-01-01,100
2023-01-02,105
...
```

## Usage

1. **Run the Streamlit App**:
   In your terminal or command prompt, navigate to the directory containing `dashboard.py` and run:
   ```bash
   streamlit run dashboard.py
   ```

2. **View the Dashboard**:
   Streamlit will automatically open a new browser window or tab with the dashboard. If not, you can manually navigate to the provided local URL (usually `http://localhost:8501`).

