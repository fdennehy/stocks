#! /usr/bin/env python

# Financial Data 
import yfinance as yf

# Dates and Times
import datetime as dt

# Get data for Microsoft, Apple and Google.
tickers = ['MSFT', 'AAPL', 'GOOG']
df = yf.download(tickers, period="1d", interval="1m")

# Get the current date and time.
filename = dt.datetime.now()
# Create a string format from the current date and time.
filename = filename.strftime("%Y%m%d_%H%M%S") 
# Prepend data folders, append file extension.
filename = 'data/' + filename + ".csv"

# Save the data to a CSV file.
df['Close'].to_csv(filename)
