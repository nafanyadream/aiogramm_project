import aiogram
import logging
import asyncio
from aiogram import Dispatcher, Bot, types
from aiogram.filters import Command
import re

logging.basicConfig(level=logging.INFO)
TOKEN = '7915766873:AAECjWAJF9lu6pCm_aRxZBhFKgoAo2QFdHs'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply('Привет! Я бот-калькулятор. Введите выражение для вычисления.')

@dp.message()
async def calculate(message: types.Message):
    expression = re.sub(r'[^0-9+\-*/(). ]', '', message.text)
    try:
        result = eval(expression)
        await message.reply(f"Результат: {result}")
    except Exception as e:
        await message.reply("Ошибка: " + str(e))

async def start_db():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_db())
