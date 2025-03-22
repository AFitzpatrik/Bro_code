#nested loop = a loop withing another loop (outer, inner)
#           outer loop:
#               inner loop:




'''
list = [1,2,3,4,5]
for x in range(5):  # Tento cyklus zopakuje celý blok 5x
    for i in list:  # Původní cyklus
        print(i)  # Výpis každého prvku seznamu
'''

'''
names = ["Kelly","Michelle", "Beyoncé"]

for n in names:
    print(f"{n}, can you handle this?")

print("I dont think they can handle this")
'''


'''
for x in range (1, 10):
    print(x, end="") #end napíše vše na jeden řádek v konzole, můžu použít i třeba "-", to mi napíše - za kazdé  číslo
'''

'''
for x in range(3):  #countery v nested loops musí být rozdilne, nesmí být stejné
    for y in range (1, 10):
        print(y, end="")
    print() # vloží nový řádek po každé iteraci cyklu
'''

řada = int(input("Enter the number of řad:"))
sloupec = int(input("Enter the number of sloupců:"))
symbol = input("Enter the symbol:")

for x in range(řada):
    for y in range (sloupec):
        print(symbol, end="")
    print()

'''
#řada = 4
#sloupec = 6
#symbol = *

for x in range(4): #step 2, step 1 se provede dohromady 4x
    for y in range (6):  #step 1 * se vyprintuje 6x
        print("*", end="")
    print() 
''''''







