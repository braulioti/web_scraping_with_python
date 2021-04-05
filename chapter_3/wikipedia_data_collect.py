import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html.read(), 'html.parser')

    try:
        print(bs.h1.get_text())
        print(bs.find(id = 'mw-content-text').find_all('p')[0])
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Continuing.')

    for link in bs.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # New page found
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')