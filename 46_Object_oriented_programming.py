# object = A "bundle" of related attributes (variables) and methods (functions)
#       Ex. phone, cup, book

'''
Je to soubor proměnných a funcí. např telefon:
phone_number = 606255937 # Toto je proměnná (variable, attribute)
def call_phone(): #toto je funkce, kterou může objekt vykonat
'''

#       You need a "class" to create many objects
#class = (blueprint) used to design the structure and layout of an object


from class_for_OOP_46 import Car #takto importujeme object CAR z filu class_for_OOP_46.py

car_1 = Car("Mustang", 2024, "red", False)  #toto jsou objekty
car_2 = Car("Corvette", 2025, "blue", True)
car_3 = Car("Charger", 2026, "yellow", True)

print(car_1.model)  #. atribute acces operator  print(car_1.model) vyprintuje model car1
print(car_1.year)
print(car_1.color)
print(car_1.for_sale)

'''
print(car_2.model)  
print(car_2.year)
print(car_2.color)
print(car_2.for_sale)
'''
car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()
car_1.describe()

