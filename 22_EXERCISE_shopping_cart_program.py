foods = []
prices = []
total = 0

while True:
    food = input("Enter food (press q to quit): ")
    if food.lower() == "q":      #food.lower() - input se po zadání převede na malé pismeno
        break
    else:
        foods.append(food)
        price = float(input(f"Enter a price of a {food} CZK: "))
        prices.append(price)


print("----- Your shopping cart -----:")
for food in foods:
    print(food, end= ", ")

for price in prices:
    total = total + price

print()
print(f"Your total is {total} CZK")
