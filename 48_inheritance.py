#Inheritance = Allow a  class to inherit attributes and methods from another class
#              Help with code reusability and extensibility
#              class Child(Parent):

#poznámka k attributům a metodám(attributes and methods):
#když mám def_něco mimo class, jedná se o funkci. Pokud mám def_něco unvnitř classy, je to metoda.

'''
class Father:
    height = 182
    color = "pink"

class Son(Father): #zde dědí z class father proměnné height a color
    pass
'''


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEK!")


dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

dog.speak()
cat.speak()
mouse.speak()



#Summary
#Classy mohou od sebe dědit, hodí se to abychom nemuseli psát víc kódu, když se metody, atributy opakují.















#čas - 6:53:06