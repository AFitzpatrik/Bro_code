#result = len() - délka stringu
#result = name.find(" ") # najdu znak ve stringu, vráti pozici prvního nalezeného znaku(first occurance)
#               Pokud nemůže python najít, vytiskne -1
#result = name.rfind(" ") #reverse find, najde poslední znak (firt occurance zezadu)
#               Pokud nemůže python najít, vytiskne -1
#name = name.capitalize() - da velké písmeno na první místo stringu
#name = name.upper() - přepíše input na UPPER CASE
#name = name.lower() - přepíše input na lower ase
#result = name.isdigit() - vráti bool, bud FALSE nebo TRUE. Pokud jsou v name pouze čísla =TRUE, kombinace čísla-písmen = FALSE, Písmena = FALSE
#result = name.isalpha() - vráti bool, bud FALSE nebo TRUE. Pokud jsou v name pouze písmena =TRUE, kombinace čísla-písmen = FALSE, čísla = FALSE
#result = phone_number.count("-") - vypočítá kolikrát je znak ve stringu
#phone_number = phone_number.replace("-", "") - replacne první znak druhým, v tomto případě - vymění za prázdný string
#print(help(str)) - vypíše list string funkcí


'''name = input("enter you full name: ")
result = name.isalpha()
print(result)
'''


'''
phone_number = input("zadej číslo #")
result = len(phone_number)
print(result)
'''

'''
phone_number = input("zadej číslo #: ")
result = phone_number.count("-")
print(result)
'''

'''phone_number = input("zadej číslo: ")
phone_number = phone_number.replace("-", "") 
print(phone_number)
'''


#Exercise! Validate user input
#Username is no more than 12characters
#Username must not contain spaces
#username must not contain digits

'''
user_name = input("enter your username: ")
if len(user_name) > 12:
    print("too long")

elif user_name.isdigit() == True:
    print("username cant contain digits!")

elif " " in user_name:
    print("username cant contain spaces!")

'''
#           !!!!alternativní zápis skrz .find()!!!!
#if user_name.find(" ") != -1:
#    print("username cant contain spaces!")
#    '''

'''
else:
    print("good username")
'''
















#result = "username too long" if len(user_name) > 12 else "too long username"
#print(result)







