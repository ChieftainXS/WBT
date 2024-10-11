import asyncio
import os

from db import create_db_and_tables
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
from handlers import default_router

load_dotenv(find_dotenv())

TGTOKEN = os.getenv('TGTOKEN')
APITOKEN = os.getenv('APITOKEN')

bot = Bot(token=TGTOKEN)

dp = Dispatcher()
dp.include_router(default_router)

async def main():
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)

create_db_and_tables()
asyncio.run(main())