# ZauTeKm <https://t.me/ZauTeKm>
# @ZauTeKm

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from ZKSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ZKSongBot import Jebot as app
from ZKSongBot import LOGGER

pm_start_text = """
<b>Hi [{}](tg://user?id={}), I'm a Song Downloader Bot Join our Group For Using me.</b>

Send me /help for know my commands

➟ <b>Mαde by @Hacker_Jr</b>
"""

help_text = """
<b>Helpful Commands</b>

- /song <song name>: Download songs via Youtube
- /saavn <song name>: Download songs via JioSaavn
- /deezer <song name>: Download songs via Deezer
- Send youtube url to my pm for download it on audio format

➟ <b>Mαde by @Hacker_Jr</b>
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Our Group", url="https://t.me/KL_Music_Club"
                    ),
                    InlineKeyboardButton(
                        text="Our Channel", url="https://t.me/KL_ROCKERZ"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("ZauTe Song Bot is online.")
idle()
