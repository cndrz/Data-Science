import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def fetch_stock_data(ticker, start_date, end_date):
    try:
        stock_data = yf.download(ticker, start = start_date, end = end_date)
        if stock_data.empty:
            raise ValueError("No data found for the given ticker and date range.")
        return stock_data
    except Exception as e:
        raise ValueError(f"An error occurred while fetching the data: {e}")

def main():
    ticker = input("Enter Chosen Stock: ").strip().upper()
    
    while True:
        start_date = input("Enter Start Date in YYYY-MM-DD Format: ").strip()
        if validate_date(start_date):
            break
        else:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    while True:
        end_date = input("Enter End Date in YYYY-MM-DD Format: ").strip()
        if validate_date(end_date):
            break
        else:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    try:
        stock_data = fetch_stock_data(ticker, start_date, end_date)

        # Calculate the moving average
        stock_data["MA50"] = stock_data["Close"].rolling(window = 50).mean()
        
        # Calculate the daily returns
        stock_data["Daily Return"] = stock_data["Close"].pct_change()
        
        # Plot closing prices and moving average
        plt.figure(figsize = (14, 7))
        plt.plot(stock_data["Close"], label="Close Price")
        plt.plot(stock_data["MA50"], label="50-Day Moving Average")
        plt.title(f"{ticker} Stock Price")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.show()
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
