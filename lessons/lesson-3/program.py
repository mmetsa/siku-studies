from grade import Grade

grades = []
for number in range(1, 6):
    grade = Grade(number, "Signe")
    grades.append(grade)

for number in range(1, 6):
    grade = Grade(number, "Maiko")
    grades.append(grade)

bad_grades = []
for grade in grades:
    if grade.get_value() == 1 or grade.get_value() == 2:
        bad_grades.append(grade)

print(bad_grades)
