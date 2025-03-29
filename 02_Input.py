# input() = A function that prompts the user to enter data
# Returns the entered data as a string


#Basic Info
'''
name = input("what is your name? ")
age = int(input("how old are you? "))
age =+ 25 #Can be written as age = age + 25
print(f"Hello, your name is {name}, {age} years old.")
'''

# Exercise 1 Rectange Area calculation
# A = w/l

'''
lenght = float(input("Enter your lenght: "))
width = float(input("Enter your width: "))
area = lenght * width
print(f"Your rectangle area is {area}cm^2 ")
'''

# Exercise 2 Shopping Cart Program

item = input("What do you want to buy? ")
price = float(input("How much is it? "))
quantity = int(input("How many do you want? "))
total = price * quantity

print(f"You have bought {quantity}x {item}/s")
print(f"Your total is {total}CZK")