import yfinance as yf
import pandas as pd

def generate_signals(df, fast_window, slow_window):
    """
    Takes a DataFrame with OHLCV data, calculates SMAs, 
    and generates BUY/SELL signals based on the Golden Cross.
    """
    # 1. Calculate the Math
    df["Fast_SMA"] = df["Close"].rolling(window=fast_window).mean()
    df["Slow_SMA"] = df["Close"].rolling(window=slow_window).mean()

    # 2. Setup the Signal Column (Default everything to HOLD)
    df["Trade_Signal"] = "HOLD"

    # 3. The BUY Signal (Golden Cross)
    # Logic: Fast crosses ABOVE Slow today, but was BELOW or EQUAL yesterday
    df.loc[
        (df["Fast_SMA"] > df["Slow_SMA"]) & (df["Fast_SMA"].shift(1) <= df["Slow_SMA"].shift(1)),
        "Trade_Signal"
    ] = "BUY"

    # 4. The SELL Signal (Death Cross)
    # Logic: Fast crosses BELOW Slow today, but was ABOVE or EQUAL yesterday
    df.loc[
        (df["Fast_SMA"] < df["Slow_SMA"]) & (df["Fast_SMA"].shift(1) >= df["Slow_SMA"].shift(1)),
        "Trade_Signal"
    ] = "SELL"

    return df

# Execution block
if __name__ == "__main__":
    print("Fetching 1 Year of AAPL data for Strategy Test...\n")
    
    # 1. Download the Data
    test_df = yf.Ticker("AAPL").history(period="1y")

    # 2. Run the data through the strategy engine
    result_df = generate_signals(test_df, fast_window=20, slow_window=50)

    # 3. Filter out the boring days and only look at the action
    trades = result_df[result_df["Trade_Signal"] != "HOLD"]
    
    print("=== STRATEGY ENGINE: GOLDEN CROSS ===")
    print(f"Total crossover events found: {len(trades)}")
    print("-" * 37)
    
    if len(trades) > 0:
        # Print the exact dates, prices, and signals
        print(trades[["Close", "Fast_SMA", "Slow_SMA", "Trade_Signal"]])
    
    print("=====================================\n")