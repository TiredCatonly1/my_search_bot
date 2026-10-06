import time
from aiogram import Router
from aiogram.types import Message
from models.SearchService import SearchService


search_router = Router()


@search_router.message()
async def any_message(message: Message):
    text = message.text
    start = time.time()
    resp = await SearchService(text).start_threads()
    await message.answer(' '.join(resp), parse_mode='HTML')
    end = time.time()
    print(f"Всего {round(end-start, 2)} секунд...")



