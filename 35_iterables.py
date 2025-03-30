# Iterables = An object/colelction that can return its elemets one at a time,
#             allowing it to be iterated over in a loop
# you can iterable LIST, TUPLE, SETS, STRINGS, DICTIONARIES
'''
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
'''
#LIST
'''
numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number)
'''
#TUPLE
'''
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)
'''

#SET
'''
fruits = {"apple", "banana", "cherry"} #you cant reverse sets
for fruit in fruits:
    print(fruit)
'''

#STRINGS
'''
name = "Bro Code"
for character in name:
    print(character, end=" ")
'''

#DICTIONARIES
my_dictionary = {"A": 1, "B": 2, "C": 3}
for value in my_dictionary.values(): #získá values z dictionary
    print(value)

my_dictionary = {"A": 1, "B": 2, "C": 3}
for key, value in my_dictionary.items(): #získá key i value z dictionary
    print(key, value)


