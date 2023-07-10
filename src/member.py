class Member:
    borrowed_books = []

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def __str__(self):
        return "Name : " + self.__name + ", ID : " + str(self.__id)

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def borrow_book(self, book, library):
        if book not in library.books:
            raise Exception("Book not found")
        self.borrowed_books.append(book)
        library.remove_book(book)
        book.set_availability(False)

    def return_book(self, book, library):
        if book not in library.books:
            raise Exception("Book not found")
        self.borrowed_books.remove(book)
        library.add_book(book)
        book.set_availability(True)
