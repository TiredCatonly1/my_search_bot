import asyncio
from providers.WikipediaProvider import WikipediaProvider
from providers.GitHubProvider import GitHubProvider
from providers.StackOverFlowProvider import StackOverFlowProvider

class SearchService:
    def __init__(self, text):
        self.text = text
    sem = asyncio.Semaphore(3)
    async def start_threads(self):
        async with self.sem:
            clients = await asyncio.gather(WikipediaProvider(self.text).get_url(),
                                                               GitHubProvider(self.text).get_url(),
                                                               StackOverFlowProvider(self.text).get_url(),
                                                               return_exceptions=True)
            results = []
            for client in clients:
                if isinstance(client, Exception):
                    if isinstance(client, ConnectionError):
                        results.append(f"Ошибка подключения к серверу...\nConnectionError")
                else:
                    results.append(str(client))
            return results


