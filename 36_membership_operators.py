#Membership operatros = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#   1. in (is VARIABLE in LIST)
#   2. not in (is VARIABLE not in LIST)





'''
#VARIANTA S WHILE CYKLEM

word = "APPLE"
letter = input("Enter a letter: ").upper()

while True:
    if letter in word: #Bolean - Vratí bud True nebo False
        print(f"A letter: '{letter}' is in secret word")
        break
    else:
        print (f"A letter: {letter} is not in secret word")
        letter = input("Enter a letter: ")
'''

'''
#VARIANTA BEZ WHILE CYKLU A POUŽITÍ NOT IN PRVNÍ
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")
'''

#VARIANTA BEZ CYKLU SET
'''
students = {"Filip", "Marek", "Jakub", "Pavel"}
student = input("Enter a student name: ").capitalize()

if student in students:
    print(f"{student} is in the list")

else:
    print(f"{student} is not in the list. Try again")
'''

'''
#VARIANTA S CYKLEM
students = {"Filip", "Marek", "Jakub", "Pavel"}
student = input("Enter a student name: ").capitalize()

while True:
    if student in students:
        print(f"{student} is in the list")
        break
    else:
        print(f"{student} is not in the list. Try again")
        student = input("Enter a student name: ").capitalize()
'''

'''
#VARIANTA S NOT IN BEZ CYKLU
students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")
'''

#VARIANTA BEZ CYKLU DICTIONARY
'''
grades = {"Sandy": "A",
          "Patrick": "B",
          "Spongebob": "C"}
student = input("Choose a student: ").capitalize()

if student in grades:
    print(f"{student} has a grade of {grades[student]}")
else:
    print(f"{student} is not in the dictionary")
'''

#VARIANTA S CYKLEM DICTIONARY
'''
grades = {"Sandy": "A",
          "Patrick": "B",
          "Spongebob": "C"}
student = input("Choose a student: ").capitalize()

while True:
    if student in grades:
        print(f"{student} has a grade of {grades[student]}")
        break

    else:
        print(f"{student} is not in the dictionary")
        student = input("Choose a student again: ").capitalize()
'''

#VARAIANTA BEZ CYKLU STRING
'''
email = "Brocode@gmail.com"

if "@" in email and "." in email:    #AND čekuje více než jednu věc, obě musí být pravda
    print("Valid email")

else:
    print("Not valid email")
'''
