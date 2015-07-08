#!/usr/bin/env python
# -*- coding: utf-8 -*-
import structlog
import requests
from bs4 import BeautifulSoup

logger = structlog.getLogger(__name__)

# Example 1: There is one page to scrap with 3 discs.
# 1.Make a request and capture with curl, browser or similar.
# 2.Analyze the request and Find the pagination element.
# 3.Make rules to take the pages link.
# 4.Retrieve link of all pages in pagination div.
# 5.Retrieve the information of the 13 discs.


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
    url = 'http://scrap.smartvel.net/example2.php'

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

    # Retrieve the page with GET REQUEST
    page = requests.get(url)

    # Build the DOM
    bs = BeautifulSoup(page.text)

    # Retrieve the link pages in pagination div.
    pages = [url['href'] for url in bs.findAll(*rules['pages'])]
    logger.info("#Link pages collected: {} links".format(len(pages)))

    # Find disco structure in DOM and iterate it
    for disco_raw in bs.findAll(*rules['discos']):

        # Create a disco class for each disco with its fields
        discos.append(
                    Disco(id=disco_raw.find(*rules['id']).text,
                          title=disco_raw.find(*rules['title']).text,
                          author=disco_raw.find(*rules['author']).text,
                          link=disco_raw.find(*rules['link'])['href'],
                          image=disco_raw.find(*rules['image'])['src'],
                          canciones=[cancion.text for cancion in disco_raw.findAll(*rules['canciones'])]
                          )
                    )

    logger.info("Spider collects {} discs ".format(len(discos)))
