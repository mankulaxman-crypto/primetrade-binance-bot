import os

# Binance API Keys - Ikkada paste cheyyaku. Secrets lo pedatham
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Bot Settings
SYMBOL = "BTCUSDT"  # Trade cheyyali anukunna coin
TRADE_QUANTITY = 0.001  # Entha quantity konali/ammali
USE_TESTNET = True  # True = Paper trading, False = Real money

# Strategy Settings - EMA Crossover
FAST_EMA = 9   # Fast EMA period
SLOW_EMA = 21  # Slow EMA period
TIMEFRAME = "5m"  # 1m, 5m, 15m, 1h, 4h

# Risk Management
STOP_LOSS_PERCENT = 1.5  # 1.5% loss ayite auto exit
TAKE_PROFIT_PERCENT = 3.0  # 3% profit vasthe auto exit
