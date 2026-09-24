import aiohttp
from models.search_result import SearchResult
class StackOverFlowProvider:
    url = "https://api.stackexchange.com/search/excerpts"
    def __init__(self, text):
        self.text = text
        self.params = {
            "q": self.text,
            "site": "stackoverflow"
        }

    async def get_url(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as resp:
                clients = await resp.json()
                results = []
                for client in clients.get('items', []):
                    client = SearchResult(client['title'], client["excerpt"], f"https://api.stackexchange.com/{client['question_id']}", "Stack OverFlow").result()
                    results.append(client)
        return results

