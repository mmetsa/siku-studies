# Homework 1

## Lets create a Library program

Take a look at the files `book.py` and `person.py`. Make sure
you understand them.

#### Create the following methods in the `book.py` class
* `def add_rating(self, rating)`

This method should add a rating to the ratings list.

* `def get_average_rating(self)`

This method should return the average rating of the book.
You can get the average rating by adding all the ratings
together and dividing it by the amount of ratings.
`average = sum(ratings) / amount(ratings)`

#### Create the following methods in the `person.py` class
* `def read_book(self, book, rating)`

If the person age is smaller than the books `min_age` then raise
an Exception with the message "Too young to read!".

Otherwise, this method should add a `Book` object to the `books_read` list.
This should also add a new rating to the `Book` object.