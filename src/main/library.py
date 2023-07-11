class Library:
    books = []

    def __init__(self, name):
        self.__name = name

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_by_title(self, title):
        filtered_books = [book for book in self.books if title == book.get_title()]
        if not filtered_books:
            raise Exception("No book with this title")
        else:
            return filtered_books

    def get_name(self):
        return self.__name
