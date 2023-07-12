import sys
import unittest

sys.path.append("src\main")
from book import Book
from library import Library
from member import Member


class TestMember(unittest.TestCase):
    def setUp(self):
        self.library = Library("Alexandria Library")
        self.book1 = Book("The Alchemist", "Paulo Coelho", 5, "9780061122415")
        self.book2 = Book(
            "The Catcher in the Rye", "J.D. Salinger", 8, "9780316769488"
        )
        self.book3 = Book(
            "To Kill a Mockingbird", "Harper Lee", 20, "9780446310789"
        )
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        self.member = Member("John Doe", 12345)

    def test_get_name(self):
        self.assertEqual(self.member.get_name(), "John Doe")

    def test_get_id(self):
        self.assertEqual(self.member.get_id(), 12345)

    def test_borrow_book(self):
        self.member.borrow_book(self.book1, self.library)
        self.assertEqual(len(self.member.borrowed_books), 1)
        self.assertEqual(len(self.library.books), 2)
        self.assertFalse(self.book1.get_availability())

    def test_return_book(self):
        self.member.borrow_book(self.book2, self.library)
        self.member.return_book(self.book2, self.library)
        self.assertEqual(len(self.member.borrowed_books), 0)
        self.assertEqual(len(self.library.books), 3)
        self.assertTrue(self.book2.get_availability())

    def test_borrow_nonexistent_book(self):
        with self.assertRaises(Exception):
            self.member.borrow_book(
                Book("Nonexistent Book", "Unknown Author", 8, "1234567890"),
                self.library,
            )

    def test_return_nonexistent_book(self):
        with self.assertRaises(Exception):
            self.member.return_book(
                Book("Nonexistent Book", "Unknown Author", 8, "1234567890"),
                self.library,
            )


# if __name__ == "__main__":
#     unittest.main()
