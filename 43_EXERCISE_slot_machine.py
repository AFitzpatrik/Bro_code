import random
#SLOT MACHINE EXERCISE 🍒🍉🍋🔔⭐
symbols = ("🍒", "🍉", "🍋", "🔔", "⭐")



def spin_row():
    pass



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
            print("Please enter a valid number.")
            continue



if __name__ == "__main__":
    main()

