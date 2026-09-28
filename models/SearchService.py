import aiohttp
import asyncio
from providers.WikipediaProvider import WikipediaProvider
from providers.GitHubProvider import GitHubProvider
from providers.StackOverFlowProvider import StackOverFlowProvider

class SearchService:
    def __init__(self, text):
        self.text = text

    async def start_threads(self):
        clients = await asyncio.gather(WikipediaProvider(self.text).get_url(),
                                                           GitHubProvider(self.text).get_url(),
                                                           StackOverFlowProvider(self.text).get_url(),
                                                           return_exceptions=True)
        results = []
        for client in clients:
            try:
                if isinstance(client, Exception):
                    raise client
            except ConnectionError:
                results.append(f"Ошибка подключения к серверу...\nConnectionError")
            except aiohttp.ClientError:
                results.append("Ошибка клиента")
            except Exception as e:
                results.append(f"Непредвиденная ошибка ")
            else:
                results.append(client)
        return results


