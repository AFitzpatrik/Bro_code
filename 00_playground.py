def print_power(**kwargs):
    for key, value in kwargs.items():
        print(f"Auto {key} má výkon {value}")


print_power(skoda=130, mazda=200, bmw=250)