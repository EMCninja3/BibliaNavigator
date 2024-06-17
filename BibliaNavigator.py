import tkinter as tk
from tkinter import ttk, font

import requests
from PIL import Image, ImageTk

from capitelextractor import CapitelExtractor
from database import Database
from bibliacrawler import BibliaCrawler

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

# crawler = BibliaCrawler(url2)
# crawler.crawl()

chapter_title = "Fertig"
result = "Fertig"

## Set the widget (GUI)
root = tk.Tk()
root.geometry('1280x800')
# img = ImageTk.PhotoImage(image)
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky='nsew')

canvas = tk.Canvas(frame)
scroll_bar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scroll_bar.set)

content_frame = ttk.Frame(canvas)
content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

text = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
aliquyam erat, sed diam voluptua. At vero eos et accusam et justo 
duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata 
sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt 
ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero 
eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren
, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum do
lor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At v
ero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gube
rgren, no sea takimata sanctus est Lorem ipsum dolor sit amet.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse mole
stie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros 
et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril d
elenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit 
amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidun
t ut laoreet dolore magna aliquam erat volutpat.   

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper susc
ipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eu
m iriure dolor in hendrerit in vulputate velit esse molestie consequat, ve
l illum dolore eu feugiat nulla facilisis at vero eros et accumsan et ius
to odio dignissim qui blandit praesent luptatum zzril delenit augue duis d
olore te feugait nulla facilisi.   

Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet d
oming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet
, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt 
 laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam
 , quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliqu
 ip ex ea commodo consequat.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse moles
tie consequat, vel illum dolore eu feugiat nulla facilisis.   

At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
 gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore
 m ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eir
 mod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam vo
 luptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet cl
 ita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit am
 et. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, At accusam 
 
 aliquyam diam diam dolore dolores duo eirmod eos erat, et nonumy sed temp
 or et et invidunt justo labore Stet clita ea et gubergren, kasd magna no 
 rebum. sanctus sea sed takimata ut vero voluptua. est Lorem ipsum dolor s
 it amet. Lorem ipsum dolor sit amet, consetetur
 duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata 
sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt 
ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero 
eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren
, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum do
lor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At v
ero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gube
rgren, no sea takimata sanctus est Lorem ipsum dolor sit amet.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse mole
stie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros 
et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril d
elenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit 
amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidun
t ut laoreet dolore magna aliquam erat volutpat.   

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper susc
ipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eu
m iriure dolor in hendrerit in vulputate velit esse molestie consequat, ve
l illum dolore eu feugiat nulla facilisis at vero eros et accumsan et ius
to odio dignissim qui blandit praesent luptatum zzril delenit augue duis d
olore te feugait nulla facilisi.   

Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet d
oming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet
, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt 
 laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam
 , quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliqu
 ip ex ea commodo consequat.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse moles
tie consequat, vel illum dolore eu feugiat nulla facilisis.   

At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
 gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore
 m ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eir
 mod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam vo
 luptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet cl
 ita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit am
 et. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, At accusam 
 
 aliquyam diam diam dolore dolores duo eirmod eos erat, et nonumy sed temp
 or et et invidunt justo labore Stet clita ea et gubergren, kasd magna no 
 rebum. sanctus sea sed takimata ut vero voluptua. est Lorem ipsum dolor s
 it amet. Lorem ipsum dolor sit amet, consetetur
 duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata 
sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt 
ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero 
eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren
, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum do
lor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At v
ero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gube
rgren, no sea takimata sanctus est Lorem ipsum dolor sit amet.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse mole
stie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros 
et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril d
elenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit 
amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidun
t ut laoreet dolore magna aliquam erat volutpat.   

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper susc
ipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eu
m iriure dolor in hendrerit in vulputate velit esse molestie consequat, ve
l illum dolore eu feugiat nulla facilisis at vero eros et accumsan et ius
to odio dignissim qui blandit praesent luptatum zzril delenit augue duis d
olore te feugait nulla facilisi.   

Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet d
oming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet
, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt 
 laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam
 , quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliqu
 ip ex ea commodo consequat.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse moles
tie consequat, vel illum dolore eu feugiat nulla facilisis.   

At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
 gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore
 m ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eir
 mod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam vo
 luptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet cl
 ita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit am
 et. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, At accusam 
 
 aliquyam diam diam dolore dolores duo eirmod eos erat, et nonumy sed temp
 or et et invidunt justo labore Stet clita ea et gubergren, kasd magna no 
 rebum. sanctus sea sed takimata ut vero voluptua. est Lorem ipsum dolor s
 it amet. Lorem ipsum dolor sit amet, consetetur"""
font_size = 84
custom_font = font.Font(family='Helvetica', size=font_size)
label = ttk.Label(content_frame, text=text, font=custom_font , wraplength=1000)
label.grid(row=0, column=0, pady=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

canvas.create_window((0, 0), window=content_frame, anchor='nw')
canvas.grid(row=0, column=0, sticky='nsew')
scroll_bar.grid(row=0, column=1, sticky='ns')


def _on_mousewheel(event):
    print(event.delta)
    canvas.yview_scroll(int(-1 * (event.delta*4 /3)), 'units')

def _on_keydown(event):
    global font_size, label
    print(font_size)
    if event.keysym == 'Up':
        font_size += 1
    elif event.keysym == 'Down':
        font_size -= 1

    custom_font = font.Font(family='Helvetica', size=font_size)
    label.configure(font=custom_font)
    label.update_idletasks()
    #label.config(scrollregion=canvas.bbox("all"))
    print(event.keysym)



canvas.bind_all("<MouseWheel>", _on_mousewheel)
canvas.bind_all("<KeyPress>", _on_keydown)

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
