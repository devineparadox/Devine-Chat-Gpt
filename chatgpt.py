from pyrogram import Client, filters, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ParseMode
import openai
import os, sys, re, requests
import asyncio, time
from random import choice
from datetime import datetime

# Import logging module
import logging

# Logging configuration
FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
logging.basicConfig(
    level=logging.WARNING,
    format=FORMAT,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Constants from config.py
from config import API_ID, API_HASH, BOT_TOKEN, OPENAI_KEY, BOT_NAME, BOT_USERNAME, OWNER_USERNAME, SUPPORT_GROUP, START_IMG, UPDATE_CHANNEL

StartTime = time.time()
DEVINE = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START = f"""
๏ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}
➻ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ.
──────────────────
ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇ ʙᴏᴛ ᴀɴᴅ ᴄᴀɴ 
ᴀɴsᴡᴇʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀɪᴇs ᴇᴀsʟɪʏ

Rᴇᴀᴅ Tʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ

๏ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴜsᴇ /help
"""

MAIN_BUTTONS = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text=" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GROUP}"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴍᴅs ", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"https://github.com/Devineparadox/chat-dev"),
        InlineKeyboardButton(text=" ᴜᴘᴅᴀᴛᴇs ", url=f"https://t.me/{UPDATE_CHANNEL}"),
    ],
]

HELP_READ = "**ᴜsᴀɢᴇ** /chatgpt <prompt>\n\n ᴇxᴀᴍᴘʟᴇ: `/chatgpt write a simple flask app in python.`\n\n**➻ ᴜsᴀɢᴇ** : /generate <prompt> \nᴇxᴀᴍᴘʟᴇ: `/generate a cute girl photo`  \n\n➻ ᴜsᴀɢᴇ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.**\n\n©️ @YourUsername**"

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
        caption=f"Hey! {BOT_NAME} is alive.\nPing: {ms} ms",
        reply_markup=InlineKeyboardMarkup(MAIN_BUTTONS),
    )

openai.api_key = OPENAI_KEY

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
            await message.reply_text(f"{message.from_user.first_name} asked:\n\n{prompt}\n\n{BOT_NAME} answered:\n\n{reply_text}")
    except Exception as e:
        logger.error(f"Error in chat command: {e}")
        await message.reply_text(f"Error: {e}")

@DEVINE.on_message(filters.command(["generate", "image", "photo"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def generate_image(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("Example:\n\n`/generate a white siamese cat`")
        else:
            prompt = message.text.split(' ', 1)[1]
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024",
            )
            image_url = response['data'][0]['url']
            await message.reply_photo(image_url, caption="Here is your generated image!")
    except Exception as e:
        logger.error(f"Error in generate_image command: {e}")
        await message.reply_text(f"Error: {e}")

if __name__ == "__main__":
    logger.info(f"{BOT_NAME} is starting...")
    try:
        DEVINE.start()
    except (ApiIdInvalid, ApiIdPublishedFlood) as e:
        logger.critical(f"Your API_ID/API_HASH is not valid: {e}")
        raise
    except AccessTokenInvalid as e:
        logger.critical(f"Your BOT_TOKEN is not valid: {e}")
        raise
    logger.info(f"{BOT_NAME} is alive!")
    idle()
    DEVINE.stop()
    logger.info(f"{BOT_NAME} has stopped.")
