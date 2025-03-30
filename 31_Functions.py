# functions - block of reusable code
#             place () after the function name to invoke it

#NÁZVY#
#def happy - definuji funkci, happy je NÁZEV FUNKCE
#happy(name, age) - v závorce jsou parametry. Name a age jsou PARAMETRY
#happy("Bob", 20) - tímto zavolám již hotovou funkci, s argumenty které chci v závorce. V závorce jsou ARGUMENTY Bob a 20


'''
def add(a, b):  #jmeno funkce(parametr1,parametr2)
    return a + b #obsah funkce, co funkce provede po zavolání

add(1, 2) #add - zavolání funkce, 1 = argument, 2 = argument
print(add(1, 2)) #vyprintování funkce
'''








'''
def happy_bday():                                   #definuji funkci, vše pod ní se vypíše, pokud níže napíšu jméno funkce - happy_bday()
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

happy_bday()
happy_bday()
happy_bday()
happy_bday()
'''



#můžeme poslat data directly do funkce skrz argument happy_bday("ARGUMENT_JE_V_TETO_ZAVORCE")
'''
def happy_bday(name, age): # V závorce je kolik je funkce schopná vzít argument, každý argument který bere musí mít název
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}!")
    print()

happy_bday("Franciska", 20)
happy_bday("Bob", 30)
happy_bday("Mary", 50)
'''

# INVOICE EXERCISE #

'''
def display_invoice(username, amount, due_date):
    print(f"Hello {username}, this is your invoice for ${amount} due on {due_date}:")

display_invoice("Patrik", "50,000", "2.11.1996")
display_invoice("Filip", "40,000", "11.14.1999")
'''

#return = statement used to end a function and send a result bact to the caller

'''
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))
'''


'''
def multiply(num1, num2):
  return num1 * num2   #return num * num 2 a poté ho stornem ve proměnné x

x = multiply(6, 8)

print(x)
'''


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last



full_name = create_name("patrik", "franců")
print(full_name)