import logging
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import openai
import os

# Logging configuration
FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
logging.basicConfig(
    level=logging.WARNING,
    format=FORMAT,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Get environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")
BOT_NAME = os.getenv("BOT_NAME")
BOT_USERNAME = os.getenv("BOT_USERNAME")
OWNER_USERNAME = os.getenv("OWNER_USERNAME")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP")
START_IMG = os.getenv("START_IMG")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL")
OWNER_ID = int(os.getenv("OWNER_ID"))

DEVINE = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START = f"""
<b>ɢʀᴇᴇᴛɪɴɢs, ɪ ᴀᴍ {BOT_NAME}</b>

<b>──────────────────</b>
<b>ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀʟɢᴏʀɪᴛʜᴍs,
ɪ ᴄᴀɴ ʀᴇsᴏʟᴠᴇ ʏᴏᴜʀ ǫᴜᴇʀɪᴇs ᴡɪᴛʜ
ʟɪɢʜᴛɴɪɴɢ sᴘᴇᴇᴅ ᴀɴᴅ ᴀᴄᴄᴜʀᴀᴄʏ.</b>"""

MAIN_BUTTONS = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/devineparadox/Devine-Chat-Gpt"),
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
            await message.reply_text(reply_text)
    except Exception as e:
        logger.error(f"Error in chat command: {e}")
        await message.reply_text(f"Error: {e}")

if __name__ == "__main__":
    try:
        logger.info("Bot is starting...")
        DEVINE.run()
        idle()
    except Exception as e:
        logger.error(f"Bot encountered an error: {e}")
    finally:
        logger.info("Bot has stopped.")
