#Collection = single "variable" used to store multiple values
# LIST = [] ORDERED AND CHANGEABLE. DUPLICATES OK
# SET = {} UNORDERED AND IMMUTABLE, BUT ADD/REMOVE OK. NO DUPLICATES
# TUPLE = () ORDERED AND UCHANGEABLE. DUPLICATES OK. FASTER

#print(dir(fruits)) Vypíše všechny funkce atd které jde s uvedenou kolekcí provést
#print(help(fruits)) Vypíše popis co každá možná funkce dělá

#                   LIST                #
# fruits = ['apple', 'banana', 'cherry']

#print(help(fruits)) Vypíše popis co každá možná funkce dělá
#print("apple" in fruits) Vyhodí boolean, X in Y hledání v kolekcích
#fruits.append("pineapple) - přidá do listu na konec
#fruits.remove("apple") - odstraní z listu
#fruits.instert(0, pineapple) - přidá na určitou pozici v listu
#fruits.sort() - seřadí podle abecedy
#fruits.reverse - reversne
#fruits.clear() - vyčistit komplet všechno
#fruits.index("apple") - vráti na kterém indexu je apple
#fruits.count("banana") - spočítá kolikrát je v listu

#                   SET                #
#fruits = {'apple', 'orange', 'banana', 'coconut'}
#fruits.add("pineapple")
#fruits.remove("apple")
#fruits.pop() - removne první element, je to random
#fruits.clear() - vymaže se

#                   TUPLE                #
#fruits = ('apple', 'orange', 'banana', 'coconut')
#print(fruits.index("apple"))
#fruits.count("banana")



'''
fruits = ['apple', 'banana', 'cherry']
fruits[0] = "pineapple"
for fruit in fruits:
    print(fruit)
'''

'''
fruits = ['apple', 'banana', 'cherry']
print(fruit)
print(fruit[3]) #indexing
print(fruits[:2]) #slicing
'''


#print(fruit[0])
#for fruit in fruits:
    #print(fruit)