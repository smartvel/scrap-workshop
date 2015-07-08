#!/usr/bin/env python
# -*- coding: utf-8 -*-
import structlog
import requests
from bs4 import BeautifulSoup

logger = structlog.getLogger(__name__)

# Example 3: There is one page to scrap with 3 music discs but requieres auth.
# 1.Make a get request and capture with curl, browser or similar.
# 2.Look at Requests lib documentation how to make auth requests.
# 3.Use auth to retrieve the 3 discs information.


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
    url = 'http://scrap.smartvel.net/auth/example3.html'

    # Rules
    rules = {'discos': ('div', {'class': 'disco'}),
             'id': ('span', {'class', 'id'}),
             'title': ('h1', {'class', 'titulo'}),
             'author': ('span', {'class', 'author'}),
             'link': ('a', {'class', 'spotifylink'}),
             'image': ('img',),
             'canciones': ('span', {'class', 'cancion'})
             }

    # Retrieve the page with GET REQUEST
    page = requests.get(url)

    # Build the DOM
    bs = BeautifulSoup(page.text)

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
