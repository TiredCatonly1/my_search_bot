from providers.WikipediaProvider import WikipediaProvider
from providers.GitHubProvider import GitHubProvider
from providers.StackOverFlowProvider import StackOverFlowProvider

class SearchService:
    def __init__(self, text):
        self.text = text

    async def start_threads(self):
        wiki = await WikipediaProvider(self.text).get_url()
        github = await GitHubProvider(self.text).get_url()
        stackoverflow = await StackOverFlowProvider(self.text).get_url()
        results = [wiki, github, stackoverflow]
        valid_results = [str(res) for res in results if res]
        return "\n".join(valid_results)
