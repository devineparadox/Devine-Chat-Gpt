import logging
import os
from pyrogram import Client, filters

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s - %(levelname)s] - %(name)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Environment variables (make sure these are set in your Heroku app)
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize the bot
DEVINE = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Log bot start
@DEVINE.on_startup
async def on_startup(client):
    logger.info("Bot is starting...")
    # Additional startup tasks

# Log bot stop
@DEVINE.on_shutdown
async def on_shutdown(client):
    logger.info("Bot is stopping...")

# Example command handler
@DEVINE.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    logger.info(f"Received /start command from {message.from_user.id}")
    await message.reply("ɢʀᴇᴇᴛɪɴɢs, ɪ ᴀᴍ {BOT_NAME}\n──────────────────\nᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀʟɢᴏʀɪᴛʜᴍs, ɪ ᴄᴀɴ ʀᴇsᴏʟᴠᴇ ʏᴏᴜʀ ǫᴜᴇʀɪᴇs ᴡɪᴛʜ ʟɪɢʜᴛɴɪɴɢ sᴘᴇᴇᴅ ᴀɴᴅ ᴀᴄᴄᴜʀᴀᴄ.")

# Log unexpected errors
@DEVINE.on_errors
async def handle_errors(client, message, exception):
    logger.error(f"Error occurred: {exception}")

if __name__ == "__main__":
    try:
        logger.info("Starting Bot...")
        DEVINE.run()
    except Exception as e:
        logger.exception("An error occurred while starting the bot: %s", e)
