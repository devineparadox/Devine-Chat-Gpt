# Devine Chat GPT

![Logo](https://telegra.ph//file/811e905e122befab95032.jpg)

A Telegram bot powered by ChatGPT, enabling natural language conversations and more.

## Features

- **Natural Language Processing**: Engage in conversations with the power of ChatGPT.
- **Command Handling**: Responds to commands like /start, /help, and more.
- **Inline Query Support**: Provides instant answers using inline queries.
- **Customizable Responses**: Tailor responses based on user interactions and context.
- **Error Handling**: Logs errors and ensures smooth operation.

## Deploying the Bot

### Using Template Deployment

You can quickly deploy your own instance of the Devine Chat GPT bot on Heroku by clicking the button below:

<p align="center"><a href="https://dashboard.heroku.com/new?template=https://github.com/devineparadox/Devine-Chat-Gpt/"> <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

1. Click the "Deploy" button above.
2. Fill in the required environment variables (`API_ID`, `API_HASH`, `BOT_TOKEN`, `OPENAI_KEY`, `OWNER_ID`, `OWNER_USERNAME`, `UPDATE_CHANNEL`, `SUPPORT_GROUP`) on the Heroku deployment page.
3. Deploy your app.

### Manual Deployment

To manually deploy the bot, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/devineparadox/Devine-Chat-Gpt.git
   cd Devine-Chat-Gpt
2. Install dependencies:

bash

pip install -r requirements.txt

3. Set up environment variables:

export API_ID=your_api_id
export API_HASH=your_api_hash
export BOT_TOKEN=your_bot_token
export OPENAI_KEY=your_openai_key
export OWNER_ID=your_owner_id
export OWNER_USERNAME=your_owner_username
export UPDATE_CHANNEL=your_update_channel
export SUPPORT_GROUP=your_support_group

Ensure these environment variables are set with your own values.

4. Run the bot:

python chatgpt.py

Notes

    Environment Variables: These variables are crucial for the bot to connect to Telegram and OpenAI services. Ensure they are correctly set either via a .env file or through your deployment platform's environment variable settings.
    Error Handling: The bot includes robust error handling and logging (logging module) to help diagnose issues during deployment and operation.
    Support: For assistance or troubleshooting, feel free to reach out to Support Group or the Bot Developer.

csharp


This complete markdown code provides comprehensive instructions for deploying your bot using either template deployment on Heroku or manual deployment by cloning the repository. Adjust the placeholders (`your_api_id`, `your_api_hash`, etc.) with your actual values before using it in your README.md file.

