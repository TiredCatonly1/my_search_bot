from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start_router = Router(name="start")

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет, я поисковый бот.\nВведи поисковый запрос...")