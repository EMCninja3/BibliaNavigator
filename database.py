import os

from sqlobject import sqlhub, connectionForURI
from sqlobject.sqlite import builder

from book import Book
from chapter import Chapter
from verse import Verse


class Database:
    def __init__(self, db_path="database.sqlite"):
        db_filename = os.path.abspath(db_path)
        connection_string = "sqlite:" + db_filename
        self.connection = connectionForURI(connection_string)
        sqlhub.processConnection = self.connection

    def initialize(self):
        if not Book.tableExists():
            Book.createTable()
        if not Chapter.tableExists():
            Chapter.createTable()
        if not Verse.tableExists():
            Verse.createTable()