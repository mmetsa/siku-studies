class Book:

    def __init__(self, title, author, pages_amount, min_age):
        self.__title = title
        self.__author = author
        self.__pages_amount = pages_amount
        self.__ratings = []
        self.__min_age = min_age

