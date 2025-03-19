#logical operators = evaluate multiple conditions (or, and, not)
#                   or = at least one condition must be True
#                   and = both must be true
#                   not = inverts the condition (not False,not True)
#




#                           OR
#Když se používá OR musí být aspoň jedna podmínka PRAVDA
#V tomto případě je je vše FALSE jelikož je 25 stupnu (takže není víc jak 35 a mín jak 25 a is_raining je FALSE)

'''
temperature = 25
is_raining = False
if temperature > 35 or temperature < 0 or is_raining: #is_raining je true, aspon jedna z těchto tří věcí musí být pravdivá
    print("Event is canceled! ")
else:
    print("Event is going to happen! ")
'''

#                           AND
#obě podmínky musí být TRUE
#V Tomto případě je 25 teplota a sunny je TRUE. Takže bude print  print("Event is canceled! 😥 ")
'''
temperature = 30 #moje zápisky
is_sunny = True

if temperature >= 28 and is_sunny:
    print("Its hot outside🌡️ ")
elif temperature <= 0 and is_sunny:
    print("Its sunny but cold 🥶")
elif temperature <= 30 and temperature >= 25: # 30 >= temperature >= 25: Alternativní zápis
    print("Its nice day ☺️️")
'''

#Code bro zápisky
''' 
temp = 20 
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside 😡")
    print("It is SUNNY 🌞")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY 🌞")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 🙂")
    print("It is SUNNY 🌞")
'''

#                          NOT
temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside 😡")
    print("It is SUNNY 🌞")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY 🌞")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 🙂")
    print("It is SUNNY 🌞")

elif temp >= 28 and not is_sunny:
    print("It is HOT outside 😡")
    print("It is CLOUDY ☁️")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶") #Koukáme jestli NOT is_sunny, takže když je FALSE podmínka je splněna
    print("It is CLOUDY ☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside 🙂")
    print("It is CLOUDY ☁️")
#takže když je něco TRUE a já dám IF NOT TRUE => musí být false a jestli je FALSE, provede se akce







