seznam = {"Anna": "pizza", "Petr": "špagety", "Jana": "salát", "Karel": "hamburger"}

for x in seznam:
    if x == "pizza":
        print(f"{x} má rád pizza.")

    else:
        print(f"{x} má rád něco jiného")

print(f" V seznamu je {len(seznam)} jmen")
