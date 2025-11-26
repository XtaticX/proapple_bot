import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.formatting import Text, Bold
from ig.BOT_TOKEN import BOT_TOKEN

# Убедитесь, что BOT_TOKEN.py существует и содержит переменную BOT_TOKEN
from ig.BOT_TOKEN import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_hello(message: types.Message):
    content = Text(
        "Привет, ",
        Bold(message.from_user.full_name),
        ", чем могу помочь?"
    )
    await message.answer(**content.as_kwargs())
async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())