'''Požadavky:

Vytvořte menu:
Menu bude reprezentováno slovníkem (dict), kde klíčem bude název položky (např. "káva", "čaj") a hodnotou bude cena položky (např. 2.50 CZK).
Menu by mělo obsahovat alespoň 8 různých položek.
Zobrazení menu:
Na začátku programu zobrazte uživateli přehledné menu s názvy položek a jejich cenami.

Výběr položek:
Umožněte uživateli vybírat položky z menu.
Pokud uživatel zadá název položky, která není v menu, upozorněte ho na chybu a zeptejte se znovu.
Uživatel může přidávat více položek do košíku.
Pokud uživatel zadá q, ukončete výběr a přejděte k zobrazení obsahu košíku.

Zobrazení košíku:
Po ukončení výběru vypište seznam všech vybraných položek.
Spočítejte a zobrazte celkovou cenu objednávky.

Bonusové požadavky (volitelné):
Přidejte možnost odebrání položky z košíku před dokončením objednávky.
Umožněte uživateli zadat počet kusů každé položky (např. 2 kávy, 1 čaj).
Přidejte funkci pro zobrazení aktuálního stavu košíku během výběru.
'''

cafe_menu = {"Čaj": 2.50,
             "Kafe": 3.50,
             "Voda": 4.00,
             "Pivo": 4.50,
             "Kratom": 5.00,
             "Limonáda": 5.50,
             "dortik": 6.00,
             "chips": 4.50}

cart = []
total_price = 0

# Zobrazení menu
print("--------MENU--------")
for key, value in cafe_menu.items():
    print(f"{key:10}: {value:.2f} CZK")
print("--------------------")

while item == "q":
    item = input("Vyber si položku (q pro exit): ").lower()
cart.append(food)

