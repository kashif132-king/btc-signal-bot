import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

TIMEFRAME = os.getenv("TIMEFRAME", "5m")
SYMBOL = os.getenv("SYMBOL", "BTCUSDT")
