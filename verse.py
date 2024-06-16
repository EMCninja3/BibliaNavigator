from sqlobject import SQLObject, StringCol, IntCol, ForeignKey


class Verse(SQLObject):
    number = IntCol()
    content = StringCol()
    title = StringCol(default=None)
    chapter = ForeignKey('Chapter')