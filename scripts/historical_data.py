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

ticker = yf.Ticker("AAPL")
df = ticker.history(period="6mo")

# Drop columns you won't use at this stage
df = df.drop(columns=["Dividends", "Stock Splits"])
# -----------------------------------------------------------------------------------------------------
# print(df.shape)    # (rows, columns) — e.g. (126, 5)
# print(df.columns)  # Index(['Open', 'High', 'Low', 'Close', 'Volume'])

# print(df.head(3))
# print(df.tail(3))

# -----------------------------------------------------------------------------------------------------
close_prices = df["Close"]
volume = df["Volume"]

# print(close_prices.tail(3))
# -----------------------------------------------------------------------------------------------------
# price_table = df[["Open", "Close", "Volume"]]
# print(price_table.tail(3))
# -----------------------------------------------------------------------------------------------------
# print(df.iloc[0])     # first row — oldest trading day
# print(df.iloc[-1])    # last row  — most recent trading day
# print(df.iloc[-5:])   # last 5 rows — same as tail(5)
# -----------------------------------------------------------------------------------------------------
latest_close  = df.iloc[-1]["Close"]    # most recent closing price
first_open    = df.iloc[0]["Open"]      # first opening price in dataset

# print(f"Latest close : ${latest_close:.2f}")
# print(f"First open   : ${first_open:.2f}")
# -----------------------------------------------------------------------------------------------------
df["Daily_Return"] = df["Close"].pct_change()

# print(df[["Close", "Daily_Return"]].tail(5))
# -----------------------------------------------------------------------------------------------------
total_return = (df["Close"].iloc[-1] - df["Close"].iloc[0]) / df["Close"].iloc[0] * 100
# print(f"AAPL 6-month return: {total_return:.2f}%")
# -----------------------------------------------------------------------------------------------------
# Simple Moving Averages
df["SMA_20"] = df["Close"].rolling(window=20).mean()
df["SMA_50"] = df["Close"].rolling(window=50).mean()

# Rolling volatility — standard deviation of daily returns
df["Volatility_20"] = df["Daily_Return"].rolling(window=20).std()

# print(df[["Close", "SMA_20", "SMA_50", "Volatility_20"]].tail(5))
# -----------------------------------------------------------------------------------------------------
    # Days where volume was above 100 million
high_vol_days = df[df["Volume"] > 100_000_000]
# print(f"High Volume Days : {len(high_vol_days)}")
# print(high_vol_days[["Close", "Volume"]])

    # Days where price was above SMA_20 - uptrend filter
uptrend_days = df[df["Close"] > df["SMA_20"]]
# print(f"Days of uptrend : {len(uptrend_days)}")

    # Strong Days
strong_days = df[(df["Close"] > df["SMA_20"]) & (df["Volume"] > 80_000_000)]
# print(f"Strong Days : {len(strong_days)}")
# print(strong_days[["Close", "SMA_20", "Volume"]])
# ------------------------------------------------------------------------------------------------------------------------------------------
# Classy each day's return as UP, DOWN or FLAT
def classify_day(return_val):
    if pd.isna(return_val):
        return "N/A"
    elif return_val > 0.01:
        return "STRONG UP"
    elif return_val > 0:
        return "UP"
    elif return_val < -0.01:
        return "STRONG DOWN"
    else:
        return "DOWN"
    
df["Signal"] = df["Daily_Return"].apply(classify_day)
# print(df[["Close", "Daily_Return", "Signal"]].tail(8))
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
