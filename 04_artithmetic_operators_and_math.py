import math
friends = 10

# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# reminder = friends % 3  #dividing friends into group of 3 / při zjieštění EVEN ČÍSLA = bude u tohoto operatoru vždy 0

# % MODULO operátor = Vrací zbytek po dělení dvou čísel
#výsledek bude 1 jelikož -> 3 rozdělíme na 1 a 1,  zbyde tedy 1 (10%3 -> 10 děleno 3 je 3, zbytek 1
modulo = 3
vysledek = 3 % 2
print(vysledek)

x = 3.14
y = 4
z = 5

# result = round(x)  #zaokrouhlení(round)
# result = abs(y) #absolute value  - distance away from zero as a whole number
# result = pow(4, 3) #umocenění prvního čísla na to druhé, v tom případě "4 na 3 (čtyři na třetí)"
# result = max(x, y, z) - vypíše nejvyšší
#result = min(x, y, z) - vypíše nejnižší

#print(math.pi)
#print(math.e)
#result = math.sqrt(x) #druhá odmocnina
#result = math.ceil(x) #vždy zaokrouhlí nahoru
#result = math.floor(x) #vždy zaokrouhlí dolu
#print(result)



#1 Exercise = vypočítej obvod kruhu
'''
radius = float(input("Enter radius: "))
area = 2* math.pi * radius
print(f"obvod is:{area}")
'''

#2 Exercise = Obsah kruhu
'''
radius = float(input("Enter radius: "))
area = math.pi * pow(radius, 2)

print(f"Obsah je: {round(area, 2)}cm")
'''

#3 Exercise = pravý úhel
'''
a = float(input("Enter a: "))
b = float(input("Enter b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(c)
'''