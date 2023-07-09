class Library:  # methods to add books, remove books, and search for books.
    books = None

    def __init__(self, name):
        self.__name = name

    def add_book(self, book):
        if self.books is None:
            self.books = []
        self.books.append(book)

    def remove_book(self, book):
        if self.books is None:
            self.books = []
        if book in self.books:
            self.books.remove(book)

    def search_by_title(self, title):
        if self.books is None:
            self.books = []
        for book in self.books:
            if title == book.get_title():
                print(book)

    def get_name(self):
        return self.__name
