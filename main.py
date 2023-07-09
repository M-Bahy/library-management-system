from member import Member
from library import Library
from book import Book

library = Library("GUC")
b1 = Book("Harry Potter", "J.K. Rowling", 100, "1234")
b2 = Book("The Lord of the Rings", "J.R.R. Tolkien", 150, "1235")
b3 = Book("The Da Vinci Code", "Dan Brown", 200, "1236")
b4 = Book("The Alchemist", "Paulo Coelho", 100, "1237")
b5 = Book("The Little Prince", "Antoine de Saint-Exupery", 100, "1238")
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)
library.add_book(b5)
m1 = Member("Ahmed", 1)
m2 = Member("Ali", 2)
m3 = Member("Mahmoud", 3)

library.search_by_title("Harry Potter")
m1.borrow_book(b1, library)
