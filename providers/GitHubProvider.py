import asyncio
import aiohttp
from aiohttp import ClientResponseError, ClientError
from models.search_result import GitHubResult
class GitHubProvider:
    url = "https://api.github.com/search/repositories"
    headers  = {
        "Accept": "application/vnd.github+json",
        "X-Github-Api-Version": "2022-11-28"
    }

    def __init__(self, text):
        self.text = text
        self.params = {
            "q": self.text,
            "per_page": 1
        }

    async def get_url(self):
        try:
            async with asyncio.timeout(10):
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.url, headers=self.headers, params=self.params) as resp:
                        resp.raise_for_status()
                        clients = await resp.json()
                        for client in clients["items"]:
                            client = GitHubResult(client['full_name'], client['description'], client['clone_url'], "Github", client["stargazers_count"], client["language"]).result()
        except ClientResponseError as e:
            return f"Ошибка ответа сервера GitHub...\n{e}"
        except ClientError as e:
            return f"Ошибка клиента Github...\n{e}"
        except TimeoutError as e:
            return f"Операция выполнялась слишком долго, поэтому ее отменили...\n{e}"
        else:
            return client


