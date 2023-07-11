import sys
import unittest

sys.path.append("src\main")
from book import Book


class TestBook(unittest.TestCase):
    def test_get_title(self):
        b = Book(
            "The Catcher in the Rye", ["J. D. Salinger"], 10, "0316769177"
        )
        self.assertEqual(b.get_title(), "The Catcher in the Rye")

    def test_get_authors(self):
        b = Book(
            "The Catcher in the Rye", ["J. D. Salinger"], 10, "0316769177"
        )
        self.assertEqual(b.get_authors(), ["J. D. Salinger"])

    def test_get_price(self):
        b = Book(
            "The Catcher in the Rye", ["J. D. Salinger"], 10, "0316769177"
        )
        self.assertEqual(b.get_price(), 10)

    def test_get_isbn(self):
        b = Book(
            "The Catcher in the Rye", ["J. D. Salinger"], 10, "0316769177"
        )
        self.assertEqual(b.get_isbn(), "0316769177")

    def test_get_availability(self):
        b = Book(
            "The Catcher in the Rye", ["J. D. Salinger"], 10, "0316769177"
        )
        self.assertEqual(b.get_availability(), True)

    def test_set_availability(self):
        b = Book(
            "The Catcher in the Rye", ["J. D. Salinger"], 10, "0316769177"
        )
        b.set_availability(False)
        self.assertEqual(b.get_availability(), False)


unittest.main()
