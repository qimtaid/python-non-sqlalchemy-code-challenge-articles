class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

        if not isinstance(self._title, str) or not (5 <= len(self._title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters long")

        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        self._name = name

        if not isinstance(self._name, str) or len(self._name) == 0:
            raise ValueError("Name must be a non-empty string")

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles()))


class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category

        if not isinstance(self._name, str) or not (2 <= len(self._name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters long")
        if not isinstance(self._category, str) or len(self._category) == 0:
            raise ValueError("Category must be a non-empty string")

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2]

