# Python compound interest calculator.
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter your principle amount: "))
    if principle <= 0:
        print("Principle cant be 0 or less!")

print(f"Your principle amount is {principle}")

while rate <= 0:
    rate = float(input("Enter your rate per year amount: "))
    if rate <= 0:
        print("Rate cant be 0 or less!")

while time <= 0:
    time = int(input("Enter your time of coumpounding: "))
    if time <= 0:
        print("time cant be 0 or less!")


result = principle * pow((1+rate / 100), time) # ALTERNATIVNÍ ZÁPIS, FUNGUJE TAKY : result = principle * (1 + (rate / 100 )) **
# result = pow(4, 3) #umocenění prvního čísla na to druhé, v tom případě "4 na 3 (čtyři na třetí)"

print(f"Your entered principle amount is {principle}")
print(f"Your entered rate amount is {rate}")
print(f"Your entered time of coumpounding is {rate}")
print(f"Your result is {result}")


