#Duck typing = Another way to achieve polymorphism besides Inheritance
#               Object must have a minimum necessary attributes/methods
#             = If it looks like a duck and quacks like a duck, it is a duck.


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False
#    def horn(self): # Takto nebude fungovat
    def speak(self):
        print("HONK!")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak() #Have every animal do a speak method
    print(animal.alive) #Have every animal do a alive method


