import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  
)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я простой бот. Напиши мне что-нибудь, и я повторю.")

@dp.message(Command("info"))
async def send_info(message: types.Message):
    await message.answer("Этот бот для лабы.")

@dp.message(Command("help"))
async def send_help(message: types.Message):
    await message.answer("Вы ввели команду /help \nВведите текст")

@dp.message(F.text)
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")
    print("hello")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())