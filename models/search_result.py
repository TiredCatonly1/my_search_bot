class SearchResult:
    def __init__(self, title, description, url, source):
        self.title = title
        self.description = description
        self.url = url
        self.source = source

    def result(self):
        return (f"Название: {self.title} "
                f"Описание: {self.description} "
                f"Ссылка: {self.url} "
                f"Источник: {self.source} ")