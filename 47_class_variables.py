#class variables = Shared among all instances(objects) of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

'''
class Car:
    wheels = 4 # <- Class variable (Definovaná mimo constructor init)

    def __init__(self, model, year):
        self.model = model    # <- Instance variables (definovány v constructor init)
        self.year = year
'''


class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30) #objecty
student2 = Student("Patrick", 35)
student3 = Student("Peter", 32)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(Student.class_year) #šlo by i student1.class_year ale je good practice napsat to přes celou class, protože je to class variable a funguje na celou classu kterou děláme, v tomto případě Student
print(Student.num_students)


print(Student.class_year)
print(Student.num_students)
print(student1.name)
print(student2.name)