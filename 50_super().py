# super() = Function usd in a child class to call methods from parent class (superclass)
#   Allows you to extend the functionality of the inherited method

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) #tímto zavoláme init constructor z parent classy
        self.radius = radius

    def describe(self):
        print(f"It is a circle withe and area of {3.14 * self.radius * self.radius} cm^2")
        #zde nyní chceme jak describe od parent classy, tak i od child classy. Použijeme tedy super na parent classu
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f"It is a square with an area of {self.width * self. width} cm^2")
        #zde nyní chceme jak describe od parent classy, tak i od child classy. Použijeme tedy super na parent classu
        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height /2} cm^2")
        #zde nyní chceme jak describe od parent classy, tak i od child classy. Použijeme tedy super na parent classu
        super().describe()




circle = Circle("red", True, 5)
square = Square("blue", False, 6)
triangle = Triangle("green", True, 7, 8)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius} cm")
print("")
print(square.color)
print(square.is_filled)
print(f"{square.width} cm")
print("")
triangle.color = "yellow"
print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width} cm")
print(f"{triangle.height} cm")



square.describe()
triangle.describe()
circle.describe()

#V tomto příkladu má mají classy spoločné color,is filled ale pak mají jiné proměnné
#Abychom nemuseli psát color a is_filled do každé classy, použijeme super()

#pokud jsou dvě metohdy (v tomto případe describe) stejné, tak se zavolá ta z child classy, ne z parent classy(method overriding)