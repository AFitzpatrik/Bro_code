#dictionary = a collection of {key:value} pairs
#             ordered and changeable. No dublicates
#print(dir(capitals))
#print(help(capitals))

capitals = {'USA':'Washington D.C',
              'India':'New Dehli',
              'China':'Bejing',
              "Russia": "Moscow"}
'''
if capitals.get('Japan'):
    print("That capital does exist")
else:
    print("That capital does not exist")
'''



#capitals.get('USA')) - Vypíše hodnotu dle klíče, když value není, vypíše "None"
#capitals.update({"Germany": "Berlin"}) - Přidá klíč + hodnotu do dictionary, může i updatnout současný pár
#capitals.update({"USA": "Detroit"}) - Updatne hodnotu u klíče USA na Detroit
#capitals.pop("USA") - Odstraní celá pár z dictionary
#capital.popitem() - Odstraní poslední item z dictioanry
#capitals.clear() - Odstarní vše v dictionary
#capitals.keys() - vráti klíče z dictionary
#capitals.values() - vrátí values z dictionary
#capitals.items() - Funkce  u slovníku vrací všechny klíče i jejich hodnoty jako dvojice

'''
for key, value in capitals.items():
    print(key, value)
'''

'''
for key in capitals.keys():
    print(key)
'''

