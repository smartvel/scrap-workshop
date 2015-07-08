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

    # Build the DOM
    bs = BeautifulSoup(page.text)

    # Find disco structure in DOM and iterate it
    discos_raw = bs.findAll(*rules['discos'])
    logger.info("discos en raw: {}".format(len(discos_raw)))

    titulo = discos_raw[0].find(*rules['title'])
    logger.info("titulo del primer disco: {}".format(titulo.text))

    titulo = discos_raw[1].find(*rules['title'])
    logger.info("titulo del segundo disco: {}".format(titulo.text))

    author = discos_raw[2].find(*rules['author'])
    logger.info("autor del tercer disco: {}".format(author.text))

    # Create a disco class for each disco with its fields

    logger.info("Spider collects {} discs ".format(len(discos)))
