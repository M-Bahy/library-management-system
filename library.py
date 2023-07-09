import fnmatch
class Library: #Managing the collection of books, providing methods to add books, remove books, and search for books.
    books  = None
    
    def __init__(self, name):
        self.__name = name
        
    def addBook(self, book):
        if self.books == None:
            self.books = []
        self.books.append(book)
        
        
    def removeBook(self, book):
        if self.books == None:
            self.books = []
        if book in self.books:
            self.books.remove(book)
        
            
    def searchByTitle(self, title):
        if self.books == None:
            self.books = []
        pattern = "*{}*".format("*".join(title))
        filtered_books = [b for b in self.books if fnmatch.fnmatchcase(b, pattern)]
        if len(filtered_books) == 0:
            print("No books found")
        else:
            print(filtered_books)

    def getName(self):
        return self.__name