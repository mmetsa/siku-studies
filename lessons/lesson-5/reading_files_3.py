users_file = open("files/sample-8.sql", "r")
users_list = users_file.readlines()
for i in range(2, len(users_list) - 1):
    print(users_list[i])

users_file.close()