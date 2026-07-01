# Primetrade.ai Binance Futures Testnet Bot

CLI tool for placing MARKET and LIMIT orders on Binance USDT-M Futures Testnet.

## Setup
1. `pip install -r requirements.txt`
2. Create `.env` file with `BINANCE_API_KEY` and `BINANCE_API_SECRET`
3. Run: `python -m bot.cli BTCUSDT BUY MARKET 0.001`

## Features
- Market & Limit Orders
- Structured Logging to bot.log
- Input Validation
- Testnet Only

## Proof of Execution
See `bot.log` for successful MARKET and LIMIT order logs.
