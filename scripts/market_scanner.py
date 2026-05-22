# Project Delta - V2 Multi-Ticker Scanner
import yfinance as yf

def scan_market():
    # 1. The Target List
    watchlist = ["AAPL", "MSFT", "NVDA", "TSLA", "SPY"]

    # 2. The Dashboard Header
    print("\n" + "="*47)
    print(" PROJECT DELTA: LIVE MARKET SCANNER")
    print("="*47)
    print(f"{'TICKER':<10} | {'PRICE':>12} | {'VOLUME':>15}")
    print("-"*47)

    # 3. The Execution Loop
    for ticker_symbol in watchlist:
        try:
            # Fetch Data
            ticker = yf.Ticker(ticker_symbol)
            info = ticker.info
            
            # Extract signals (using .get() with fallbacks to prevent crashes)
            # Sometimes Yahoo uses 'regularMarketPrice' when 'currentPrice' is missing
            price = info.get('currentPrice', info.get('regularMarketPrice', 0.0))
            volume = info.get('volume', info.get('regularMarketVolume', 0.0))

            # 4. The Formatted Output
            print(f"{ticker_symbol:<10} | ${price:>11.2f} | {volume:>15,}")
            
        except Exception as e:
            # If ONE ticker fails, catch the error, print a warning, and keep the loop alive
            print(f"{ticker_symbol:<10} | {'ERROR':>12} | {'NO DATA':>15}")

    print("="*47 + "\n")

# The Main Gatekeeper
if __name__ == "__main__":
    scan_market()