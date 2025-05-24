class Article:
    
    def __init__(self, author, magazine, title):
        self._author = author
        self.magazine = magazine
        self._title = title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        if isinstance(value, str) and (5 <= len(value) <= 50 ):
            self._title = value
        else:
            print('Value must be a string of between 5 and 50 characters')      

    @property
    def author(self):
        return self.author

    @author.setter
    def author(self,value):
        if isinstance(value, Author):
            self.author = value
        else:
            print("Author must be an instance of Author class ")     

    
    @property
    def magazine(self):
        return self.magazine

    @magazine.setter
    def magazine(self,value):
        if  isinstance (value, magazine) :
            self.magazine = value
        else:
            print('magazine must be of type magazine and not empty.')    


    

class Author:
    articles = []
    def __init__(self, name):
        self._name = name
    
       
    @property
    def Author(self):
        return self._author 

    @Author.setter
    def Author(self,author):
        if isinstance(author, str) and (len(author) > 0):
            self._author = author
        else:
            print("invalid Author ")         

    @property
    def articles(self):
        return articles

    @articles.setter
    def articles(self,article):
        if isinstance(article, Article) :
            articles.append(article)
        else:
            print('articles must be of type Article.')    


    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance (value, str) and (2 <=len(value) <=16):
            self._name = value      
        
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self,category):
        if isinstance(category, str) and (len(category) > 0):
            self._category = category  
    
    
    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass


        