import requests
from bs4 import BeautifulSoup
import re

from book import Book
from chapter import Chapter
from database import Database
from verse import Verse


class CapitelExtractor:
    book = None
    chapter = None

    def __init__(self, webpage):
        self.domain = "https://www.bible.com"
        self.webpage = webpage
        self.whole_title = ""
        self.book_title = ""
        self.book_number = 0
        self.chapter_number = 0
        self.next_chapter_link = ""
        self.text = ""
        self.all_verses = []
        self.dictionary = dict()
        self.chapter = 0
        self.soup = BeautifulSoup(self.webpage.content, 'html.parser')
        # self.soup = BeautifulSoup(self.webpage.content, 'html5lib')
        #print(self.soup)
        self.text = self.soup.findAll("span")
        # for i in self.text:
        #     print(i.string)
        self.get_text_content_new()
        self.convert_to_swiss_german_letters()
        self.text = self.remove_hashtag_comments(self.text)
        self.put_brackets_in_same_line()
        self.put_angle_brackets_in_same_line()
        self.remove_double_lines()
        self.remove_empty_lines()
        self.set_capitel_title()
        self.set_dictionary()
        self.set_book_meta_data()
        #self.db = Database()
        self.create_book_and_chapter()

        self.set_all_verses_from_text()

        self.set_next_chapter_link()
        # print(self.text)
        #print(self.dictionary)

    def book_exists(self, book_title):
        return Book.select(Book.q.bookname == book_title)

    def create_book_and_chapter(self):
        self.book = self.book_exists(self.book_title)
        print(f"book count  = {self.book.count()}")
        if self.book.count() == 0:
            self.book = Book(booknumber=self.book_number, bookname= self.book_title)
            self.chapter = Chapter(number=int(self.chapter_number), book=self.book)
            #self.book.chapters.append(self.chapter)
        else:
            self.chapter = Chapter(number=int(self.chapter_number), book=self.book)
            #self.book.chapters.append(self.chapter)
        # if book != None:
        #     book.

    def get_text_content_new(self):
        text = ""
        #lastLine = ""
        to_delete = []
        actual_delete = ""
        for line in self.text:
            # ChapterContent_body__O3qjr
            if line['class'] == ['ChapterContent_body__O3qjr']:
                text += "<"
                for i in line:
                    if i.string != None:
                        actual_delete += i.string + "\n"
                        #lastLine += i.string + "\n"
                        text += i.string
                to_delete.append(actual_delete)
                actual_delete = ""
                text += ">\n"
            elif line['class'] == ['ChapterContent_heading__xBDcs']:
                text += "["
                for i in line:
                    if i.string != None:
                        actual_delete += i.string + "\n"
                        #lastLine += i.string + "\n"
                        text += i.string
                to_delete.append(actual_delete)
                actual_delete = ""
                text += "]\n"
            else:
                if line.string != None:
                    text += line.string + "\n"
        for i in to_delete:
            text = text.replace(i, '')
        self.text = text

    def set_next_chapter_link(self):
        links = self.soup.find_all("a")
        text = ""
        for link in links:
            if link.get('href') != None:
                text += link.get('href') + "\n"
        # print(text)
        link = re.findall(r"/de/bible/.*", text)
        self.next_chapter_link = self.domain + link[-1]

    def set_all_verses_from_text(self):
        pattern = r"(?P<title>\[.*\].*\n)?(?P<number>\d\d?)(?P<content>\n.*)"
        text = self.text
        compiled = re.compile(pattern)
        #verses = []
        while compiled.search(text):
            match = compiled.search(text)
            title = match.group('title')
            if title == None:
                title = ""
            number = int(match.group('number'))
            content = match.group('content')
            text = text.replace(title + str(number) + content, '')
            verse = Verse(number=number, content=content, title=title, chapter=self.chapter)
            #verses.append(verse)
        #self.all_verses = verses



    def put_brackets_in_same_line(self):
        while re.search(r"\n\[\(\]\s.*\s\[\)\]", self.text) != None:
            match = re.search(r"\n\[\(\]\s.*\s\[\)\]", self.text)
            text = match.group()
            text = text.replace("\n", "")
            text = text.replace("[", "")
            text = text.replace("]", "")
            self.text = re.sub(r"\n\[\(\]\s.*\s\[\)\]", " " + text, self.text)

    def put_angle_brackets_in_same_line(self):
        notes = re.findall(r"\n\s\<.*\>\n", self.text)
        if notes != None:
            for note in notes:
                text = note.replace("\n", "")
                self.text = self.text.replace(note, text)

    # def mark_all_subtitles(self):
    #     subtitle =
    def set_capitel_title(self):
        text = self.soup.find_all("h1")
        self.whole_title = text[0].string

    def set_book_meta_data(self):
        print("*****" + self.whole_title + "*****")
        match = re.search(r"(?P<book_number>\d?)\.?\s?(?P<book_title>.*)\s(?P<chapter_number>\d*)", self.whole_title)
        self.book_title = match.group('book_title')
        self.book_number = match.group('book_number')
        #print(f"book = {self.book_number}")
        if self.book_number == "":
            self.book_number = None
        else:
            print("book numb " +self.book_number)
            self.book_number = int(self.book_number)
        self.chapter_number = match.group('chapter_number')
        print(f"chapter = {self.chapter_number} booktitle= {self.book_title} chapter_number= {self.chapter_number}")
        print("************\n")

    def convert_to_swiss_german_letters(self):
        self.text = self.text.replace('ß', 'ss')

    def remove_hashtag_comments(self, text):
        return re.sub("#.*", "", text)

    def starts_with_numbers(self, text):
        return text.isnumeric()

    def get_all_verses_with_verse_number(self):
        return re.findall(r"\d{1,2}?\n{1}.*", self.text)


    def get_number_from_verse(self, text):
        return re.search(r"\d\d*", text)


    def get_text_from_verse(self, text, number):
        return text[len(number):]

    def set_dictionary(self):
        verses = self.get_all_verses_with_verse_number()
        dictionary = dict()

        for verse in verses:
            #print(verse)
            number = self.get_number_from_verse(verse).group()
            text = self.get_text_from_verse(verse, number).replace('\n', '')
            dictionary[number] = text
        self.dictionary = dictionary

    def remove_double_lines(self):
        newText = ""
        lastLine = ""
        for line in self.text.splitlines():
            if lastLine != line:
                newText += line + "\n"
            lastLine = line
        self.text = newText

    def remove_empty_lines(self):
        newText = ""
        for line in self.text.splitlines():
            if line != " " and line != "\n" and line != "":
                newText += line + "\n"
        self.text = newText
