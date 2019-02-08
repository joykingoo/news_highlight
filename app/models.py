class News:
    '''
    news class to define news Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id =id
        self.name = name
        self.description= description
        self.url=url
        self.category=category
        self.language=language
        self.country=country
class Articles:
    '''
    articles class to define sources Objects
    '''

    def __init__(self,id,title,description,author,urlToImage,publishedAt,content,url):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url =url
