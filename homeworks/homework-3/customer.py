from cart import Cart

class Customer:

    def __init__(self, name, email, cash):
        self.__name = name
        self.__email = email
        self.__cash = cash
        self.__cart = Cart()

    def add_to_cart(self, product, quantity):
        # Add item to cart
        pass

    def complete_purchase(self):
        # Calculate the total, take it away from the cash
        # If there is not enough cash, raise Exception
        # Empty the cart when purchase is done.
        pass