import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch sample historical data for Apple Inc. (AAPL)
ticker = input("Enter Chosen Stock: ")
stock_data = yf.download(ticker, start = "2013-01-01", end = "2023-01-01")

# Calculate the moving average
stock_data["MA50"] = stock_data["Close"].rolling(window = 50).mean()

# Calculate the daily returns
stock_data["Daily Return"] = stock_data["Close"].pct_change()

# Plot closing prices and moving average
plt.figure(figsize = (14, 7))
plt.plot(stock_data["Close"], label = "Close Price")
plt.plot(stock_data["MA50"], label ="50-Day Moving Average")
plt.title(f"{ticker} Stock Price")
plt.xlabel("Date")
plt.ylabel("rice")
plt.legend()
plt.show()