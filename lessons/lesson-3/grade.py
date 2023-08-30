class Grade:
    def __init__(self, value, name):
        self.__value = value
        self.__name = name

    def get_value(self):
        return self.__value

    def __repr__(self):
        return str(self.__value) + " " + self.__name
