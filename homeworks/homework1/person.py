class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__books_read = []

    def read_book(self, book, rating):
        if self.__age < book.get_min_age():
            raise Exception("Too young to read!")
        self.__books_read.append(book)
        book.add_rating(rating)