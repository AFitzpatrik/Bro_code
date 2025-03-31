# EXERCISE BANKING PROGRAM

def show_balance(balance):
    print("******************")
    print(f"Your balance is {balance:.2f} Kč")
    print("******************")


def deposit():
    amount = float(input("Choose a amount to deposit: "))
    if amount <= 0:
        #Pokud nastane že je input <= 0, if statement vrátí 0,
        # a bude se počítat jako kdyby uživatel zadal 0, nemusím teda ošetřeovat jesště zvlášt negativní hodnoty
        print("Deposit cant be negative!")
        return 0

    else:
        print(f"You deposited {amount}.")
        return amount


def withdraw(balance):
    amount = float(input("Choose a amount to withdraw: "))

    if amount > balance:
        print("Not enough funds")
        return 0

    elif amount < 0:
        print("You cant wihdraw negative")
        return 0

    else:
        print(f"Withdrawing {amount} KČ.")
        return amount


#VARIABLES

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*******************")
        print("  Banking program  ")
        print("*******************")
        print("#1 - Show balance")
        print("#2 - Deposit")
        print("#3 - Withdraw")
        print("#4 - Exit")
        choice = (input("Choose a option: "))

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            print("Closing program...")
            is_running = False
        else:
            print("Invalid option!")

    print("Thank you for using our banking program!")  # Zpráva co se vytiskne po konci loopu

if __name__ == "__main__":
    main()