class Member : # name, ID, and a list of borrowed books.
    borrowed_books = None
    def __init__(self, name, age) :
        self.__name = name
        self.__id = age

    def __str__(self) :
        return "Name : " + self.__name + ", ID : " + str(self.__id)
    
    def getName(self) :
        return self.__name
    def getID(self) :
        return self.__id
    
    def borrowBook(self, book , library) :
        if self.borrowed_books == None:
            self.borrowed_books = []
        if book in library.books:
            self.borrowed_books.append(book)
            library.removeBook(book)
            book.setAvilability(False)
        else:
            print("Book not found")
            
    def returnBook(self, book, library) :
        if self.borrowed_books == None:
            self.borrowed_books = []
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.addBook(book)
            book.setAvilability(True)
        else:
            print("Book not found")