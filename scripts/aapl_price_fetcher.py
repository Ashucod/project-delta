# Project Delta - Live Market Data Fetcher
import yfinance as yf

#  1. Target the stock
ticker = yf.Ticker("AAPL")

# 2. Pull the data dictionary
info = ticker.info

# 3. Print the signals
print("=== AAPL LIVE DATA ===")
print(f"Company : {info.get('longName', 'N/A')}")
print(f"Price   : ${info.get('currentPrice', 'N/A')}")
print(f"Volume  : {info.get('volume', 'N/A'):,}")
print(f"Mkt Cap : ${info.get('marketCap', 0) / 1e9:.2f}B")
print("======================")

