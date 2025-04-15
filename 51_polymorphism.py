#Polymorphism = greek word that means to "have many forms or faces"
#           POLY = MANY
#           MORPH = FORM

#           TWO WAYS TO ACHIEVE POLYMORPHISM
#           1. Inheritance = An object could be treated of the same type as its parent clas
#           2. Duck typing = object must have necessary attributes/methods

from abc import ABC, abstractmethod


class Shape:
    def area(self):

@abstractmethod
class Circle(Shape):
    pass

class Square(Shape):
    pass

class Triangle(Shape):
    pass


shapes = [Circle(), Square(), Triangle()] #objekty v listu



