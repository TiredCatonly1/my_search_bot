from textwrap import dedent

class SearchResult:
    def __init__(self, title, description, url, source):
        self.title = title
        self.description = description
        self.url = url
        self.source = source

    def result(self):
        return dedent(f"""
            Название: {self.title}
            Описание:{self.description}
            Ссылка: {self.url}
            Источник: {self.source}
        """).strip()



class WikipediaResult(SearchResult):
    def __init__(self, title, description, url, source):
        super().__init__(title, description, url, source)

    def result(self):
        return dedent(f"""
        🌐 Справка из <b>{self.source}</b>
        
        📌 <b>Название:</b> {self.title}
        📜 <b>Описание:</b> {self.description}
        
        <a href="{self.url}"><b>📎 Открыть cтатью</b></a>
        """)

class GitHubResult(SearchResult):
    def __init__(self, title, description, url, source, stars, language):
        super().__init__(title, description, url, source)
        self.stars = stars
        self.language = language

    def result(self):
        return dedent(f"""
        🎴 Репозиторий <b>{self.source}</b>
        
        📌 <b>Название:</b> {self.title}
        📜 <b>Описание:</b> {self.description}
        🌟 <b>Звёзды:</b> {self.stars}
        💻 <b>Язык:</b> {self.language}
        
        <a href="{self.url}"><b>📎 Открыть репозиторий</b></a>
        """)

class StackOverFlowResult(SearchResult):
    def __init__(self, title, description, url, source, score, answer_count):
        super().__init__(title, description, url, source)
        self.score = score
        self.answer_count = answer_count

    def result(self):
        return dedent(f"""
        📊 <b>{self.source}</b>
        
        📌 <b>Название:</b> {self.title}
        🌟 <b>Рейтинг:</b> {self.score}
        💬 <b>Ответы:</b> {self.answer_count}
        
        <a href="{self.url}"><b>📎 Открыть вопрос</b></a>
        """)