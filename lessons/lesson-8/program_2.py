#küsi kasutajalt tema andmed ja salvesta andmed student.csv faili
user_id = input("Sisesta oma ID: ")
user_first_name = input("Sisesta oma eesnimi: ")
user_last_name = input("Sisesta oma perekonnanimi: ")
user_birth = input("Sisesta oma sünnikuupäev (aaaa-kk-pp): ")
user_grade = input("Sisesta oma klass (1-12): ")

user_data = open("files/students.csv", "a")
user_data.write(user_id + ",")
user_data.write(user_first_name + ",")
user_data.write(user_last_name + ",")
user_data.write(user_birth + ",")
user_data.write(user_grade + "\n")