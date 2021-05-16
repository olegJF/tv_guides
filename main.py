from aiogram import executor

from config import admin_id
from loader import bot



async def send_to_admin(*args, **kwargs):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


async def on_shutdown(dp):
    await bot.close()

if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(
        dp,  on_shutdown=on_shutdown,
        # on_startup=send_to_admin,
    )
