from aiogram import Router
from aiogram.types import Message
from providers.WikipediaProvider import WikipediaProvider
from providers.GitHubProvider import GitHubProvider
from providers.StackOverFlowProvider import StackOverFlowProvider


search_router = Router()
url = "https://en.wikipedia.org/w/api.php"
headers = {
    "User-Agent": "MyTestBot (contacts: poznavajkatv84@gmail.com)"
}

@search_router.message()
async def any_message(message: Message):
    text = message.text
    resp = await WikipediaProvider(text).get_url()
    github = await GitHubProvider(text).get_url()
    overflow = await StackOverFlowProvider(text).get_url()
    await message.answer(f"{resp}")
    await message.answer(f"{github}")
    await message.answer(f"{overflow}")




