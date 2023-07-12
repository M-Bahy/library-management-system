import sys
import unittest

sys.path.append("src\main")
from book import Book
from library import Library


def bahy(f):
    def wrapper(*args, **kwargs):
        library = Library("Helsinki Public Library")
        book = Book(
            "The Catcher in the Rye", ["J. D. Salinger"], 10, "0316769177"
        )
        library.add_book(book)
        f(*args, library, book, **kwargs)

    return wrapper


class TestLibrary(unittest.TestCase):
    @bahy
    def test_add_book(self, library, book):
        self.assertEqual(library.books, [book])

    @bahy
    def test_remove_book(self, library, book):
        library.remove_book(book)
        self.assertEqual(library.books, [])

    @bahy
    def test_get_name(self, library, book):
        self.assertEqual(library.get_name(), "Helsinki Public Library")

    @bahy
    def test_search_by_title(self, library, book):
        self.assertEqual(
            library.search_by_title("The Catcher in the Rye"), [book]
        )


# unittest.main()
