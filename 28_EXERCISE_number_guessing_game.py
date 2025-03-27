
#Python number guessing game
import random

lowest_num = 1
highest_num = 100
secret_number = random.randint(lowest_num, highest_num)
guesses = 0 #počet hádání
is_running = True

print("Welcome to Python number guessing game!")
print(f"Enter a number between {lowest_num} and {highest_num}: ")

while is_running:
   guess = input("Try to guess a number: ")

   if guess.isdigit():
    guess =  int(guess)
    guesses += 1

    if guess > highest_num or guess < 1:
        print(f"This number is out of {lowest_num} - {highest_num} range!")
        print(f"Enter a number between {lowest_num} and {highest_num}: ")

    elif guess < secret_number:
        print("Too low, try again!")
    elif guess > secret_number:
        print("Too high, try again!")
    else:
        print(f"Correct number! You've won with {guesses} tries!")
        is_running = False

else:
    print("This is not a number! Try again: ")
    print(f"Enter a number between {lowest_num} and {highest_num}: ")