#!/usr/bin/env python
# -*- coding: utf-8 -*-
import structlog
import requests
from bs4 import BeautifulSoup

logger = structlog.getLogger(__name__)

# Example 1: There is one page to scrap with 3 discs.
# 1.Make a get request.
# 2.Analize the request and find the disc structure.
# 3.Make the rules to take the info.
# 4.Retrieve the html with a request.
# 5.Retrieve the fields of a disc.
# 6.Retrieve the 3 discs information.


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
    url = 'http://scrap.smartvel.net/example1.html'

    # Rules
    rules = {'discos': ('div', {'class': 'disco'}),
             'id': ('span', {'class', 'id'}),
             'title': ('h1', {'class', 'titulo'}),
             'author': ('span', {'class', 'author'}),
             'link': ('a', {'class', 'spotifylink'}),
             'image': ('image',),
             'canciones': ('span', {'class', 'cancion'})
             }

    # Retrieve the page with GET REQUEST
    page = requests.get(url)
    logger.info("Request Status_code: {}".format(page.status_code))
    logger.info("Information in request: {}".format(page.text))

    # Build the DOM

    # Find disco structure in DOM and iterate it

    # Create a disco class for each disco with its fields

    logger.info("Spider collects {} discs ".format(len(discos)))
