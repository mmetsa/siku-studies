# Ava fail "files/exercise-4/input.txt"
# Loe selle faili tekst
# Tee uus fail "files/exercise-4/output.txt" ja kirjuta sinna
# kõik sisse loetud read vastupidises järjekorras

# Näide
# input.txt:
# Tere
# Olen
# Maiko
#
# output.txt
# Maiko
# Olen
# Tere

text = open("files/exercise-4/input.txt", "r")
text_list = text.readlines()
text.close()

new_file = open("files/exercise-4/output.txt", "w")
text_list.reverse()

for item in text_list:
    new_file.write(item)
    print(item)
new_file.close()
