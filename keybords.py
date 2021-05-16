from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.utils.callback_data import CallbackData

from utils import *

__all__ = ('all_channels_keyboard', 'channel_keyboard', 'guide_data')

guide_data = CallbackData("guide", "level", "channel")


def redefine_callback_data(level, channel="0"):
    return guide_data.new(level=level, channel=channel)


async def all_channels_keyboard():
    # текущий уровень меню - 0
    _LEVEL = 0

    keyboard = InlineKeyboardMarkup()
    channels = await get_list_of_channels()
    for channel in channels:
        button_text = f"{channel['name']}"
        _callback_data = redefine_callback_data(
            level=_LEVEL + 1, channel=channel['slug'])
        keyboard.insert(
            InlineKeyboardButton(text=button_text, callback_data=_callback_data)
        )
    return keyboard


async def channel_keyboard():
    _LEVEL = 1
    keyboard = InlineKeyboardMarkup()
    keyboard.insert(
        InlineKeyboardButton(
            text="К списку каналов",
            callback_data=redefine_callback_data(level=_LEVEL - 1))
    )
    return keyboard
