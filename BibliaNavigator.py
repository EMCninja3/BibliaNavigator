import tkinter as tk
from bs4 import BeautifulSoup
# import urllib3
import requests
import re
from PIL import Image, ImageTk
from capitelextractor import CapitelExtractor

image = Image.open('python_img.jpeg')
image = image.resize((500, 300))

# http = urllib3.PoolManager()

url1 = 'https://www.bible.com/de/bible/73/GEN.1.HFA'
url2 = "https://www.bible.com/de/bible/58/GEN.1.ELB71"
url3 = "https://www.bible.com/de/bible/149/GEN.1.RVR1960"
url4 = "https://www.bible.com/de/bible/149/GEN.2.RVR1960"
url5 = "https://www.bible.com/de/bible/149/GEN.3.RVR1960"
url6 = "https://www.bible.com/de/bible/149/GEN.9.RVR1960"
url7 = "https://www.bible.com/de/bible/149/2SA.12.RVR1960"
urls = [url1, url2, url3, url4, url5, url6, url7]

capitel = None
# for url in urls[5:6]:
for url in urls[5:6]:
    webpage = requests.get(url, 'html.parser')
    capitel = CapitelExtractor(webpage)
    print(capitel.whole_title)
verses = capitel.all_verses

for verse in verses:
    print(verse.title + verse.number + verse.content)
# for i in range(1, 100):
#     webpage = requests.get(capitel.next_chapter_link, 'html.parser')
#     capitel = CapitelExtractor(webpage)
#     print(capitel.whole_title)

    #print(capitel.text)
# print(webpage.content)
### response = http.request('GET', url)
#soup = BeautifulSoup(webpage.content, features="html.parser")
#result = soup.findAll("span")

# capitel = CapitelText(webpage)
# capitel.get_title()

result = capitel.text

## Set the widget (GUI)
root = tk.Tk()
root.geometry('1280x800')
# img = ImageTk.PhotoImage(image)
title = tk.Label(root, text="BibliaNavigator", bg="red", fg="white")
title.pack()
# label = tk.Label(root, image=img)
# lblCapitel = tk.Label(root, text=text, wraplength=500)
scroll_bar = tk.Scrollbar(root, orient="vertical")
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget = tk.Text(root, font=("Arial", 30), yscrollcommand=scroll_bar.set)
text_widget.pack(side=tk.LEFT)
text_widget.insert(tk.END, result)
scroll_bar.config(command=text_widget.yview)
# label.pack()
# lblCapitel.pack()

root.title('BibliaNavigator by M. Fässler')

root.mainloop()
