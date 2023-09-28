class Student:
    def __init__(self):
        self.student_id = None
        self.first_name = None
        self.last_name = None
        self.date_of_birth = None
        self.grade = None

    def __repr__(self):
        return "ID: " + str(self.student_id) + ", eesnimi: " + self.first_name + ", perekonnanimi: " + self.last_name