class BankAccount:
    __account_number = ""
    __account_balance = 0
    __history = []
    __account_holder = ""

    def __init__(self, account_number, account_balance, account_holder):
        self.__account_number = account_number
        self.__account_balance = account_balance
        self.__account_holder = account_holder

    def add_funds(self, amount):
        self.__history.append(amount)
        self.__account_balance += amount


    def withraw(self, amount):
        # kui pole piisavalt raha
        if self.__account_balance < amount:
            raise Exception("Not enough funds.")
        # oli piisavalt raha ...
        self.__history.append(-1 * amount)
        self.__account_balance -= amount


    def get_balance(self):
        return self.__account_balance


    def get_statement(self):
        result = "Bank account " + self.__account_number + " statement:\n"
        for item in reversed(self.__history):
            if item > 0:
                result += "added funds: " + str(item) + "\n"
            else:
                result += "withdrew funds: " + str(item) + "\n"
        return result

    def transfer(self, amount, other_person: 'BankAccount'):
        self.withraw(amount)
        other_person.add_funds(amount)
