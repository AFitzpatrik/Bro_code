#Shopping cart program
foods = []
prices = []
total = 0

while True:
    food = input("Enter food: ")
    if food == "q":
        break

    else:
        foods.append(food)
print(foods)