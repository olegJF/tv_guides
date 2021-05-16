import aiohttp
from aiogram.utils.markdown import text, bold

from config import api_url

__all__ = (
    'get_list_of_channels', 'get_tv_guide'
)


async def get_list_of_channels():
    url = api_url.format('channels/')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            program_list = await response.json(content_type=None)
    return program_list


async def get_tv_guide(channel, date=None):
    channel_str = f'guides/{channel}/'
    url = api_url.format(channel_str)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            film_list = await response.json(content_type=None)
            msq = ''
            for film in film_list:
                msq += text(
                    bold(f'{film["time"][:-3]}  {film["title"]}'),
                    f'{film["short"]}\n\n', sep='\n'
                )
    return msq
