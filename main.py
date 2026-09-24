import asyncio
from models.dispatcher import dp
from configs import bot

async def main():
    print("Starting bot")
    try:
        await dp.start_polling(bot)
    finally:
        print("Closing bot")

if __name__ == "__main__":
    asyncio.run(main())

