#Class methods = Allow operations related to the class itself
# #             Take (cls) as the first parameter, which represents the class itself.fightnight challange
# cls = class



class Student:

    count = 0  # Class variable to keep track of the number of students

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 # Increment the count of students whenever a new student is created

