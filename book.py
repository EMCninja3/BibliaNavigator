from sqlobject import SQLObject, IntCol, MultipleJoin, StringCol


class Book(SQLObject):
    """
    class Book(SQLObject):
    booknumber = IntCol(default=None)
    bookname = StringCol()
    chapters = MultipleJoin('Chapter')
    """
    number = IntCol(default=None)
    name = StringCol()
    chapters = MultipleJoin('Chapter')
    version = StringCol()
