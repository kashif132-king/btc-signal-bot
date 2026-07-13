import os
import time
import requests
import pandas as pd
import ta

from binance.client import Client
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

SYMBOL = "BTCUSDT"
TIMEFRAME = "5m"

client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)
bot = Bot(token=BOT_TOKEN)
