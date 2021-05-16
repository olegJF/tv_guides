from typing import Union

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ParseMode

from keybords import all_channels_keyboard, channel_keyboard, guide_data
from loader import bot, dp
from utils import get_tv_guide


@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await list_of_channels(message)


async def list_of_channels(message: Union[CallbackQuery, Message], **kwargs):
    markup = await all_channels_keyboard()

    if isinstance(message, Message):
        await message.answer("Список каналов", reply_markup=markup)

    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def show_program(callback: CallbackQuery, channel):
    markup = await channel_keyboard()
    text = await get_tv_guide(channel)
    await callback.message.edit_text(
        text, reply_markup=markup, parse_mode=ParseMode.MARKDOWN)
    # await callback.message.answer(
    #     text, reply_markup=markup, parse_mode=ParseMode.MARKDOWN)


# Функция, которая обрабатывает ВСЕ нажатия на кнопки в этой менюшке
@dp.callback_query_handler(guide_data.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Тип объекта CallbackQuery, который прилетает в хендлер
    :param callback_data: Словарь с данными, которые хранятся в нажатой кнопке
    """

    # Получаем текущий уровень меню, который запросил пользователь
    current_level = callback_data.get("level")

    # Получаем категорию, которую выбрал пользователь (Передается всегда)
    channel = callback_data.get("channel")

    # Прописываем "уровни"
    levels = {
        "0": list_of_channels,
        "1": show_program,

    }

    # Забираем нужную функцию для выбранного уровня
    current_level_function = levels[current_level]

    # Выполняем нужную функцию и передаем туда параметры, полученные из кнопки
    await current_level_function(
        call,
        channel=channel,
    )

# @dp.message_handler()
# async def echo(message: Message):
#     text = f"Привет, ты написал: {message.text}"
#     await bot.send_message(chat_id=message.from_user.id, text=text)
#     await message.reply(text=text)
#     await message.answer(text=text)
