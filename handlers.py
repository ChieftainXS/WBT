from db import LogBase, add_log
from lexicon import LEXICON as L

from weather import get_weather_to_city

from aiogram import types, Router, F
from aiogram.filters import Command

default_router = Router()

@default_router.message(Command('start'))
async def start_message(message: types.Message):
    await message.answer(L['start_message'])

@default_router.message(F.text.startswith('/weather'))
async def get_city_weather(message: types.Message):
    city = message.text.split(' ')[-1]
    user = message.from_user.id
    date_text = message.date.strftime("%Y-%m-%d %H:%M:%S")
    answer = await get_weather_to_city(city)
    log = LogBase(user_id=user, date_text=date_text, req_text=message.text, ans_text=answer)
    await add_log(log)
    await message.answer(answer)