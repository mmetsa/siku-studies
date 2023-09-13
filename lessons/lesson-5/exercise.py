# Küsi kasutajalt mitu rida juttu ta tahab.
# Prindi nii mitu rida juttu failis sample-1.txt

# Küsin kasutjalt
# Saan arvu
# võtan selle jutu, panen listi
# prindin selle arvu ridu listist ?

story_file = open("files/sample-1.txt", "r")

story_lines = int(input("Mitu rida juttu tahad? "))

lines = story_file.readlines()
lines_true = []

for line in lines:
    if len(line) != 1:
        lines_true.append(line)

for i in range(story_lines):
     print(lines_true[i])