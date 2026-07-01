import time
from binance.client import Client
from binance.enums import *
import pandas as pd
import ta
from bot.config import *

# Binance Client Setup
if USE_TESTNET:
    client = Client(API_KEY, API_SECRET, testnet=True)
    print("✅ Connected to Binance TESTNET - Fake money mode")
else:
    client = Client(API_KEY, API_SECRET)
    print("⚠️ Connected to Binance LIVE - Real money mode")

def get_data():
    """Binance nunchi price data teesukuntadi"""
    klines = client.get_klines(symbol=SYMBOL, interval=TIMEFRAME, limit=100)
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 
                                       'close_time', 'quote_asset_volume', 'number_of_trades', 
                                       'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    df['close'] = pd.to_numeric(df['close'])
    return df

def calculate_emas(df):
    """EMA calculate chestadi"""
    df['fast_ema'] = ta.trend.ema_indicator(df['close'], window=FAST_EMA)
    df['slow_ema'] = ta.trend.ema_indicator(df['close'], window=SLOW_EMA)
    return df

def check_signal(df):
    """Buy/Sell signal check chestadi - EMA Crossover"""
    fast_ema = df['fast_ema'].iloc[-1]
    slow_ema = df['slow_ema'].iloc[-1]
    prev_fast = df['fast_ema'].iloc[-2]
    prev_slow = df['slow_ema'].iloc[-2]
    
    # Golden Cross - Buy Signal
    if prev_fast < prev_slow and fast_ema > slow_ema:
        return "BUY"
    # Death Cross - Sell Signal
    elif prev_fast > prev_slow and fast_ema < slow_ema:
        return "SELL"
    else:
        return "HOLD"

def place_order(signal):
    """Order vestadi"""
    try:
        if signal == "BUY":
            order = client.create_order(
                symbol=SYMBOL,
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quantity=TRADE_QUANTITY
            )
            print(f"🟢 BUY Order Placed: {order['orderId']}")
            
        elif signal == "SELL":
            order = client.create_order(
                symbol=SYMBOL,
                side=SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=TRADE_QUANTITY
            )
            print(f"🔴 SELL Order Placed: {order['orderId']}")
            
    except Exception as e:
        print(f"❌ Order Error: {e}")

def run_bot():
    """Bot main loop"""
    print(f"🚀 Starting Bot for {SYMBOL} | Timeframe: {TIMEFRAME}")
    print(f"Strategy: EMA {FAST_EMA} / {SLOW_EMA} Crossover")
    
    while True:
        try:
            df = get_data()
            df = calculate_emas(df)
            signal = check_signal(df)
            
            current_price = df['close'].iloc[-1]
            fast = df['fast_ema'].iloc[-1]
            slow = df['slow_ema'].iloc[-1]
            
            print(f"Price: {current_price} | Fast EMA: {fast:.2f} | Slow EMA: {slow:.2f} | Signal: {signal}")
            
            if signal in ["BUY", "SELL"]:
                place_order(signal)
            
            time.sleep(60)  # 60 seconds wait
            
        except Exception as e:
            print(f"⚠️ Bot Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    run_bot()
