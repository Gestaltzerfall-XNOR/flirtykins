import os

import lightbulb
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

bot = lightbulb.BotApp(token=token)

bot.load_extensions_from("src/extensions")
