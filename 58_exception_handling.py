# exception = Aa event that interrupts the flow of a program
#             (ZeroDivisionError, ValueError, TypeError, FileNotFoundError, IndexError...)
#             1. try,  2. except,  3.finally


try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")

