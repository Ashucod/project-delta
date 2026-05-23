# Project Delta — Historical Time Series Engine
import yfinance as yf
import pandas as pd

def fetch_history(ticker_symbol, period="1mo"):
    print(f"\nFetching {period} of Time Series data for {ticker_symbol}...")
    
    # 1. Target the stock
    ticker = yf.Ticker(ticker_symbol)
    
    # 2. Pull the historical data (Returns a pandas DataFrame)
    hd = ticker.history(period=period)
    
    # 3. Print the last 5 days of data using the pandas .tail() function
    print("="*84 + "\n")
    print(hd.tail())
    print("\n" + "="*84)

if __name__ == "__main__":
    fetch_history("AAPL", "1mo")