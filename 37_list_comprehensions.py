# List comprehension = a concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]
                     #[výraz for hodnota in iterovatelný_objekt if podmínka]

#TRADIČNÍ ZÁPIS FOR CYKLUS
'''
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)
'''

#ZÁPIS SKRZ LIST COMPREHENSION
'''
doubles = [x * 2 for x in range(1, 11)]
print(doubles)
'''

'''

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]
print(doubles)
print(triples)
print(squares)

'''


#STRINGS
'''
fruits = ["apple", "banana", "cherry"]
fruits = [fruit.upper() for fruit in fruits]
'''

'''
fruits = ["apple", "banana", "cherry"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)
'''
#EXERCISE
'''
numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_list = [num for num in numbers if num >= 0]
negative_list = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0] # % vydělí 2 a vrátí zbytek
odd_numbers = [num for num in numbers if num % 2 ==1]
print(positive_list)
print(negative_list)
print(even_numbers)
print(odd_numbers)
'''

#EXERCISE
grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)

