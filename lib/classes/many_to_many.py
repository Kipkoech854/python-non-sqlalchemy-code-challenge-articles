class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None
        
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if not (5 <= len(value) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author")
        self._author = author
        author._articles.append(self)

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = magazine
        magazine._articles.append(self)
        if self.author:
            magazine._contributors.add(self.author)


class Author:
    def __init__(self, name):
        self._name = None
        self._articles = []
        self.name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    all = []
    
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self._articles = []
        self._contributors = set()
        
        self.name = name
        self.category = category
        Magazine.all.append(self)
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value
            
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if  not isinstance(value, str) :
            raise TypeError("Category must be a string ")
        if len(value) == 0:
            raise ValueError('categorymust be longer than 0 characters')
        else:         
            self._category = value
        
           
    def articles(self):
        return self._articles

    def contributors(self):
        return list(self._contributors)

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
            
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        else:    
            return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)