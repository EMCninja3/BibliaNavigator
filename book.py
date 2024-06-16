from sqlobject import SQLObject, IntCol, MultipleJoin, StringCol


class Book(SQLObject):
    """
    class Book(SQLObject):
    booknumber = IntCol(default=None)
    bookname = StringCol()
    chapters = MultipleJoin('Chapter')
    """
    booknumber = IntCol(default=None)
    bookname = StringCol()
    chapters = MultipleJoin('Chapter')
