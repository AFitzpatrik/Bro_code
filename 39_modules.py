#module = a file containing code y ou want to include in your program
#         use 'import' to include a module (built-in or your own)
#         useful to break up a large program to reusable separate files
# Například při projektu HRA v SDA, byl program rozdělen do více filů

#print(help("modules")) - vypíše list modulů ve standartní knihovne pythonu
#print(help("math"))

import math #nainportuju modul math a mám nyní přístup k proměnným a funkcím tohoto modulu
#print(math.pi)

#import math as cigan #modul se dá takto přejmenovat a používat tak alternativní jmeno modulu
#print(cigan.pi)

'''
from math import pi
print(pi)
'''

import example_module

result = example_module.pi
result = example_module.square(3)
result = example_module.cube(3)
result = example_module.circumference(3)
result = example_module.area(3)
print(result)