import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import openai
from pymongo import MongoClient
import os

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_KEY")

# Configure MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client['chatbot']
collection = db['conversations']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your ChatGPT bot.')

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=50
    )
    bot_reply = response.choices[0].text.strip()

    # Save conversation to MongoDB
    collection.insert_one({"user": user_message, "bot": bot_reply})

    await update.message.reply_text(bot_reply)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    start_handler = CommandHandler('start', start)
    chat_handler = CommandHandler('chat', chat)

    application.add_handler(start_handler)
    application.add_handler(chat_handler)

    application.run_polling()
