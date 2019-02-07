from flask import render_template
from .request import get_news,get_articles
from ..models import News,Articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting general news
    general_news = get_news('general')
    print(general_news)
     # Getting entertainment news
    entertainment_news = get_news('entertainment')
    print(entertainment_news)
    # Getting entertainment news
    science_news=get_news('science')
    print (science_news)
    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', name = title,general = general_news, entertainment =entertainment_news, science =science_news)

@main.route('/articles/<id>')
def articles(id):
    '''View a specific source page and its articles'''
    articles = get_articles(id)
    title = f'{id}'
    return render_template('articles.html',title = title, id = id, articles = articles)