funkce = input("Zvol funkci: * , / , +, - ")
funkce_seznam = ["*", "/", "+", "-"]

while funkce not in funkce_seznam:
    funkce = input("Nesprávný symbol, zadej znovu: * , / , +, - ")

cislo_jedna = float(input("zadej první číslo: "))
cislo_dva = float(input("zadej druhé číslo: "))

if funkce == "*":
    kraceni = cislo_jedna*cislo_dva
    print(f"{cislo_jedna}*{cislo_dva} se rovná {kraceni}")

elif funkce == "+":
    scitani = cislo_jedna+cislo_dva
    print(f"{cislo_jedna}+{cislo_dva} se rovná {scitani}")

elif funkce == "-":
    odcitani = cislo_jedna-cislo_dva
    print(f"{cislo_jedna}-{cislo_dva} se rovná {odcitani}")

elif funkce == "/":
    while cislo_dva == 0:
        print("nemůžeš dělit nulou!")
        cislo_dva = float(input("zadej druhé číslo znovu: "))
    deleni = cislo_jedna/cislo_dva
    print(f"{cislo_jedna}/{cislo_dva} se rovná {deleni:.3f}")   #:-.3f tři desetina cisla



'''while funkce == "/":
    if cislo_dva == 0:
        print("nemůžeš dělit nulou!")
        cislo_dva = float(input("zadej druhé číslo znovu: "))
        deleni = cislo_jedna/cislo_dva
    else:
        deleni = cislo_jedna/cislo_dva
        print(f"{cislo_jedna}/{cislo_dva} se rovná {deleni}")
        break
'''