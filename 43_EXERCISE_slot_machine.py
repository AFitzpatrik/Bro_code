import random
#SLOT MACHINE EXERCISE 🍒🍉🍋🔔⭐




def spin_row():
    symbols = ("🍒", "🍉", "🍋", "🔔", "⭐")
    return [random.choice(symbols) for _ in range(3)]



def print_row():
    pass



def get_payout():
    pass


def main():
    balance = 100

    print("************************")
    print("Welcome to Slot Machine!")
    print("Symbols:🍒 🍉 🍋 🔔 ⭐")
    print("************************")

    while balance > 0: #While je balance víc jak 0, můžem pokračovat ve hře
        print(f"Current balance: {balance} KČ")
        bet = input("How much would you like to bet?: ")
        if not bet.isdigit():
            print("PLEASE ENTER VALID NUMBER!")
            continue

        bet = int(bet)

        if bet > balance:
            print("NOT ENOUGH BALANCE!")
            bet = input("How much would you like to bet?: ")
            continue #Continue přeruší tuto část a vráti se na úplný začátek while cyklu (while balance > 0...) Protože uživatel bude číslo zadávat znovu a je potřeba tedy projet cyklus znovu a zkontrolovat .is digit a až poté jestli je input menší než bet.

        if bet <= 0:
            print("BET MUST BE GREATER THAN 0!")
            continue

        balance -= bet
        row = spin_row() #Funkce spin() zavolá list, proto před ní dáme row = přiradíme jí tuto proměnnou
        print(row)

if __name__ == "__main__":
    main()
    #d

