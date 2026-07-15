import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database import init_db

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    init_db()

    print("✅ LumivraAnonBot Started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
