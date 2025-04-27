# exception = Aa event that interrupts the flow of a program
#             (ZeroDivisionError, ValueError, TypeError, FileNotFoundError, IndexError...)
#             1. try,  2. except,  3.finally

'''
try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
except Exception: #This will catch any other exceptions that are not specifically handled above, shouldn't be used solo.
    print("An unexpected error occurred!")
finally:
    print("Do some cleanup here.")
'''

while True:
    try:
        input_uzivatele = input("Enter a number, press X to close the program: ")

        if input_uzivatele.upper() == "X":
            print("Program closed.")
            break

        number = int(input_uzivatele)
        print(1 / number)

    except ZeroDivisionError:
        print("You cannot divide by zero!")
    except ValueError:
        print("Please enter a valid number!")
    except Exception:  # This will catch any other exceptions that are not specifically handled above, shouldn't be used solo.
        print("An unexpected error occurred!")
    finally:
        print("Do some cleanup here.")

'''
- **Blok `finally` garantuje, že kód uvnitř něj se vždy vykoná, a to bez ohledu na výskyt výjimky.**
- **Použití `finally` je nutné, když se pracuje s prostředky, které je potřeba uzavřít nebo správně uvolnit.**
- Pokud se aplikace obejde bez čisticích operací, blok `finally` není potřeba.
'''