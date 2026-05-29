import yfinance as yf
import pandas as pd
from strategy import generate_signals

def run_backtest(ticker, period, starting_capital):
    print(f"---INITIALIZING BACKTEST FOR {ticker}---")
    print(f"Starting capital: ${starting_capital}\n")

    raw_data = yf.Ticker(ticker).history(period=period)
    df = generate_signals(raw_data)

    cash = starting_capital
    shares = 0

    trades = df[df["Trade_Signal"] != "HOLD"]

    for date, row in trades.iterrows():
        price = row['Close']
        signal = row['Trade_Signal']

        if signal == "BUY" and cash >= price:
            shares = int(cash // price)
            cost = shares * price
            cash = cash - cost
            print(f"[{date.date()}] BUY  {shares} shares @ ${price:.2f} | Remaining Cash: ${cash:.2f}")

        elif signal == "SELL" and shares > 0:
            sale_value = shares * price
            cash = cash + sale_value
            print(f"[{date.date()}] SELL {shares} shares @ ${price:.2f} | New Cash: ${cash:,.2f}")
            shares = 0

    final_value = df.iloc[-1]['Close']
    if shares > 0:
        portfolio_value = cash + (shares * final_value)
    else:
        portfolio_value = cash

    profit = portfolio_value - starting_capital
    roi = (profit / starting_capital) * 100

    print("\n" + "="*35)
    print(f"FINAL PORTFOLIO VALUE : ${portfolio_value:,.2f}")
    print(f"TOTAL NET PROFIT      : ${profit:,.2f}")
    print(f"RETURN ON INVESTMENT  : {roi:.2f}%")
    print("="*35 + "\n")

if __name__ == "__main__":
    run_backtest("AAPL", "1y", 10000.0)