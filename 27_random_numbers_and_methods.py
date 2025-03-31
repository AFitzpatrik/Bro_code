import random #Random module
#random.random() #random module | #random method


#print(help(random)) - Nápověda ke commandům k modulu random

#                   METODY              #
#random.randint(1, 6) - random(název modulu) randint (random_int, celé číslo)(1, 6) od 1 do 6. Vyprintuje random číslo od 1 do 6
#random.random() - vrací náhodný float s desetinnou čárkou mezi <0.0, 1.0
#random.choice() - vybere random choice z listu např.
#random.shuffle() - random zamíchá položky v seznamu
'''
number = random.randint(1, 6)
print(number)
'''

'''#Lze napsat i skrz proměnné
low = 1 #nejnižší hodnota
high = 100 #nejvyšší hodnota
#number = random.randint(low, high)
number = random.random()
print(number)
'''

'''
options = ("rock", "paper", "scissors")
option = random.choice(options) #proměnná option = random.choice(volba) vyber random volbu z (options)
print(option)
'''


'''
cards = ["2", "3", "4","5","6","7","8","9","10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
'''

