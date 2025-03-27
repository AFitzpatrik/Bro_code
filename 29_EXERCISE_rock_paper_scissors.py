import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
running = True

while running:
    player = None
    computer = random.choice(options)

    player = input("Enter a choice: ")  # pokud player variable is not found in choice tuple
    while player not in options:
        print("invalid choice")
        player = input("Enter a choice: ")

    print(f"Player: {player}.")
    print(f"Computer: {computer}.")

    if player == computer:
        print("Its a tie!")

    elif "player" == "rock" and "computer" == "scissors":
        print("You won!")

    elif player == "paper" and "computer" == "rock":
        print("You won!")

    elif player == "scissors" and "computer" == "paper":
        print("You won!")

    else:
        print("You lost!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if not play_again == "y":
        running = False
print("thank you for playing!")