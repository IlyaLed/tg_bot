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

LOG_DIR = "logs"
LOG_FILE = "bot.log"
LOG_PATH = Path(LOG_DIR) / LOG_FILE

Path(LOG_DIR).mkdir(exist_ok=True)

def setup_logging():
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler = logging.FileHandler(
        filename=LOG_PATH,
        mode='a', 
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logging()

logger.debug("Отладочное сообщение")
logger.info("Бот запущен")
logger.warning("Предупреждение")
logger.error("Ошибка")

if not LOG_PATH.exists():
    logger.critical("Не удалось создать файл логов!")
else:
    logger.info(f"Логи записываются в: {LOG_PATH.absolute()}")

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  
)
dp = Dispatcher()

logger = logging.getLogger(__name__)
logger.info("Файл логов создан/открыт")

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
    print("hello")
    asyncio.run(main())