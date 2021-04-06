from urllib.request import urlopen

from bs4 import BeautifulSoup
from pip._vendor import requests


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.read(), 'html.parser')

def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.findAll("p", {"class":"css-1cy1v93"}).text
    body = "\n".join([line.text for line in lines])
    return Content(url, title, body)

def scrapeBookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find("div", {"class":"post-body"}).text
    return Content(url, title, body)

url = 'https://www.bookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-unconfortable-thruths/'
content = scrapeBookings(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)

url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'
content = scrapeNYTimes(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)