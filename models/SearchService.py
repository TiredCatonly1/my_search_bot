import asyncio
from providers.WikipediaProvider import WikipediaProvider
from providers.GitHubProvider import GitHubProvider
from providers.StackOverFlowProvider import StackOverFlowProvider

class SearchService:
    def __init__(self, text):
        self.text = text

    async def start_threads(self):
        wiki, github, stackoverflow = await asyncio.gather(WikipediaProvider(self.text).get_url(),
                                                           GitHubProvider(self.text).get_url(),
                                                           StackOverFlowProvider(self.text).get_url())
        results = [str(wiki), str(github), str(stackoverflow)]
        return results
