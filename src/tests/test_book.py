import sys
import unittest

sys.path.append("src\main")
from book import Book


def bahy(f):
    def wrapper(*args, **kwargs):
        b = Book(
            "The Catcher in the Rye", ["J. D. Salinger"], 10, "0316769177"
        )
        f(*args, b, **kwargs)

    return wrapper


class TestBook(unittest.TestCase):
    @bahy
    def test_get_title(self, b):
        self.assertEqual(b.get_title(), "The Catcher in the Rye")

    @bahy
    def test_get_authors(self, b):
        self.assertEqual(b.get_authors(), ["J. D. Salinger"])

    @bahy
    def test_get_price(self, b):
        self.assertEqual(b.get_price(), 10)

    @bahy
    def test_get_isbn(self, b):
        self.assertEqual(b.get_isbn(), "0316769177")

    @bahy
    def test_get_availability(self, b):
        self.assertEqual(b.get_availability(), True)

    @bahy
    def test_set_availability(self, b):
        b.set_availability(False)
        self.assertEqual(b.get_availability(), False)


if __name__ == "__main__":
    unittest.main()
