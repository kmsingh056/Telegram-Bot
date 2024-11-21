import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

# Command handler
@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    await message.reply("Hi\nI am Echo Bot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message:types.Message):
    await message.answer(message.text)

# Start polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
