import random
from Hangman_art import stages,logo
from Hangman_word import word_list

print(logo)
word = random.choice(word_list)
print(word)
placeholder = ["_"] * len(word)
print("".join(placeholder))
lives=6

letter_guess =""
while "_" in placeholder and lives>0:
    letter_guess=input("\nEnter 1 alphabet: ").lower()
    if len(letter_guess)!=1 or not letter_guess.isalpha():
        print("Enter a valid input")
        continue
    if letter_guess in placeholder:
        print("You have already guessed this letter! Try another letter.")
    if letter_guess in word:
        for index,letter in enumerate(word):
            if letter==letter_guess:
                placeholder[index]=letter_guess
        print("".join(placeholder))
    else:
        lives-=1
        print(letter_guess + " is not in the word. You lose a life")
        print(f"Lives remaining = {lives}")
        print("".join(placeholder))

    print(stages[lives])    

if lives!=0 and "_" not in placeholder:
    print("***********YOU WIN***********")
if lives==0:
    print("**********YOU LOSE**********") 
    print("The correct word is " + word.upper()) 
    
