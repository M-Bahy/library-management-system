class Member:
    borrowed_books = None

    def __init__(self, name, age):
        self.__name = name
        self.__id = age

    def __str__(self):
        return "Name : " + self.__name + ", ID : " + str(self.__id)

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def borrow_book(self, book, library):
        if self.borrowed_books is None:
            self.borrowed_books = []
        if book in library.books:
            self.borrowed_books.append(book)
            library.remove_book(book)
            book.set_availability(False)
        else:
            raise Exception("Book not found")

    def return_book(self, book, library):
        if self.borrowed_books is None:
            self.borrowed_books = []
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.add_book(book)
            book.set_availability(True)
        else:
            raise Exception("Book not found")
