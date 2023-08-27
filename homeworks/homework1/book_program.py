from book import Book
from  person import Person

book_1 = Book("Mina olin siin", "Sass Henno", 200, 18)
person_1 = Person("Signe", 24)

book_1.add_rating(5)
book_1.add_rating(5)
book_1.add_rating(4)
book_1.add_rating(3)

average = book_1.get_average_rating()
print("The rating of the first book is", average)
