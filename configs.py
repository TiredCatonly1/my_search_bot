from os import getenv
from dotenv import load_dotenv
from aiogram import Bot

load_dotenv()

token = getenv("BOT_TOKEN")

if not token:
    raise ValueError("Bot token is missing")

bot = Bot(token=token)
