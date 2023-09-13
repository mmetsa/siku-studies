users_file = open("files/sample-6.xml", "r")

# read() tagastab kõik, mis failis kirjas on.
print(users_file.read())

# See ei prindi midagi, sest fail on juba loetud
# print(users_file.read())

# readline() loeb ühe rea
#print(users_file.readline())
#print(users_file.readline())

# readlines() loeb kõik read ja paneb iga rea eraldi listi
# print(users_file.readlines())


users_file.close()
