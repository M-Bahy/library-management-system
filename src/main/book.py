class Book:
    def __init__(self, title, authors, price, isbn):
        self.__title = title
        self.__authors = authors
        self.__price = price
        self.__isbn = isbn
        self.__availability = True

    def __str__(self):
        return (
            "Title: "
            + self.__title
            + " Authors: "
            + ", ".join(self.__authors)
            + " Price: "
            + str(self.__price)
            + " isbn: "
            + self.__isbn
            + " Availability: "
            + str(self.__availability)
        )

    def get_title(self):
        return self.__title

    def get_authors(self):
        return self.__authors

    def get_price(self):
        return self.__price

    def get_isbn(self):
        return self.__isbn

    def get_availability(self):
        return self.__availability

    def set_availability(self, availability):
        self.__availability = availability
