import random
#SLOT MACHINE EXERCISE 🍒🍉🍋🔔⭐




def spin_row():
    symbols = ("🍒", "🍉", "🍋", "🔔", "⭐")
    return [random.choice(symbols) for _ in range(3)] #vygeneruje 3 random symboly a vrátí list?



def print_row(row): #Funkce print_row nemá přístup k proměnným mimo svůj vlastní obsah, musí být tedy přidán do argumentu
    print("*********")
    print("|".join(row)) #using join method vezmeme iterable row(list) a ke každému elementu v listu přidáme mezeru
    print("*********")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    else:
        return 0 #toto je mimo if statement, znamená to tedy, že pokud nenastane varianta if row 0 == row 1 == row 2, hráč nedostane nic protože nemá match



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

        row = spin_row() #Funkce spin_row() zavolá list, proto před ní dáme row = přiradíme jí tuto proměnnou
        print("Spinning...\n") #\n = ně line
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won {payout} Kč")
        else:
            print("Sorry, you lost this round!")
        balance += payout

        play_again = input("Play again? (Y/N): ").upper()
        if play_again != "Y":
            break


if __name__ == "__main__":
    main()
    #d

