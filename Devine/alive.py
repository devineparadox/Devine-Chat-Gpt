import logging
from pyrogram import Client, filters
from pyrogram.types import Message
import os
from datetime import datetime

# Logging configuration
FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
logging.basicConfig(
    level=logging.INFO,  # Adjust log level as needed
    format=FORMAT,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Get environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
BOT_USERNAME = os.getenv("BOT_USERNAME")
START_IMG = os.getenv("START_IMG")

DEVINE = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@DEVINE.on_message(filters.command(["ping", "alive"], prefixes=["+", "/", "-", "?", "$", "&", "."]))
async def ping(client, message: Message):
    try:
        start_time = datetime.now()
        await message.reply_text("ᴡᴀɪᴛ...")
        end_time = datetime.now()
        ms = (end_time - start_time).microseconds / 1000
        await message.reply_photo(
            photo=START_IMG,
            caption=f"✨ {BOT_NAME} ɪs ᴀʟɪᴠᴇ.\n\n"
                f"‣ ᴍᴀᴅᴇ ʙʏ [ᴅᴇᴠɪɴᴇ ɴᴇᴛᴡᴏʀᴋ](https://t.me/Devine_Network)\n"
                f"‣ ᴅᴇᴠʟᴏᴘᴇʀ : [Ꭰᴇᴠɪɴᴇ Ꭰᴀʀᴋ 々](https://t.me/Devine_dark)\n"
                f"‣ ᴘɪɴɢ : {ms} ᴍs\n"
                f"‣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 𝟹.𝟿\n"
                f"‣ ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : 𝟷.𝟸.𝟶",
        )
    except Exception as e:
        logger.error(f"Error processing /ping or /alive command: {e}")

if __name__ == "__main__":
    try:
        logger.info("Alive check bot is starting...")
        DEVINE.run()
    except Exception as e:
        logger.error(f"Alive check bot encountered an error: {e}")
    finally:
        logger.info("Alive check bot has stopped.")
