unit = input("Type C or F: ")
temperature = float(input("Type temperature: " ))

if unit == "C":
    result = (9*temperature)/5 + 32
    print(f" Your temperature from Celsius to Fahrenheit is {result:.1f}")

elif unit == "F":
    result = (temperature - 32) * 5 / 9
    print(f"Your temperature from Fahrenheit to Celsius is {result:.1f}")

else:
    print(f"{unit} Unit is invalid")