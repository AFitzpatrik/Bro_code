import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []   #ukládá hodnotu od každé kostky kterou hodíme (pokud hodíme 4, uloží 4 hodnoty [3, 3, 4, 6]
total = 0   #bude sčítat hodnoty z dice jako int
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):  #"Udělám toto tolikrát kolik je hodnota v num_of_dice. takže když hodím 3 kostky, řádek append se provede 3x a vygeneruje random číslo od 1 do 6 a přidá k dice proměnné.
    dice.append(random.randint(1, 6))

'''
PRINT VERTICALLY
for die in range(num_of_dice):
for line in dice_art.get(dice[die]):
print(line)
'''

#PRINT HORIZONTALLY
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")