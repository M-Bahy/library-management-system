class Book:  # title, author, ISBN, availability status,
    def __init__(self, title, author, price, ISBN):
        self.__title = title
        self.__author = author
        self.__price = price
        self.__ISBN = ISBN
        self.__availability = True

    def __str__(self):
        return (
            "Title: "
            + self.__title
            + " Author: "
            + self.__author
            + " Price: "
            + str(self.__price)
            + " ISBN: "
            + self.__ISBN
            + " Availability: "
            + str(self.__availability)
        )

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def get_ISBN(self):
        return self.__ISBN

    def get_availability(self):
        return self.__availability

    def set_availability(self, availability):
        self.__availability = availability
