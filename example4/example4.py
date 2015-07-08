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
    rules = {'discos': ('discos_list',),
             'id': ('span', {'class', 'id'}),
             'title': ('h1', {'class', 'titulo'}),
             'author': ('span', {'class', 'author'}),
             'link': ('a', {'class', 'spotifylink'}),
             'image': ('img',),
             'canciones': ('span', {'class', 'cancion'}),
             }

    # Retrieve the page with Selenium
    driver = webdriver.PhantomJS(service_log_path='/dev/null')
    driver.get(url)
    pages = 1

    page = BeautifulSoup(driver.page_source)

    # Retrieve the discs in first page
    for disco_raw in page.findAll(*rules['discos']):
        discos.append(
            Disco(id=disco_raw.find(*rules['id']).text,  # chaged this rule..
                  title=disco_raw.find(*rules['title']).text,
                  author=disco_raw.find(*rules['author']).text,
                  link=disco_raw.find(*rules['link'])['href'],
                  image=disco_raw.find(*rules['image'])['src'],
                  canciones=[cancion.text for cancion in disco_raw.findAll(*rules['canciones'])]
                  )
            )

    # Find next_page button
    next_page = driver.find_element_by_class_name('btn')

    # look for a  visible next page button
    while next_page and next_page.is_displayed():
        # next page clicking the button
        next_page.click()
        pages += 1

        # Retrieve the discs in page
        page = BeautifulSoup(driver.page_source)

        for disco_raw in page.findAll(*rules['discos']):
            discos.append(
                Disco(id=disco_raw.find(*rules['id']).text,
                      title=disco_raw.find(*rules['title']).text,
                      author=disco_raw.find(*rules['author']).text,
                      link=disco_raw.find(*rules['link'])['href'],
                      image=disco_raw.find(*rules['image'])['src'],
                      canciones=[cancion.text for cancion in disco_raw.findAll(*rules['canciones'])]
                      )
            )

        # find next page button
        next_page = driver.find_element_by_class_name('btn')

    logger.info("Spider with seleniun visits {} pages ".format(pages))
    logger.info("Spider collects {} discs ".format(len(discos)))
