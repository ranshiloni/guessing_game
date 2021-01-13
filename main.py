import random
from os import system

def game():
    print("Welcome to the Numbers Guessing Game! 🎲")
    print("I'm thinking of a number between 1 and 100... 🤔")

    level = input("Choose a difficulty. Type 'easy' or 'hard' 💪")
    tries = 0
    if level == "easy":
        tries = 10
    else:
        tries = 5

    number = random.randint(1,100)
    isWon = False
    for i in range(1, tries-1):
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.\n Guess again.")
            print(f"You have {tries - i} attempts remaining to guess the number")
        elif guess < number:
            print("Too low.\n Guess again.")
            print(f"You have {tries - i} attempts remaining to guess the number")
        else:
            print("That's RIGHT!")
            isWon = True
            break
    if isWon:
        if input("Play another game? y or n: ") == 'y':
            _ = system('clear')
            game()
        else:
            print("Ok, bye..")
    else:
        if input("Sorry, you are out of guesses. Play another game? y or n: ") == 'y':
            _ = system('clear')
            game()
        else:
            print("Ok, bye..")

game()


