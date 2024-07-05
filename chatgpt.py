from pyrogram import Client, filters, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ParseMode
import openai
import os, sys, re, requests
import asyncio, time
from random import choice
from datetime import datetime
import logging
from config import API_ID, API_HASH, BOT_TOKEN, OPENAI_KEY, BOT_NAME, BOT_USERNAME, OWNER_USERNAME, SUPPORT_GROUP, START_IMG, UPDATE_CHANNEL, OWNER_ID

# Logging configuration
FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
logging.basicConfig(
    level=logging.WARNING,
    format=FORMAT,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

StartTime = time.time()
DEVINE = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# New code to add sticker reply and loading animation
async def pre_start(client, message: Message):
    try:
        x = await message.reply_sticker(
            "CAACAgUAAyEFAASGBdcxAAOmZlhVrQbbVPD0vf8e64iTgGTh4i8AAsYNAAL1AAE5Vc5H-6Ms_qgfNQQ"
        )
        await x.delete()
        usr = message.from_user
        lol = await message.reply_text(
            f"Hello, {usr.first_name}!", parse_mode=ParseMode.MARKDOWN
        )
        await asyncio.sleep(0.4)
        await lol.edit_text("⚡")
        await asyncio.sleep(0.7)
        await lol.edit_text("Ꮮᴏᴀᴅɪɴɢ... ")
        await asyncio.sleep(0.5)
        await lol.delete()
    except Exception as e:
        logger.error(f"Error in pre_start animation: {e}")
        await message.reply_text(f"Error: {e}")

START = f"""
<b>ɢʀᴇᴇᴛɪɴɢs, ɪ ᴀᴍ {BOT_NAME}</b>

<b>──────────────────</b>
<b>ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀʟɢᴏʀɪᴛʜᴍs, ɪ ᴄᴀɴ
ʀᴇsᴏʟᴠᴇ ʏᴏᴜʀ ǫᴜᴇʀɪᴇs ᴡɪᴛʜ ʟɪɢʜᴛɴɪɴɢ
sᴘᴇᴇᴅ ᴀɴᴅ ᴀᴄᴄᴜʀᴀᴄʏ.</b>"""

MAIN_BUTTONS = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://graph.org/file/bf2b05a4ccc3f40a715c0.mp4"),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="HELP"),
    ],
]

HELP_READ = "ᴜsᴀɢᴇ /chatgpt <prompt>\n\n ᴇxᴀᴍᴘʟᴇ: `/chatgpt write a simple flask app in python.`\n\n**➻ ᴜsᴀɢᴇ** : /generate <prompt> \nᴇxᴀᴍᴘʟᴇ: `/generate a message to comfort a friend `"

HELP_BACK = [
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ ", callback_data="HELP_BACK"),
    ],
]

@DEVINE.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]))
async def start(client, message: Message):
    try:
        await message.reply_photo(
            photo=START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN_BUTTONS),
        )
    except Exception as e:
        logger.error(f"Error in start command: {e}")
        await message.reply_text(f"Error: {e}")

@DEVINE.on_callback_query()
async def cb_handler(client, query):
    if query.data == "HELP":
        await query.message.edit_text(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BACK),
        )
    elif query.data == "HELP_BACK":
        await query.message.edit_text(
            text=START,
            reply_markup=InlineKeyboardMarkup(MAIN_BUTTONS),
        )

@DEVINE.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["", "+", ".", "/", "-", "?", "$"]))
async def help(client, message: Message):
    await message.reply_photo(
        START_IMG,
        caption=HELP_READ,
        reply_markup=InlineKeyboardMarkup(HELP_BACK),
    )

@DEVINE.on_message(filters.command(["ping", "alive"], prefixes=["+", "/", "-", "?", "$", "&", "."]))
async def ping(client, message: Message):
    start_time = datetime.now()
    await message.reply_text("Pinging...")
    end_time = datetime.now()
    ms = (end_time - start_time).microseconds / 1000
    await message.reply_photo(
        photo=START_IMG,
        caption=f"✨ {BOT_NAME} ɪs ᴀʟɪᴠᴇ.\n\n"
                f"‣ ᴍᴀᴅᴇ ʙʏ [ᴅᴇᴠɪɴᴇ ɴᴇᴛᴡᴏʀᴋ](https://t.me/Devine_Network)\n"
                f"‣ ᴅᴇᴠʟᴏᴘᴇʀ : [Ꭰᴇᴠɪɴᴇ Ꭰᴀʀᴋ 々](https://t.me/Devine_dark)\n"
                f"‣ ᴘɪɴɢ : {ms} ᴍs\n"
                f"‣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : <code>'𝟸.𝟺.𝟸'<code> \n"
                f"‣ ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : <code>'𝟸.𝟶.𝟷𝟶𝟼'<code>",
        reply_markup=InlineKeyboardMarkup(MAIN_BUTTONS),
    )

openai.api_key = OPENAI_KEY  # This line should be at the top level, not inside any function or class

@DEVINE.on_message(filters.command(["chatgpt", "ai", "ask"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def chat(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("Example:\n\n`/chatgpt Where is the Taj Mahal?`")
        else:
            prompt = message.text.split(' ', 1)[1]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
            )
            reply_text = response['choices'][0]['message']['content']
            await message.reply_text(reply_text)
    except Exception as e:
        logger.error(f"Error in chat command: {e}")
        await message.reply_text(f"Error: {e}")

if __name__ == "__main__":
    logger.info("Bot is starting...")
    DEVINE.run()
    idle()
    logger.info("Bot has stopped.")
