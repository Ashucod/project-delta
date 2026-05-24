# Project Delta - Live Market Data Fetcher
import yfinance as yf

#  1. Target the stock
ticker = yf.Ticker("AAPL")

# 2. Pull the data dictionary
info = ticker.info
fast = ticker.fast_info

# 3. Print the signals
# print("=== AAPL LIVE DATA ===")
# print(f"Company : {info.get('longName', 'N/A')}")
# print(f"Price   : ${info.get('currentPrice', 'N/A')}")
# print(f"Volume  : {info.get('volume', 'N/A'):,}")
# print(f"Mkt Cap : ${info.get('marketCap', 0) / 1e9:.2f}B")
# print("======================")

# 4. Print the fast info
print("=== AAPL FAST INFO ===")
print(f"Price   : ${fast.last_price if fast.last_price is not None else 'N/A'}")
print(f"Volume  : {fast.last_volume if fast.last_volume is not None else 'N/A':,}")
print("======================")
