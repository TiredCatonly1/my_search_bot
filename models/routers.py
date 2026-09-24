from aiogram import Router
from handlers.start import start_router
from handlers.search import search_router

main_router = Router()

main_router.include_router(start_router)
main_router.include_router(search_router)
