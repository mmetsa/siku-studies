# Ava fail "input.txt" mis asub kaustas "files/exercise-3"
# Loe, mitu sõna selles failis on.
# Kirjuta see arv samasse kausta faili "output.txt"

exercise = open("files/exercise-3/input.txt", "r")
word_count = 0
lines = exercise.readlines()
exercise.close()

for item in lines:
    words = item.split(" ")
    print(words)
    word_count += len(words)
    print(word_count)

new_file = open("files/exercise-3/output.txt", "w")
new_file.write(str(word_count))
new_file.close()