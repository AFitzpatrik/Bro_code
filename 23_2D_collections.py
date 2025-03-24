
'''
fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]


groceries = [fruits, vegetables, meats]

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()
'''
#end=" ": Díky němu jsou potraviny z jedné kolekce vypsány na stejném řádku oddělené mezerami.
# Prázdný print(): Zajišťuje oddělení kolekcí přidáním prázdného řádku mezi nimi pro lepší čitelnost výstupu.

#        NUMPAD       #

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()