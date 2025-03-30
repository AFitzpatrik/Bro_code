def favorite_food(food):
    print(f"Your favorite food is {food}")
print(__name__)

def main():
    print("This is script 1")
    favorite_food("pizza")
    print("Goodbye")


if __name__ == "__main__":
    main()





'''
if __name__ == "__main__":
    print("Run Directly")
    print(__name__)

else:
    print("Run from import")
'''


# Kód v bloku `if __name__ == "__main__":` se vykoná POUZE tehdy, když spustíš soubor přímo (nikoli při jeho importu).