#if = Do some code only IF some condition is true
# Else do someting else


#1 Exercise - person wants to sign up for a credit card = needs to be 18

'''
age = int(input("How old are you? "))

if age >= 100:
    print("you are way too old")
elif age >= 18:
    print("You can get a credit card")
elif age <= 0:
    print("you havent been born yet")
elif age >= 100:
    print("you are way too old")
else:
    print("You are too young for that")
'''

#2 Exercise - Food

'''
response = input("Do you want to order food? (yes/no) ")
if response == "yes":
    response = (input("Ok, what do you want?"))
    print(f"ok, ill order {response}. ")

else:
    print("ok, lets not order food.")
'''

#3 Exercise - Names

'''
name = input("What is your name? ")

if name == "":
    print("You didnt enter anything.")
else:
    print(f"Hello {name}. ")
'''

#4 Exercise - For sale

for_sale = False

if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")
