import matplotlib.pyplot as plt
import seaborn as sns

# Exploratory Data Analysis (EDA)
# Plot the cumulative sales over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Date', y='Sales_USD_cumsum')
plt.title('Cumulative Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Sales (USD)')
plt.show()

# Plot the number of sales over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Date', y='Number_of_Sales_cumsum')
plt.title('Cumulative Number of Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Number of Sales')
plt.show()

# Correlation matrix
corr_matrix = df[['Sales_USD', 'Number_of_Sales', 'Active_Market_Wallets']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()