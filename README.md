# Devine Chat GPT

![Logo](https://telegra.ph//file/44f9c0b5f1afbf934c078.jpg)

A Telegram bot powered by ChatGPT, enabling natural language conversations and more.

## Features

- **Natural Language Processing**: Engage in conversations with the power of ChatGPT.
- **Command Handling**: Responds to commands like /start, /help, and more.
- **Inline Query Support**: Provides instant answers using inline queries.
- **Customizable Responses**: Tailor responses based on user interactions and context.
- **Error Handling**: Logs errors and ensures smooth operation.

Click the button below to deploy your own instance of the bot on Heroku.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/devineparadox/Devine-Chat-Gpt)

## Environment Variables

- `API_ID`: Your Telegram API ID
- `API_HASH`: Your Telegram API Hash
- `BOT_TOKEN`: Your Telegram Bot Token
- `OPENAI_KEY`: Your OpenAI API Key
- `OWNER_ID`: The Telegram ID of the bot owner
- `OWNER_USERNAME`: The Telegram username of the bot owner
- `UPDATE_CHANNEL`: The Telegram update channel
- `SUPPORT_GROUP`: The Telegram support group

## How to Run Locally

1. Clone the repository
2. Install dependencies
3. Set up environment variables
4. Run the bot

```bash
git clone https://github.com/devineparadox/Devine-Chat-Gpt.git
cd Devine-Chat-Gpt
pip install -r requirements.txt
export API_ID=your_api_id
export API_HASH=your_api_hash
export BOT_TOKEN=your_bot_token
export OPENAI_KEY=your_openai_key
export OWNER_ID=your_owner_id
export OWNER_USERNAME=your_owner_username
export
UPDATE_CHANNEL=your_update_channel
export SUPPORT_GROUP=your_support_group
python bot.py

