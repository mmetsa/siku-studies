class House:
    area = 0
    color = "WHITE"
    stories = 1
    year_built = 2020

    #def __init__(self):

    def print_house_data(self):
        print("Total area:", self.area, "color:", self.color, "stories:", self.stories, "year built:", self.year_built)

    def renovate(self, new_color):
        if self.year_built >= 2000:
            raise Exception("House is too new to renovate.")
        self.color = new_color