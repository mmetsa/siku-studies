from classes.zoo import Zoo
from classes.ticket import Ticket
from classes.cage import Cage
from classes.animal import Animal

my_zoo = Zoo()
my_zoo.name = "Loomaaed"
my_zoo.address = "Laagna tee 5"
my_zoo.contact = "59053482"
my_zoo.email = "loomaaed@loomaaed.ee"
my_zoo.prices = []
my_zoo.cages = []

full_ticket = Ticket()
full_ticket.name = "täispilet"
full_ticket.price = 15

child_ticket = Ticket()
child_ticket.name = "lapsepilet"
child_ticket.price = 8

my_zoo.prices.append(full_ticket)
my_zoo.prices.append(child_ticket)

small_cage = Cage()
small_cage.size = 3
small_cage.indoor = True
small_cage.location = "Roomajate maja"
small_cage.description = "Väike puur akvaariumi vastas."
small_cage.last_feeding_timestamp = 1694276180
small_cage.animals = []

big_cage = Cage()
big_cage.size = 2000
big_cage.location = "Õues, värava vastas"
big_cage.description = "Suur, kole jurakas"
big_cage.last_feeding_timestamp = 1694276180 - 60*60
big_cage.animals = []

small_cage_animal = Animal()
small_cage_animal.name = "Juta"
small_cage_animal.type = "Koduhiir"
small_cage_animal.size = 1
small_cage_animal.food_type = "Taimed"

big_cage_animal_1 = Animal()
big_cage_animal_1.name = "Peep"
big_cage_animal_1.type = "Jääkaru"
big_cage_animal_1.size = 100
big_cage_animal_1.food_type = "Liha"

big_cage_animal_2 = Animal()
big_cage_animal_2.name = "Peeter"
big_cage_animal_2.type = "Ninasarvik"
big_cage_animal_2.size = 95
big_cage_animal_2.food_type = "Taimed"

small_cage.animals.append(small_cage_animal)
big_cage.animals.append(big_cage_animal_1)
big_cage.animals.append(big_cage_animal_2)

my_zoo.cages.append(small_cage)
my_zoo.cages.append(big_cage)

print("Tere tulemast loomaaeda", my_zoo.name)
print("Meil on müügil järgnevad piletid:")
for ticket in my_zoo.prices:
    print(ticket)
animal_count = 0
for cage in my_zoo.cages:
    animal_count += len(cage.animals)
print("Meil on loomaaias", animal_count, "looma.")
