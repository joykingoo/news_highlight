from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news
    popular_news = get_news('popular')
    print(popular_news)
    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', name = title,popular = popular_news)

@app.route('/news')
def news():

    '''
    View movie page function that returns the movie details page and its data
    '''
    title = 'Home - Welcome to The best News Website '
    return render_template('news.html', title = title)