# Loe sisse hinnete fail
# Prindi välja iga õpilase keskmine hinne

grades_file = open("files/hinded.txt", "r")
grades_list = grades_file.readlines()
for student in grades_list:
    student_data = student.split(",")
    correct_data = []
    for i in range(len(student_data)):
        if i == len(student_data) - 1:
            correct_data.append(student_data[i][0])
        else:
            correct_data.append(student_data[i])
    grades_sum = 0
    grades_amount = 0
    for i in range(1,len(correct_data)):
        grades_sum += int(correct_data[i])
        grades_amount += 1
    grades_avg = grades_sum / grades_amount
    print(correct_data[0] + ": " + str(grades_avg))
