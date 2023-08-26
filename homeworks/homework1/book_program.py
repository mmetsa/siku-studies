from book import Book

book_1 = Book("Mina olin siin", "Sass Henno", 200, 18)

book_1.add_rating(5)
book_1.add_rating(5)
book_1.add_rating(4)
book_1.add_rating(3)

average = book_1.get_average_rating()
print("The rating of the first book is", average)
