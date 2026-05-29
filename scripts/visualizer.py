# scripts/visualizer.py
import os
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from strategy import generate_signals

def draw_chart():
    print("--- GENERATING TACTICAL VISUALIZATION ---")
    
    # 1. Fetch the exact OOS data we just tested
    df = yf.Ticker("AAPL").history(start="2022-01-01", end="2024-01-01")
    
    # 2. Run the strategy
    df = generate_signals(df, fast_window=6, slow_window=36)
    
    # 3. Setup the Canvas
    plt.figure(figsize=(16, 8))
    plt.title("Project Delta: 6/36 Golden Cross Strategy (AAPL OOS Test)", fontsize=16)
    plt.grid(True, alpha=0.3)
    
    # 4. Draw the core lines
    plt.plot(df.index, df['Close'], label='AAPL Price', color='gray', alpha=0.6, linewidth=1)
    plt.plot(df.index, df['Fast_SMA'], label='6-Day Fast SMA', color='blue', alpha=0.8, linewidth=1.5)
    plt.plot(df.index, df['Slow_SMA'], label='36-Day Slow SMA', color='orange', alpha=0.8, linewidth=1.5)
    
    # 5. Paint the Trade Signals
    buys = df[df['Trade_Signal'] == 'BUY']
    sells = df[df['Trade_Signal'] == 'SELL']
    
    # Green Up-Arrows for Buys
    plt.scatter(buys.index, buys['Close'], marker='^', color='green', s=150, label='BUY Signal', zorder=5)
    
    # Red Down-Arrows for Sells
    plt.scatter(sells.index, sells['Close'], marker='v', color='red', s=150, label='SELL Signal', zorder=5)
    
    # 6. Final Polish and Save
    plt.legend(loc='upper left')
    plt.ylabel("Price (USD)")
    plt.xlabel("Date")
    
    # --- NEW SAVE LOGIC ---
    # Ensure the output directory exists
    os.makedirs("output", exist_ok=True)
    
    # Define the new path
    output_path = "output/tactical_chart.png"
    
    # Save to the new path
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Success! Chart saved as {output_path}")

if __name__ == "__main__":
    draw_chart()