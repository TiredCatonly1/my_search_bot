import aiohttp
from models.search_result import SearchResult

class WikipediaProvider:
    def __init__(self, text):
        self.text = text
        self.params = {
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrsearch": self.text,
            "gsrlimit": 5,

            "prop": "info|extracts",

            "inprop": "url",
            "exintro": "1",
            "explaintext": "1",
            "exsentences": 3,
            "elexlimit": 5
        }

    url = "https://en.wikipedia.org/w/api.php"
    headers = {
        "User-Agent": "MyTestBot (contacts: poznavajkatv84@gmail.com)"
    }
    async def get_url(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.url, params=self.params) as resp:
                clients = await resp.json()
                result = []
                for client in clients["query"]["pages"].values():
                    client = SearchResult(client["title"], client["extract"], client["fullurl"], "Wikipedia").result()
                    result.append(client)
        return result





