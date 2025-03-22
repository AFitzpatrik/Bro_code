#for loop =execude a b lock of code a fixed of times.
#               You can iterate over a range, string, sequence, etc.
# lepší v případech kdy nemá loop jet do nekonečna, pouze určitý počet pokusů
# https://www.youtube.com/watch?v=dHANJ4l6fwA

#Nejčastěji se for loop používá s funkcí range(), která generuje posloupnost čísel.


#for i in range(5):  # i postupně nabývá hodnot 0, 1, 2, 3, 4   - (5) značí že se for loop provede 5x, tzn. vyprintuje 0 1 2 3 4
#   print(i)




'''
for x in range(1, 21): # loop control variable, iteration variable = x, variable represent each listed item one at the time
    if x == 13:
        continue #skip over ideration
    else:
        print(x)
'''


'''
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)
'''

'''
for x in reversed(range(1, 11, 2)):   #(ZAČÁTEK - KONEC - STEP)
    print(x)
'''


'''
heslo = "cigan"
for pokus in range(3): #loop na 3 pokusy
    heslo_input = input("Enter your password: ")

    if heslo_input != heslo:
        print(f"Špatné heslo, zadej znovu. Pokus {pokus + 1} z 3")

        if pokus == 1:
            print("POZOR MÁTE POSLEDNÍ POKUS!")
    else:
        print("Přihlašuji")
        break
else:
    print("Přístup odepřen!")
'''


'''
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:    # for every FRUIT in FRUITS
    print(fruit) 
'''
