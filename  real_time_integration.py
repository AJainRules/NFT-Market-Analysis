import pandas as pd
from datetime import datetime, timedelta

# Load the existing dataset
df = pd.read_csv('/Users/apjain/Documents/NFT Project/NFTlyze Dataset.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

def fetch_mock_real_time_data():
    # Generate mock data for the next 7 days
    base_date = df['Date'].max() + timedelta(days=1)
    mock_data = []
    for i in range(7):
        date = base_date + timedelta(days=i)
        sales_usd = 1000 + i * 100  # Example incremental sales
        number_of_sales = 10 + i  # Example incremental sales number
        active_market_wallets = 5 + i  # Example incremental wallets
        primary_sales = 2 + i  # Example incremental primary sales
        mock_data.append({
            'Date': date,
            'Sales_USD': sales_usd,
            'Number_of_Sales': number_of_sales,
            'Active_Market_Wallets': active_market_wallets,
            'Primary_Sales': primary_sales
        })
    return mock_data

# Fetch mock real-time data
real_time_data = fetch_mock_real_time_data()

# Convert real-time data to DataFrame
real_time_df = pd.DataFrame(real_time_data)

# Convert 'Date' column to datetime
real_time_df['Date'] = pd.to_datetime(real_time_df['Date'])

# Append real-time data to the existing dataset
updated_df = pd.concat([df, real_time_df], ignore_index=True)

# Display the updated dataset
print(updated_df.tail())

# Example: Displaying the updated cumulative sales over time
import matplotlib.pyplot as plt
import seaborn as sns

# Recalculate cumulative sales and number of sales
updated_df['Sales_USD_cumsum'] = updated_df['Sales_USD'].cumsum()
updated_df['Number_of_Sales_cumsum'] = updated_df['Number_of_Sales'].cumsum()

plt.figure(figsize=(10, 6))
sns.lineplot(data=updated_df, x='Date', y='Sales_USD_cumsum')
plt.title('Cumulative Sales Over Time (with Real-Time Data)')
plt.xlabel('Date')
plt.ylabel('Cumulative Sales (USD)')
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=updated_df, x='Date', y='Number_of_Sales_cumsum')
plt.title('Cumulative Number of Sales Over Time (with Real-Time Data)')
plt.xlabel('Date')
plt.ylabel('Cumulative Number of Sales')
plt.show()