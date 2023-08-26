class Product:

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def update_quantity(self, purchased_amount):
        if self.__quantity > purchased_amount:
            self.__quantity -= purchased_amount
        else:
            raise Exception("Not so many in stock!")

