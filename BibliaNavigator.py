import tkinter as tk
from tkinter import ttk, font

import requests
from PIL import Image, ImageTk
from sqlobject import AND

from book import Book
from capitelextractor import CapitelExtractor
from chapter import Chapter
from database import Database
from bibliacrawler import BibliaCrawler
from verse import Verse

db = Database()
db.initialize()

url0 = "https://www.bible.com/de/bible/149/EXO.INTRO1.RVR1960"
url1 = 'https://www.bible.com/de/bible/73/GEN.1.HFA'
url2 = "https://www.bible.com/de/bible/58/GEN.1.ELB71"
url3 = "https://www.bible.com/de/bible/149/GEN.1.RVR1960"
url4 = "https://www.bible.com/de/bible/149/GEN.2.RVR1960"
url5 = "https://www.bible.com/de/bible/149/GEN.3.RVR1960"
url6 = "https://www.bible.com/de/bible/149/GEN.9.RVR1960"
url7 = "https://www.bible.com/de/bible/149/2SA.12.RVR1960"
url8 = "https://www.bible.com/de/bible/149/REV.22.RVR1960"
urls = [url0, url1, url2, url3, url4, url5, url6, url7, url8]

# crawler = BibliaCrawler()
# crawler.crawl()

chapter_title = "Fertig"
result = "Fertig"

## Set the widget (GUI)
root = tk.Tk()
root.geometry('1280x800')
# img = ImageTk.PhotoImage(image)
frame = ttk.Frame(root)
frame.grid(row=1, column=0, sticky='nsew')

canvas = tk.Canvas(frame)
scroll_bar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scroll_bar.set)

content_frame = ttk.Frame(canvas)
content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

font_size = 34
custom_font = font.Font(family='Helvetica', size=font_size)
# label = ttk.Label(content_frame, text="", font=custom_font , wraplength=1000)
# label.grid(row=0, column=0, pady=5)


search_frame = ttk.Frame(root)
search_frame.grid(row=0, column=0, sticky='ew', pady=10)
search_label = ttk.Label(search_frame, text="Search")
search_label.grid(row=0, column=0, pady=5)
search_entry = ttk.Entry(search_frame, width=50)
search_entry.grid(row=0, column=1, pady=5)
search_button = ttk.Button(search_frame, text="Suchen", command=lambda: search_chapter(search_entry.get()))
search_button.grid(row=0, column=2, pady=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

canvas.create_window((0, 0), window=content_frame, anchor='nw')
canvas.grid(row=0, column=0, sticky='nsew')
scroll_bar.grid(row=0, column=1, sticky='ns')
default_color = canvas.cget("background")

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta*4 /3)), 'units')

def _on_keydown(event):
    global font_size, label
    print(event.keysym)
    if event.keysym == 'Up':
        font_size += 1
    elif event.keysym == 'Down':
        font_size -= 1
    elif event.keysym == 'Return':
        search_chapter(search_entry.get())
    custom_font = font.Font(family='Helvetica', size=font_size)
    # label.configure(font=custom_font)
    # label.update_idletasks()
    for l in last_widgets:
        l.configure(font=custom_font)
        l.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def _on_hover(label):
    label.bind("<Enter>", func=lambda e: label.config(background="blue"))
    label.bind("<Leave>", func=lambda e: label.config(background=default_color))
tk.Label()


canvas.bind_all("<MouseWheel>", _on_mousewheel)
canvas.bind_all("<KeyPress>", _on_keydown)

last_widgets = list()
def search_chapter(search_query):
    global last_widgets
    try:
        # label.config(text="")
        for l in last_widgets:
            l.destroy()
        last_widgets = list()
        search = search_query.split()
        book_name, chapter_number, book_number = None, None, None
        if(len(search) == 2):
            book_name, chapter_number = search
        else:
            book_number, book_name, chapter_number = search
            book_number = int(book_number)
        #book_name, chapter_number = search_query.split()
        chapter_number = int(chapter_number)
        book = Book.select(AND(Book.q.name == book_name, AND(Book.q.version =="ELB71", Book.q.number== book_number))).getOne(None)
        if book:
            chapter = Chapter.select(AND(Chapter.q.book == book.id, Chapter.q.number == chapter_number)).getOne(None)
            if chapter:
                verses = Verse.select(Verse.q.chapter == chapter.id)
                text = '\n'.join([f"{verse.number}. {remove_newline(verse.content)}" for verse in verses])
                i = 1
                print(f"verses = {verses.count()}")
                for verse in verses:
                    l2 = None
                    if verse.title != "":
                        cfont = font.Font(family='Helvetica', size=font_size, weight="bold")
                        text = verse.title
                        text = text.replace("[", "")
                        text = text.replace("]", "")
                        l2 = tk.Label(content_frame, text=text, font=cfont)
                        l2.grid(row=i, column=0)
                    i += 1
                    l1 = tk.Label(content_frame, text=verse.number, font=custom_font)
                    l1.grid(row=i, column=0)
                    i += 1
                    l = tk.Label(content_frame, text=verse.content, font=custom_font, wraplength=1000)
                    l.grid(row=i, column=0)
                    if l2:
                        last_widgets.append(l2)
                    last_widgets.append(l1)
                    last_widgets.append(l)
                    i+=1
                #label. config(text=text)
            else:
                print("Chapter not found.")
                # label.config(text="Chapter not found.")
        else:
            print("Book not found.")
            # label.config(text="Book not found.")
    except Exception as e:
        print(e)
        # label.config(text=f"Error: {str(e)}")
    for l in last_widgets:
        _on_hover(l)

def remove_newline(text=""):
    return text.replace("\n", "")

# tk.Label(root, text="Suche Kapitel").grid(row=0)
# entry = tk.Entry(root)
# entry.grid(row=0, column=1)

# title = tk.Label(root, text=chapter_title, bg="red", fg="white").grid(row=1)

# title.pack()
# label = tk.Label(root, image=img)
# lblCapitel = tk.Label(root, text=text, wraplength=500)

# text_widget = tk.Text(root, font=("Arial", 30), yscrollcommand=scroll_bar.set)
# text_widget.pack(side=tk.LEFT)
# text_widget.insert(tk.END, result)
# scroll_bar.config(command=text_widget.yview)

# label.pack()
# lblCapitel.pack()

root.title('BibliaNavigator by M. Fässler')

root.mainloop()
