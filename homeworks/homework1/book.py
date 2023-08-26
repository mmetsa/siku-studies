class Book:

    def __init__(self, title, author, pages_amount, min_age):
        self.__title = title
        self.__author = author
        self.__pages_amount = pages_amount
        self.__ratings = []
        self.__min_age = min_age

    def add_rating(self, rating):
        self.__ratings.append(rating)

    def get_average_rating(self):
        rating_sum = int(sum(self.__ratings))
        rating_amount = len(self.__ratings)

        average_rating = rating_sum / rating_amount
        return average_rating
