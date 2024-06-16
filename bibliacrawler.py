import tkinter as tk
import requests
from PIL import Image, ImageTk
from capitelextractor import CapitelExtractor
from database import Database

db = Database()
db.initialize()


class BibliaCrawler:
    url = None
    def __init__(self, url):
        self.url = url

    def crawl(self):
        next_url = self.url
        last_url = ""
        second_last_url = ""
        capitel = None
        count = 0
        while last_url != next_url and next_url != second_last_url:
            second_last_url = last_url
            last_url = next_url
            webpage = requests.get(next_url, 'html.parser')
            capitel = CapitelExtractor(webpage, next_url)
            next_url = capitel.next_chapter_link
            count += 1
            if count > 100:
                break
        print("Crawler finished!!!")
        print("Crawler finished!!!")
        print("Crawler finished!!!")

    # print(capitel.whole_title)