from sqlobject import SQLObject, IntCol, MultipleJoin, ForeignKey


class Chapter(SQLObject):
    number = IntCol()
    verses = MultipleJoin('Verse')
    book = ForeignKey('Book')