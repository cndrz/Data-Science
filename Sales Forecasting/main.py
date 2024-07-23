import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Load the sales dataset
dataset = pd.read_csv("Sales Forecasting/sales.csv", parse_dates = ["ORDERDATE"], index_col = "ORDERDATE")
print(dataset.head())

# Check for missing values
print(dataset.isnull().sum())

# Fill or drop missing values
dataset = dataset.fillna(method = "ffill")

# Ensure the "SALES" column is numeric
dataset["SALES"] = pd.to_numeric(dataset["SALES"], errors = "coerce")

# Drop any remaining NaNs in "SALES" after conversion
dataset = dataset.dropna(subset = ["SALES"])

# Plot the sales data
plt.figure(figsize = (10, 6))
plt.plot(dataset["SALES"], label = "Sales")
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.show()

# Split the data into training and test sets
train_size = int(len(dataset) * 0.8)
train, test = dataset[:train_size], dataset[train_size:]

# Fit the ARIMA model
model = ARIMA(train["SALES"], order = (5, 1, 0))  # (p, d, q) parameters can be adjusted
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())

# Forecast sales
forecast = model_fit.forecast(steps = len(test))
test["Forecast"] = forecast.values

# Calculate the error
error = mean_squared_error(test["SALES"], test["Forecast"])
print(f"Mean Squared Error: {error}")

# Predict future sales
future_steps = 12  # Number of months to forecast
future_forecast = model_fit.forecast(steps = future_steps)
future_dates = pd.date_range(start = test.index[-1], periods = future_steps, freq = "M")
future_sales = pd.DataFrame(future_forecast, index = future_dates, columns = ["Forecast"])

# Plot the actual vs predicted sales
plt.figure(figsize = (10, 6))
plt.plot(train.index, train["SALES"], label = "Train")
plt.plot(test.index, test["SALES"], label = "Test")
plt.plot(test.index, test["Forecast"], label = "Forecast")
plt.plot(future_sales.index, future_sales["Forecast"], label = "Future Forecast")
plt.title("Sales Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.show()
