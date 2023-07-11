from book import Book


class Library:
    def __init__(self, name):
        self.__name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_by_title(self, title):
        filtered_books = [
            book for book in self.books if title == book.get_title()
        ]
        if not filtered_books:
            raise Exception("No book with this title")
        else:
            return filtered_books

    def get_name(self):
        return self.__name


l = Library("Helsinki Public Library")
b = Book("The Catcher in the Rye", ["J. D. Salinger"], 10, "0316769177")
l.add_book(b)
# x = l.search_by_title("The Catcher in the Rye")
# print(x)
print(l.books)
l.remove_book(b)
print(l.books)
