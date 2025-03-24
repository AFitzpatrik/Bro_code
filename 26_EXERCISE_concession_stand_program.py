#Concession stand program


menu = menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []
total = 0

print("---------MENU---------")
for key, values in menu.items():
    print(f"{key:10}: {values:.2f} CZK")
print("----------------------")

while True:
    food = input("Select and item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:   #Když je zadána položka co nemá key, vypíše NONE, tzn když dám input a nebude to NONE, program přidá food do cartu.
        cart.append(food)
print("------Your cart-----")
for food in cart:
    total = total + menu.get(food)
    print(food, end=" ")

print()
print(f"Total: {total:.2f} CZK")