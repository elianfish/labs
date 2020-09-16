__author__ = 'ooobj'


import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

def parse():
    client = MongoClient()
    db = client.bttt.movies
    for page in range(1, 684):
        get_url(db, page)

def get_url(db, page):
    r = requests.get('http://www.bttiantang.com/?PageNo=%d' %page, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    items = soup.find_all('div', class_='litpic')
    print("%d -- %d" % (page, len(items)))
    for item in items:
        links = item.find_all('a')
        for link in links:
            if 'href' in link.attrs:
                s = link['href']
                if not check_exists(db, s):
                    print(s)
                    movie = {}
                    movie['url'] = s
                    movie['status'] = 0
                    db.save(movie)

def check_exists(db, url):
    count = db.find({'url': url}).count()
    if count > 0:
        return True
    else:
        return False



if __name__ == '__main__':
    parse()
