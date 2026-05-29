import yfinance as yf
import pandas as  pd
from strategy import generate_signals

def fast_backtest(df, starting_capital):
    """A stripped-down, lightning-fast version of your backtester just for calculating final PnL."""
    cash = starting_capital
    shares = 0

    trades = df[df["Trade_Signal"] != "HOLD"]

    for date, row in trades.iterrows():
        price = row['Close']
        signal = row['Trade_Signal']

        if signal == "BUY" and cash > price:
            shares = int(cash // price)
            cash -= shares*price
        elif signal == "SELL" and shares > 0:
            cash += shares*price
            shares = 0

    final_price = df.iloc[-1]['Close']
    if shares > 0:
        portfolio_value = cash + (shares * final_price)
    else:
        portfolio_value = cash

    return portfoilio_value - starting_capital


if __name__ == "__main__":
    print(("--- STARTING BRUTE-FORCE OPTIMIZATION (AAPL 1Y) ---\n"))

    best_profit = -999999
    best_fast = 0
    best_slow = 0

    # THE NESTED LOOP
    # Test every fast line from 5 to 30 days
    for fast in range(5, 31):
        # Test every slow line from 35 to 90 days
        for slow in range(35, 91):
            
            # Make a fresh copy of the data
            df_copy = raw_data.copy()
            
            # Run the strategy and the backtest
            df_signals = generate_signals(df_copy, fast_window=fast, slow_window=slow)
            profit = fast_backtest(df_signals)
            
            # If this combination beat our previous high score, save it!
            if profit > best_profit:
                best_profit = profit
                best_fast = fast
                best_slow = slow
                print(f"New High Score! {fast}/{slow} Cross -> Profit: ${profit:,.2f}")

    print("\n" + "="*40)
    print("🏆 OPTIMIZATION COMPLETE")
    print(f"Best Parameters : {best_fast}-Day / {best_slow}-Day Cross")
    print(f"Maximized Profit: ${best_profit:,.2f}")
    print("="*40 + "\n")
