import aiohttp
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
            "filter": "!6W.j*A974)7wT"
        }

    async def get_url(self):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.url, params=self.params) as resp:
                    clients = await resp.json()
                    results = []
                    for client in clients.get('items', []):
                        client = SearchResult(client['title'], client["excerpt"], f"https://api.stackexchange.com/{client['question_id']}", "Stack OverFlow").result()
                        results.append(client)
            except aiohttp.ClientConnectionError as e:
                return f"Ошибка подключения к StackOverflow {e}"
            else:
                return results

