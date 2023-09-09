import random
import time

numbers = []
for number in range(10_000_000):
    numbers.append(number)
random.shuffle(numbers)

number_count = 0
start_time = time.time()
for number in numbers:
    if number == 1:
        print(number_count)
    else:
        number_count += 1
end_time = time.time()
print(end_time - start_time)