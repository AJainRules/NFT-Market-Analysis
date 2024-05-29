**NFT Market Analysis**

This project analyzes trends in the NFT (Non-Fungible Token) market using various techniques including exploratory data analysis (EDA), ARIMA modeling, and Prophet forecasting. It also integrates real-time data updates and visualizes the results through a dashboard.

Installation

Before running the project, make sure you have the necessary dependencies installed. You can install them using pip:

**bash**
pip install prophet pandas matplotlib seaborn statsmodels scikit-learn dash plotly

**Usage**

**Exploratory Data Analysis (EDA):**

Load the dataset from 'NFTlyze Dataset.csv'.
Convert the 'Date' column to datetime format.
Plot cumulative sales and the number of sales over time.
Visualize the correlation matrix.

**ARIMA Modeling:**

Prepare data for the ARIMA model.
Train the ARIMA model with the specified order.
Forecast future sales using the trained model.
Evaluate the ARIMA model's performance.
Prophet Forecasting:

Prepare data for the Prophet model.
Train the Prophet model.
Forecast future sales using the trained model.
Evaluate the Prophet model's performance.
Real-time Data Integration:

Fetch mock real-time data for the next 7 days.
Append the real-time data to the existing dataset.
Display the updated cumulative sales and number of sales over time.

**Dashboard:**

Run the dashboard application to visualize NFT sales over time.
The dashboard updates every minute with new data.

**Files**

**EDA_and_Forecasting.ipynb: Jupyter notebook containing exploratory data analysis and forecasting code.
data_collection.py: Python script for fetching mock real-time data.
exploratory_data_analysis.py: Python script for exploratory data analysis plotting functions.
forecasting.py: Python script for ARIMA modeling and Prophet forecasting.
real_time_integration.py: Python script for integrating real-time data into the dataset.
dashboard.py: Python script for running the dashboard application.**

**Dataset**

The dataset used for analysis is located at 'NFTlyze Dataset.csv'.

