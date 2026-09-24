import aiohttp
from models.search_result import SearchResult
class GitHubProvider:
    url = "https://api.github.com/search/issues"
    headers  = {
        "Accept": "application/vnd.github+json",
        "X-Github-Api-Version": "2022-11-28"
    }

    def __init__(self, text):
        self.text = text
        self.params = {
            "q": self.text,
            "per_page": 5
        }

    async def get_url(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=self.headers, params=self.params) as resp:
                clients = await resp.json()
                result = []
                for client in clients["items"]:
                    client = SearchResult(client['title'], client['body'], client['html_url'], "Github").result()
                    result.append(client)
        return result



