from aiogram import Dispatcher
from models.routers import main_router

dp = Dispatcher()

dp.include_router(main_router)