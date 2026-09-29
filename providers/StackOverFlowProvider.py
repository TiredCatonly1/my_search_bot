import asyncio
import aiohttp
from aiohttp import ClientResponseError, ClientError
from models.search_result import SearchResult
class StackOverFlowProvider:
    url = "https://api.stackexchange.com/search/excerpts"
    def __init__(self, text):
        self.text = text
        self.params = {
            "q": self.text,
            "site": "stackoverflow",
            "pagesize": 3,
            "page": 1,
        }

    async def get_url(self):
        try:
            async with asyncio.timeout(10):
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.url, params=self.params) as resp:
                        resp.raise_for_status()
                        clients = await resp.json()
                        results = []
                        for client in clients.get('items', []):
                            client = SearchResult(client['title'], client["excerpt"], f"https://api.stackexchange.com/{client['question_id']}", "Stack OverFlow").result()
                            results.append(client)
        except ClientResponseError as e:
            return f"Сервер StackOverFlow не отвечает...\n{e}"
        except ClientError as e:
            return f"Ошибка клиента StackOverFlow...\n{e}"
        except TimeoutError as e:
            return f"Операция выполнялась слишком долго, поэтому ее отменили...\n{e}"
        else:
            return results

