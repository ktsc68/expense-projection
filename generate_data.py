import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
dates = pd.date_range(start='2020-01-01', periods=48, freq='M')
expenses = np.random.normal(loc=5000, scale=200, size=len(dates))
gdp = np.random.normal(loc=20000, scale=500, size=len(dates))

data = pd.DataFrame({'Date': dates, 'Expenses': expenses, 'GDP': gdp})
data.set_index('Date', inplace=True)
data.to_csv('synthetic_data.csv')

print("Synthetic data has been generated and saved to 'synthetic_data.csv'.")
