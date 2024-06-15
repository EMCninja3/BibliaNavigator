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
        self.whole_title = self.get_capitel_title()
        self.set_dictionary()
        # print(self.text)
        #print(self.dictionary)

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
    def get_capitel_title(self):
        text = self.soup.find_all("h1")
        return text[0].string

    # TODO implement get capitel title, book number and book title
    def set_book_meta_data(self):
        pass

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
