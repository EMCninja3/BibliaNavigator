import tkinter as tk
from datetime import datetime

import requests
from capitelextractor import CapitelExtractor

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
        start_time = datetime.now()
        while last_url != next_url and next_url != second_last_url:
            second_last_url = last_url
            last_url = next_url
            webpage = requests.get(next_url, 'html.parser')
            capitel = CapitelExtractor(webpage, next_url)
            next_url = capitel.next_chapter_link
            count += 1
            duration = datetime.now() - start_time
            if count % 30 == 0:
                print(f"{100/1190*count} % done")
                print(f"running {duration.seconds} s ...")
        end_time = datetime.now()
        duration = end_time - start_time
        print(f"Number of chapters = {count}")
        print(f"Crawler finished in {duration.seconds} s.")
