# Failis "files/exercise-6/input.txt" on komaga eraldatud arvud
# Loe selle faili andmed sisse
# Kui arv jagub seitsmega (jääk on = 0), lisa see faili "files/exercise-6/seitsmega_jaguvad.txt"
# Kui arv ei jagu seitsmega (jääk ei ole = 0), lisa see faili "files/exercise-7/seitsmega_mitte_jaguvad.txt"

numbers = open("files/exercise-6/input.txt", "r")
numbers_text = numbers.readline()
numbers.close()

numbers_list = numbers_text.split(",")
divisible_by_seven = []
not_divisible_by_seven = []
for number in numbers_list:
    if int(number) % 7 == 0:
        divisible_by_seven.append(number)
    else:
        not_divisible_by_seven.append(number)

divisible = open("files/exercise-6/seitsmega_jaguvad.txt", "w")
for number in divisible_by_seven:
    divisible.write(number + ",")
divisible.close()

not_divisible = open("files/exercise-6/seitsmega_mitte_jaguvad.txt", "w")
for number in not_divisible_by_seven:
    not_divisible.write(number + ",")
not_divisible.close()
