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
            await message.reply_text("Example:\n\n/generate a white siamese cat")
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

if name == "main":
    logger.info(f"{BOT_NAME} is starting...")
    try:
        DEVINE.start()
    except (ApiIdInvalid, ApiIdPublishedFlood) as e:
        logger.critical(f"Your API_ID/API_HASH is not valid: {e}")
        raise
    except AccessTokenInvalid as e:
        logger.critical(f"Your BOT_TOKEN is not valid: {e}")
        raise
    logger.info(f"{app.mention} is alive!")
    idle()
    DEVINE.stop()
    logger.info(f"{BOT_NAME} has stopped.")
