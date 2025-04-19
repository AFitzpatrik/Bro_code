# Hangman game
import random

words = ("apple", "orange", "banana", "coconut", "pineapple")
random.choice(words)
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

'''
for line in hangman_art[6]: #Check how the man is looking
    print(line)
'''


def display_man(wrong_guesses):
    # Display hangman art based on number of wrong guesses
    print("**************")
    for line in hangman_art[wrong_guesses]:  # wrong_guesses is number, display art corresponding with that.
        print(line)
    print("**************")


def display_hint(hint):
    # Display hint, after guess. Flip empty _ to a letter, if guess correctly, display "INCORRECT" if not.
    print(" ".join(hint)) #Add "SPACE" to every element in hint list


def display_answer(answer):
    # Display correct answer once the game is won/lost
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)  # Multiply "_" by the length of the answer variable.
    wrong_guesses = 0  # Count wrong guesses
    guessed_letters = set()  # Create an empty set to store guessed letters
    is_running = True  # While the game is running, keep running the game

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        #display_answer(answer) #Uncomment to display the answer
        guess = input("Enter a letter: ").lower()  # Make input lower case


if __name__ == "__main__":
    main()