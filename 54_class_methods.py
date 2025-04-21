#Class methods = Allow operations related to the class itself
# #             Take (cls) as the first parameter, which represents the class itself.fightnight challange
# cls = class



class Student:

    count = 0  # Class variable to keep track of the number of students
    total_gpa = 0  # Class variable to keep track of the total GPA

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 # Increment the count of students whenever a new student is created
        Student.total_gpa += gpa

        #INSTANCE METHOD
    def get_info(self):
        return f"Student: {self.name}, GPA: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"


student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)



print(Student.get_count())

