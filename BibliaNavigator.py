import tkinter as tk
from bs4 import BeautifulSoup
# import urllib3
import requests
import re
from PIL import Image, ImageTk


def get_text_content(content):
    text = ""
    for i in content:
        if i.string is not None and i.string != ' ':
            if len(text) > 0:
                if text[-1] == '#':
                    text += i.string + "#\n"
                elif text[-1] == '\n':
                    text += i.string
                else:
                    text += "\n" + i.string
            else:
                text += i.string
    return text


def convert_to_swiss_german_letters(text):
    return text.replace('ß', 'ss')


def remove_hashtag_comments(text):
    return re.sub("#.*#", "", text)

def remove_subtitle():
    pass

def starts_with_numbers(text):
    return text.isnumeric()


def convert_to_dictionary(text):
    text = text.split("\n")
    while "" in text:
        text.remove("")
    dictionary = dict()
    number = -1
    content = ""
    for line in text:
        if starts_with_numbers(line):
            number = int(line) - 1
            if content != "":
                dictionary[number] = content
                content = ""
        else:
            content += line
    dictionary[number] = content
    return dictionary


image = Image.open('python_img.jpeg')
image = image.resize((500, 300))

# http = urllib3.PoolManager()
url = 'https://www.bible.com/de/bible/73/GEN.1.HFA'
#url = "https://www.bible.com/de/bible/58/GEN.1.ELB71"
# url = "https://www.bible.com/de/bible/149/GEN.1.RVR1960"
url = "https://www.bible.com/de/bible/149/GEN.2.RVR1960"
# url = "https://www.bible.com/de/bible/149/GEN.3.RVR1960"
url = "https://www.bible.com/de/bible/149/GEN.9.RVR1960"
webpage = requests.get(url, 'html.parser')
#response = http.request('GET', url)
soup = BeautifulSoup(webpage.content, features="html.parser")

result = soup.findAll("span")
print(result)
text = convert_to_swiss_german_letters(get_text_content(result))
# print(text)
text = remove_hashtag_comments(text)
# print(text)
dictionary = convert_to_dictionary(text)
# print(dictionary)

## Set the widget (GUI)
root = tk.Tk()
root.geometry('1280x800')
# img = ImageTk.PhotoImage(image)
title = tk.Label(root, text="BibliaNavigator", bg="red", fg="white")
title.pack()
# label = tk.Label(root, image=img)
#lblCapitel = tk.Label(root, text=text, wraplength=500)
scroll_bar = tk.Scrollbar(root, orient="vertical")
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget = tk.Text(root, font=("Arial", 30), yscrollcommand=scroll_bar.set)
text_widget.pack(side=tk.LEFT)
text_widget.insert(tk.END, text)
scroll_bar.config(command=text_widget.yview)
# label.pack()
#lblCapitel.pack()

root.title('BibliaNavigator by M. Fässler')

root.mainloop()
