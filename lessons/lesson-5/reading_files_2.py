# Ava kasutajad.txt fail ja loe esimesed 3 rida

users = open("files/kasutajad.txt", "r")
for i in range(3):
    print(users.readline())
