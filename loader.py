

from aiogram import Bot, Dispatcher

from config import TOKEN, admin_id

bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
