class Ticket:
    def __init__(self):
        self.price = 0
        self.name = ""
        self.is_periodic = False

    def __repr__(self):
        return self.name + ": " + str(self.price) + "€"