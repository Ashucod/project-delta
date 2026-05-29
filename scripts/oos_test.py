# scripts/oos_test.py
import yfinance as yf
import pandas as pd
from strategy import generate_signals

def run_oos_test():
    print("--- OUT-OF-SAMPLE TEST: AAPL (Jan 2022 - Jan 2024) ---")
    print("Testing locked 6/36 parameters on unseen historical data...\n")
    
    # 1. Fetch data from the past (The Blind Test)
    df = yf.Ticker("AAPL").history(start="2022-01-01", end="2024-01-01")
    
    # 2. Generate signals using our locked-in 6/36 parameters
    df = generate_signals(df, fast_window=6, slow_window=36)
    
    # 3. Setup the Bank Account
    starting_capital = 10000.0
    cash = starting_capital
    shares = 0
    trades = df[df['Trade_Signal'] != 'HOLD']
    
    # 4. The Execution Loop
    for date, row in trades.iterrows():
        price = row['Close']
        signal = row['Trade_Signal']
        
        if signal == 'BUY' and cash > price:
            shares = int(cash // price)
            cash -= (shares * price)
            print(f"[{date.date()}] BUY  {shares} shares @ ${price:.2f}")
        elif signal == 'SELL' and shares > 0:
            cash += (shares * price)
            print(f"[{date.date()}] SELL {shares} shares @ ${price:.2f}")
            shares = 0
            
    # 5. Final Calculations
    final_price = df.iloc[-1]['Close']
    if shares > 0:
        portfolio_value = cash + (shares * final_price)
    else:
        portfolio_value = cash
        
    profit = portfolio_value - starting_capital
    roi = (profit / starting_capital) * 100
    
    print("\n" + "="*35)
    print(f"OOS FINAL VALUE : ${portfolio_value:,.2f}")
    print(f"OOS NET PROFIT  : ${profit:,.2f} ({roi:.2f}%)")
    print("="*35 + "\n")

if __name__ == "__main__":
    run_oos_test()