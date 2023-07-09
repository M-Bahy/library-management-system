class Book : #title, author, ISBN, availability status,
    def __init__(self, title, author, price, ISBN) :
        self.__title = title
        self.__author = author
        self.__price = price
        self.__ISBN = ISBN
        self.__availability = True

    def __str__(self) :
        return "Title: " + self.__title + " Author: " + self.__author \
    + " Price: " + str(self.__price) + " ISBN: " + self.__ISBN \
    + " Availability: " + str(self.__availability)
    
    def getTitle(self) :
        return self.__title
    def getAuthor(self) :
        return self.__author
    def getPrice(self) :
        return self.__price
    def getISBN(self) :
        return self.__ISBN
    def getAvailability(self) :
        return self.__availability
    def setAvilability(self, availability) :
        self.__availability = availability