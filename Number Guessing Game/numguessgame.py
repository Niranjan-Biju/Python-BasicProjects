from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_ans(user_guess,answer,remaining_turn):
    """Checks answer against user guess. Returns the number of turns remaining."""
    if user_guess>answer:
        print("Too high")
    elif user_guess<answer:
        print("Too low")
    else:
        print(f"You got it! The correct answer is {answer}")
    return remaining_turn-1

def set_difficulty():
    """Used to set the user difficulty to "easy" or "hard"."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty=="easy":
        return EASY_LEVEL_TURNS
    elif difficulty=="hard":
        return HARD_LEVEL_TURNS

def game():
    """Welcome to the Number Guessing Game."""
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    number = randint(1,100)
    turns = set_difficulty()
    guess = 0
    while number!=guess:
        if turns!=0:
            print(f"You have {turns} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            turns = check_ans(guess, number, turns)
        else:
            print("You ran out of guesses. You lose.")
            break


game()

