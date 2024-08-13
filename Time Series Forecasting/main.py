import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

# Load the dataset
file_path = "vegetables_fruits.csv"  # Replace with your actual file path
df = pd.read_csv(file_path)

# Convert the Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], format = "%Y-%m-%d")  # Adjust the format if necessary

# Set the Date column as the index
df.set_index("Date", inplace = True)

# Remove duplicate entries by keeping the first occurrence
df = df[~df.index.duplicated(keep = "first")]

# Set the frequency of the index (e.g., daily). Adjust 'D' to your data's frequency if needed.
df = df.asfreq("D")

# Display the first few rows of the DataFrame
print(df.head())

# Visualize the Average price over time for the entire dataset
plt.figure(figsize = (10, 6))
plt.plot(df.index, df["Average"], marker = "o", linestyle = "-")
plt.title("Average Price of Commodities Over Time")
plt.xlabel("Date")
plt.ylabel("Average Price")
plt.grid(True)
plt.show()

# Train-Test Split (e.g., using the last 20% of data as the test set)
train_size = int(len(df) * 0.8)
train, test = df["Average"].iloc[:train_size], df["Average"].iloc[train_size:]

# Manually specify ARIMA parameters (p, d, q)
model = ARIMA(train, order = (5, 1, 0))  # You can change these parameters
model_fit = model.fit()

# Make predictions
predictions = model_fit.forecast(steps = len(test))

# Handle missing values in test and predictions
test = test.dropna()
predictions = pd.Series(predictions, index = test.index).ffill()

# Calculate error
error = mean_squared_error(test, predictions)
print(f"Test MSE: {error}")

# Plot predictions vs actual
plt.figure(figsize = (10, 6))
plt.plot(train.index, train, label = "Training Data")
plt.plot(test.index, test, label = "Test Data")
plt.plot(test.index, predictions, label = "Predicted Data", color = "red")
plt.title("Average Price Prediction")
plt.xlabel("Date")
plt.ylabel("Average Price")
plt.legend()
plt.grid(True)
plt.show()

# Forecast future values (e.g., next 30 days)
future_steps = 30
future_predictions = model_fit.forecast(steps = future_steps)

# Plot the forecast
plt.figure(figsize = (10, 6))
plt.plot(df.index, df["Average"], label = "Historical Data")
plt.plot(pd.date_range(df.index[-1], periods = future_steps, freq = "D"),
         future_predictions, label = "Future Predictions", color = "red")
plt.title("Future Price Prediction")
plt.xlabel("Date")
plt.ylabel("Average Price")
plt.legend()
plt.grid(True)
plt.show()
