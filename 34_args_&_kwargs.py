
#* args = allows you to pass multiple non-key arguments     -> Zabalí argumenty do tuplu ()
#** kwargs = allows you to pass multiple keyword-aruments   - > Zabalí argumenty do dictionary {}
#   *unpacking operator
# 1. positional 2.default 3. keyword 4. ARBITRARY


'''
def add(a, b):  #jmeno funkce(parametr1,parametr2)
    return a + b #obsah funkce, co funkce provede po zavolání

add(1, 2) #add - zavolání funkce, 1 = argument, 2 = argument
print(add(1, 2)) #vyprintování funkce
'''

#V tomto kódu když přidám další argument k volání funkce, funkce již nebude fungovat. add(1, 2, 3)
#Vypíše se TypeError: add() takes 2 positional arguments but 3 were given, v tomto případě použijeme *args


#ARGS!
'''
def add(*args):  #args převede argumenty do tuplu// Jméno parametru může být i jiné, jde tam o "*" takže *numbs např. je ok
    total = 0 #musím si dát variable, kde budem ukládat výpočet
    for arg in args:
        total = total + arg
    return total

print(add(1, 2, 3, 4, 5, 5, 6, 7, 9, 8))
'''

'''
def display_name(*args):
    for arg in args:
        print(arg, end = " ")
display_name("Patrik", "Filip", "Jiří", "David", "Tomáš")
'''

#KWARGS!

'''
def print_adress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_adress(street="123 Fake street",
             apt="100",
             city="Detroit",
             state="MI",
             zip="54321")
'''

# EXERCISE - SHIPPING LABEL
#Moje řešení :1) Vypíše celé jmeno
#             2) Poté vypíše adresu ve stylu STREET : XXXX, V řádcích pod sebou

'''
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    for key, value in kwargs.items():
        print()
        print(f"{key.upper()} : {value}", end="")


shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zip="54321")
'''

#bro code řešení

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")