import asyncio
import aiohttp
from aiohttp import ClientResponseError, ClientError
from models.search_result import SearchResult
class StackOverFlowProvider:
    url = "https://api.stackexchange.com/2.3/search/advanced"
    def __init__(self, text):
        self.text = text
        self.params = {
            "q": self.text,
            "site": "stackoverflow",
            "pagesize": 1,
            "page": 1,
            "sort": "relevance"
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
                            client = SearchResult(client.get('title', ""), client.get("excerpt", ""), client.get("link", ""), "Stack OverFlow").result()
                            results.append(client)
        except ClientResponseError as e:
            return f"Сервер StackOverFlow не отвечает...\n{e}"
        except ClientError as e:
            return f"Ошибка клиента StackOverFlow...\n{e}"
        except TimeoutError as e:
            return f"Операция выполнялась слишком долго, поэтому ее отменили...\n{e}"
        else:
            return results

