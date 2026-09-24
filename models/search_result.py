class SearchResult:
    def __init__(self, title, description, url, source):
        self.title = title
        self.description = description
        self.url = url
        self.source = source

    def result(self):
        return (f"Название: {self.title}\n"
                f"Описание: {self.description}\n"
                f"Ссылка: {self.url}\n"
                f"Источник: {self.source}")