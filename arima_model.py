import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load the synthetic data
data = pd.read_csv('synthetic_data.csv', index_col='Date', parse_dates=True)

# Fit the ARIMA model
model = SARIMAX(data['Expenses'], exog=data['GDP'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()

# Forecast future expenses
forecast = results.get_forecast(steps=12, exog=data['GDP'][-12:])
forecast_df = forecast.conf_int()
forecast_df['Forecast'] = results.predict(start=forecast_df.index[0], end=forecast_df.index[-1], exog=data['GDP'][-12:])
print(forecast_df)

