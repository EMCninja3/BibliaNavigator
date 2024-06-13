from bs4 import BeautifulSoup
import re


class CapitelText:
    def __init__(self, webpage):
        self.webpage = webpage
        self.whole_title = ""
        self.book_title = ""
        self.book_number = 0
        self.capitel_number = 0
        self.text = ""
        self.dictionary = dict()
        self.soup = BeautifulSoup(self.webpage.content, 'html.parser')
        # print(self.soup)
        self.text = self.soup.findAll("span")
        self.get_text_content_new()
        self.text = self.remove_hashtag_comments(self.text)
        self.put_brackets_in_same_line()
        self.remove_double_lines()
        self.remove_empty_lines()
        self.convert_to_dictionary()
        self.whole_title = self.get_capitel_title()

        self.get_all_verses_with_verse_number()
        #print(self.text)

    def get_text_content_new(self):
        text = ""
        lastLine = ""
        for line in self.text:
            # ChapterContent_body__O3qjr
            if line['class'] == ['ChapterContent_body__O3qjr']:
                text += "<"
                for i in line:
                    if i.string != None:
                        lastLine += i.string + "\n"
                        text += i.string
                text += ">\n"
            else:
                if line.string != None:
                    if line.string not in lastLine:
                        text += line.string + "\n"
                        lastLine = ""
        self.text = text

    def put_brackets_in_same_line(self):
        while re.search(r"\(\s*.*\s.*\s\)", self.text) != None:
            match = re.search(r"\(\s*.*\s.*\s\)", self.text)
            text = match.group()
            text = text.replace("\n", "")
            self.text = re.sub(r"\(\s*.*\s.*\s\)", text, self.text)

    def get_text_content(self, content):
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

    def get_capitel_title(self):
        text = self.soup.find_all("h1")
        return text[0].string

    #TODO implement get capitel title, book number and book title
    def get_book_meta_data(self):
        pass

    def convert_to_swiss_german_letters(self, text):
        return text.replace('ß', 'ss')

    def remove_hashtag_comments(self, text):
        return re.sub("#.*", "", text)

    # TODO is it needed ??? removing text explanations
    def remove_subtitle(self):
        pass

    def starts_with_numbers(self, text):
        return text.isnumeric()

    def get_all_verses_with_verse_number(self):
        return  re.findall(r"\d\d*\s.*", self.text)

    # TODO implement method
    def convert_to_dictionary(self):
        text = self.text.split("\n")
        while "" in text:
            text.remove("")
        dictionary = dict()
        number = -1
        content = ""
        for line in text:
            if self.starts_with_numbers(line):
                number = int(line) - 1
                if content != "":
                    dictionary[number] = content
                    content = ""
            else:
                content += line
        dictionary[number] = content
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
