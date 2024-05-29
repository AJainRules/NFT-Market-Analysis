import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# ARIMA Model
# Prepare data for ARIMA model
df.set_index('Date', inplace=True)
df_sales = df['Sales_USD'].dropna()  # Drop NA values for sales

# Train ARIMA model
model_arima = ARIMA(df_sales, order=(5,1,0))
model_fit_arima = model_arima.fit()
print(model_fit_arima.summary())

# Forecast future sales
forecast_arima = model_fit_arima.forecast(steps=30)
forecast_dates_arima = pd.date_range(start=df_sales.index[-1], periods=30, freq='D')

plt.figure(figsize=(10, 6))
plt.plot(df_sales.index, df_sales, label='Actual Sales')
plt.plot(forecast_dates_arima, forecast_arima, label='Forecasted Sales', color='red')
plt.title('ARIMA Forecast of NFT Sales')
plt.xlabel('Date')
plt.ylabel('Sales (USD)')
plt.legend()
plt.show()

# Evaluate ARIMA model
mse_arima = mean_squared_error(df_sales[-30:], forecast_arima[:30])
print(f'ARIMA Model Mean Squared Error: {mse_arima}')

# Prophet Model
# Prepare data for Prophet model
df_prophet = df.reset_index().rename(columns={'Date': 'ds', 'Sales_USD': 'y'})

# Train Prophet model
model_prophet = Prophet()
model_prophet.fit(df_prophet)

# Forecast future sales
future_prophet = model_prophet.make_future_dataframe(periods=30)
forecast_prophet = model_prophet.predict(future_prophet)

# Plot forecast
fig = model_prophet.plot(forecast_prophet)
plt.title('Prophet Forecast of NFT Sales')
plt.xlabel('Date')
plt.ylabel('Sales (USD)')
plt.show()