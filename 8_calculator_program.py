operator = input("Choose an operator: /, *, +, - ")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))


if operator == "/":
    vysledek = number1 / number2
    print(f"{vysledek:.3f}")

elif operator == "*":
    vysledek = number1 * number2
    print(f"{vysledek:.3f}")

elif operator == "+":
    vysledek = number1 + number2
    print(f"{vysledek:.3f}")

elif operator == "-":
    vysledek = number1 - number2
    print(f"{vysledek:.3f}")

else:
    print(f"{operator} is invalid operator")