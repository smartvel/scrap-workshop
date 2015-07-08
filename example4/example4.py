#!/usr/bin/env python
# -*- coding: utf-8 -*-
import structlog
from selenium import webdriver
from bs4 import BeautifulSoup

logger = structlog.getLogger(__name__)

# Example 4: There is a paginated web, loading the info with Angularjs(javascript).
# 1.Make a get request and capture with curl, browser or similar.
# 2.Analize the request.
# 3.Use selenium to retrieve the web.
# 4.Analize the retrieved information, find the next page button and use selenium to change the page clicking on it.
# 5.Build the scraper to retrieve the 13 discs information.


# Class with the fields of a disc
class Disco():
    def __init__(self, id='', title='', author='', link='', image='', canciones=[]):
        self.id = id
        self.title = title
        self.author = author
        self.link = link
        self.image = image
        self.canciones = canciones

if __name__ == "__main__":

    discos = []
    url = 'http://scrap.smartvel.net/javascript/example4.html'

    # Rules
    rules = {'discos': ('div', {'class': 'disco'}),
             'id': ('span', {'class', 'id'}),
             'title': ('h1', {'class', 'titulo'}),
             'author': ('span', {'class', 'author'}),
             'link': ('a', {'class', 'spotifylink'}),
             'image': ('img',),
             'canciones': ('span', {'class', 'cancion'}),
             'pages': ('a', {'class', 'page'})
             }

    # Retrieve the page with Selenium

    driver = webdriver.PhantomJS(service_log_path='/dev/null')
    driver.get(url)
    logger.info("Spider collects this page: {} ".format(driver.page_source))
