# Loe andmed failist "files/exercise-5/input.txt"
# Selles failis on paroolid
# Igal paroolil peab olema vähemalt:
# * 7 tähemärki
#
# Lisa sobivad paroolid faili "files/exercise-5/oiged.txt"
# Lisa mittesobivad paroolid faili "files/exercise-5/valed.txt"

passwords = open("files/exercise-5/input.txt", "r")
correct_passwords = []
incorrect_passwords = []
for item in passwords:
    if len(item) >= 7:
        correct_passwords.append(item)
    else:
        incorrect_passwords.append(item)
passwords.close()

oiged = open("files/exercise-5/oiged.txt", "w")
for item in correct_passwords:
    oiged.write(item)
oiged.close()

valed = open("files/exercise-5/valed.txt", "w")
for item in incorrect_passwords:
    valed.write(item)
valed.close()