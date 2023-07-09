import fnmatch


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
        pattern = "*{}*".format("*".join(title))
        filtered_books = [b for b in self.books
                          if fnmatch.fnmatchcase(b, pattern)]
        if len(filtered_books) == 0:
            print("No books found")
        else:
            print(filtered_books)

    def get_name(self):
        return self.__name
