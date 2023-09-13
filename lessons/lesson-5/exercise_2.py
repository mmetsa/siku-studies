# Küsi kasutajalt tema isikukood
# Kontrolli, kas sellise isikukoodiga kasutaja on olemas
# Kui on olemas, küsi kasutajalt parool
# Kui pole olemas, prindi "Sellist kasutajat ei eksisteeri"
# Kui parool sisestatakse õige, siis prindi "Edukalt sisse logitud"
# Kui parool sisestatakse vale, siis prindi "Vale parool!"
# Kasutajad on failis kasutajad.txt

users_file = open("files/kasutajad.txt", "r")
users_list = users_file.readlines()
print(users_list)

user_id = input("Sisesta oma isikukood: ")
for user in users_list:
    user_data = user.split(",")
    user_code = user_data[3]
    if user_code == user_id:
        user_pass = input("Sisesta oma parool: ")
        user_passw = user_data[4]
        if user_passw == user_pass + "\n":
            print("Edukalt sisse logitud!")
            exit()
        else:
            print("Vale parool!")
            exit()
print("Sellist kasutajat ei eksisteeri!")