from house import House

my_house = House()
my_house.color = "BLACK"
my_house.year_built = 1960

my_house.print_house_data()

my_house.renovate("GREEN")

my_house.print_house_data()

maikos_house = House()
maikos_house.color = "YELLOW"
maikos_house.stories = 2
maikos_house.area = 140
maikos_house.year_built = 1970

maikos_house.print_house_data()

maikos_house.renovate("PINK")

maikos_house.print_house_data()