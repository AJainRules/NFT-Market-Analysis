import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from prophet import Prophet

# Load the dataset
df = pd.read_csv('/Users/apjain/Documents/NFT Project/NFTlyze Dataset.csvv')

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])