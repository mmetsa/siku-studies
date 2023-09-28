from classes.student import Student

#loen failis kõik read
#teen iga rea kohta student objekti
#pane objektid listi
#prindin listi

students_file = open("files/students.csv", "r")
student_list = []

for line in students_file:
    correct_line = line.strip()
    values = correct_line.split(",")
    if values[0].startswith("StudentID"):
        continue

    student = Student()
    student.student_id = int(values[0])
    student.first_name = values[1]
    student.last_name = values[2]
    student.date_of_birth = values[3]
    student.grade = values[4]

    student_list.append(student)

print(student_list)