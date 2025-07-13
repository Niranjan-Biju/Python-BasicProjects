from art import logo
from art import vs
from game_data import data
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def winner(final_score):
    print("You have guessed every answer correctly.")
    print("You win!!!")
    print(f"Final score: {final_score}")

def compare_score(a,b):    
    if a['follower_count']>b['follower_count']:
        return 'a'
    else:
        return 'b'

def hlgame(A,game_data,score):
    
    while game_data:
        print(logo)
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
        print(vs)
        B = random.choice(game_data)
        game_data.remove(B)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
        highest_score = compare_score(A,B)
        
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        while user_guess not in ['a', 'b']:
            user_guess = input("Invalid input. Please type 'A' or 'B': ").lower()

        clear()
        if user_guess == highest_score:
            score += 1
            print("You are correct.")
            print(f"Current score: {score}")
            A=B
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return
    
    
    winner(score)

def main():
    
    score = 0
    options = data.copy()
    choice_1 = random.choice(options)
    options.remove(choice_1)
    hlgame(choice_1,options,score)

main()