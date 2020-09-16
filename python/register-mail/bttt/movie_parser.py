__author__ = 'ooobj'

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

def parse():
    file_path = '/Users/ooobj/python/bttt/download/'
    base_url = 'http://www.bttiantang.com'

    client = MongoClient()
    db = client.test.movies

    movies = get_movies(db)
    for movie in movies:
        print(movie['url'])
        get_page(db, base_url+movie['url'])


def get_page(db, url):
    r = requests.get(url)
    print(r.text)


def get_movies(db):
    movies = db.find({'status': 0}).limit(1)
    return movies


if __name__ == '__main__':
    parse()