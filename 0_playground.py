# Definice správného hesla
heslo = "tajneheslo"

# Smyčka na 3 pokusy
for pokus in range(3):
    heslo_input = input("Zadejte heslo: ")  # Uživatelské zadání hesla

    if heslo_input != heslo:  # Kontrola správnosti hesla
        print(f"Špatné heslo, zadej znovu. Pokus {pokus + 1} z 3")

        # Upozornění na poslední pokus
        if pokus == 1:  # Pokud je právě druhý pokus
            print("Pozor, máte poslední pokus!")
    else:  # Heslo je správné
        print("Heslo je správné! Přístup povolen.")
        break  # Ukončení smyčky
else:  # Pokud smyčka doběhne bez přerušení (heslo bylo 3x špatně)
    print("Příliš mnoho pokusů. Přístup zablokován.")