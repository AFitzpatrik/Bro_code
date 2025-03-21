# while loop = execute some code WHILE some coidition remains true
# loop cyklus pojede dokud nekterá z podmínek bude TRUE


'''
name = input("napiš jméno: ")
while name == "":  #while je jmeno = ""
    print("nezadal jsi jméno.")
    name = input("zadej znovu: ") # exit strategy, reprompt znova na input

print(f"hello {name}.")
'''


'''
ge = int(input("Enter your age: "))
while age <= 0:
    print("you have not been born yet: ")
    age = int(input("Enter your age again: "))

print(f"your age is {age}")
'''


"""
food = input("enter the food you like (q for quit): ")
while food == "q":
    print("ukončuji program")
    break
else:
    print(f"your favorite food is {food}")
"""


'''
food = input("enter the food you like (q for quit): ")
while not food == "q": #pokud se food rovna cemukoliv jinemu nez q
    print(f"you like {food} ")
    food = input("enter second food you like")

print("shutting down")
'''

number = int(input("enter number between 1 and 10: "))

while number < 1 or number > 10:
    print("number not valid!")
    numb = int(input("enter number between 1 and 10 again: "))

print(f"valid number {number}")
