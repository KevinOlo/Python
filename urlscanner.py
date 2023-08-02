#Program to see what's contained in HTML title tagL

import requests
from bs4 import BeautifulSoup #web scraper


def scan_url(url):
    try:
        response= requests.get(url) #sends Get request and stores response
        response.raise_for_status #checks HTTP status code

        info = BeautifulSoup(response.content, 'html.parser')
        title = info.title.string    #put parsed data in string format from title HTML tag
        print(title, 'title')

    except requests.exceptions.RequestException as e:
        print("Error:", e)

to_scan = input('What''s the full URL you would like to scan?   ')

url_to_scan = to_scan
scan_url(url_to_scan)
