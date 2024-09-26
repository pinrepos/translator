# Для начала необходимо установить библиотеки
#             sudo apt install pip
#             pip install googletrans==3.1.0a0  -it is important to install this version of the library
#             pip install pyTelegramBotAPI
#             pip install asyncio
#             pip install aiohttp

# import library
from googletrans import Translator
from telebot.async_telebot import AsyncTeleBot
import asyncio
from telebot.types import InlineQuery, InputTextMessageContent
from telebot import types

# Bot API
bot = AsyncTeleBot(
    "", parse_mode=None)


# Message text processing


@bot.message_handler()
async def user_text(message):
    translator = Translator()

    # Defining the input language.
    lang = translator.detect(message.text)
    lang = lang.lang

    # Translate
    if lang == 'uk':
        send = translator.translate(message.text)
        await bot.reply_to(message, '------\n' + send.text + '\n------')

    else:
        send = translator.translate(message.text, dest='en')
        await bot.reply_to(message, '------\n' + send.text + '\n------')

# Processing pictures with captions


@bot.message_handler(content_types=['photo'])
async def handle_image(message):
    translator = Translator()
    # Image message handler
    chat_id = message.chat.id
    photo = message.photo[-1].file_id
    caption = message.caption

    # Definition of the input language.
    lang = translator.detect(caption)
    lang = lang.lang

    # Translate
    if lang == 'uk':
        send = translator.translate(caption)

    else:
        send = translator.translate(caption, dest='en')
    await bot.send_photo(chat_id, photo, caption=send.text)

# Startup and restart on failure.
asyncio.run(bot.infinity_polling())
