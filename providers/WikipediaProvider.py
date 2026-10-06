import asyncio
import aiohttp
from aiohttp import ClientResponseError, ClientError
from models.search_result import WikipediaResult

class WikipediaProvider:
    def __init__(self, text):
        self.text = text
        self.params = {
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrsearch": self.text,
            "gsrsort": 'relevance',
            "gsrlimit": 1,

            "prop": "info|extracts",

            "inprop": "url",
            "exintro": "1",
            "explaintext": "1",
            "exsentences": 1
        }

    url = "https://en.wikipedia.org/w/api.php"
    headers = {
        "User-Agent": "MyTestBot (contacts: poznavajkatv84@gmail.com)"
    }
    async def get_url(self):
        try:
            async with asyncio.timeout(10):
                async with aiohttp.ClientSession(headers=self.headers) as session:
                    async with session.get(self.url, params=self.params) as resp:
                        resp.raise_for_status()
                        clients = await resp.json()
                        for client in clients["query"]["pages"].values():
                            client = WikipediaResult(client["title"], client["extract"], client["fullurl"],
                                                  "Wikipedia").result()
        except ClientResponseError as e:
            return f"Ошибка ответа сервера Wikipedia...\n{e}"
        except ClientError as e:
            return f"Ошибка клиента Wikipedia...\n{e}"
        except TimeoutError as e:
            return f"Операция выполнялась слишком долго, поэтому ее отменили...\n{e}"
        else:
            return client





