import requests
from pyrogram import Client as Bot

from YuiHirasawaMusicBot.config import API_HASH
from YuiHirasawaMusicBot.config import API_ID
from YuiHirasawaMusicBot.config import BG_IMAGE
from YuiHirasawaMusicBot.config import BOT_TOKEN
from YuiHirasawaMusicBot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="YuiHirasawaMusicBot.modules"),
)

bot.start()
run()
