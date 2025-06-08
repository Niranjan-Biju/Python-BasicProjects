import random
rock = '''
                       888      
                       888      
                       888      
888d888 .d88b.  .d8888b888  888 
888P"  d88""88bd88P"   888 .88P 
888    888  888888     888888K  
888    Y88..88PY88b.   888 "88b 
888     "Y88P"  "Y8888P888  888 
'''

paper = '''
88888b.  8888b. 88888b.  .d88b. 888d888 
888 "88b    "88b888 "88bd8P  Y8b888P"   
888  888.d888888888  88888888888888     
888 d88P888  888888 d88PY8b.    888     
88888P" "Y88888888888P"  "Y8888 888     
888             888                     
888             888                     
888             888   
'''

scissors = '''
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' 
'''

image_list = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))
if user_choice>=0 and user_choice<=2:
    print(image_list[user_choice])
else:
    print("Invalid input. You lost!")
    exit()

computer_choice = random.randint(0,2)
print(image_list[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win.")
elif computer_choice == 0 and user_choice == 2:
    print("You lose.")
elif user_choice>computer_choice:
    print("You win.")
elif computer_choice>user_choice:
    print("You lose.")
else:
    print("Draw.")

