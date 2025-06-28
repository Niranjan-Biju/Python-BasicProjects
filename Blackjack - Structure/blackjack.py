import random

def first_draw(play):
    while play=="yes":  
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

        user_hand = random.sample(cards,k=2)
        user_score = sum(user_hand)
        print(f"Your cards: {user_hand}, current score = {user_score}")
        dealer_hand = random.sample(cards,k=2)
        dealer_score = dealer_hand[0]
        print(f"Computer's first card: {dealer_hand[0]}")

        if user_score==21:
            final_hand(user_hand,user_score,dealer_hand,dealer_score)
        
        while user_score<21:
            choice = input("Type 'yes' to get another card, or type 'no' to pass. ").lower()
            if choice=="yes":
                user_hand.append(random.choice(cards))
                user_score += sum(user_hand)
                if 11 in user_hand:
                    checksum = sum(user_hand)-11
                    if checksum>10:
                        user_hand = new_user_hand(user_hand)
                    elif checksum==10:
                        final_hand(user_hand,user_score,dealer_hand,dealer_score)
                                     
            # elif choice=="no":
            #     dealer_score = sum(dealer_hand)
            # while dealer_score<17:
            #     dealer_hand.append(random.choice(cards))
            #     dealer_score += sum(dealer_hand)
            #     print(f"Your final hand: {user_hand}, final score: {user_score}")
def new_user_hand(userhand):
    
    
  
            
def final_hand(userhand,userscore,dealerhand,dealerscore):
    print(f"Your final hand: {userhand}, final score: {userscore}")
    print(f"Computer's final hand: [{dealerhand}], final score: {dealerscore}")
    print("You win with a blackjack!!!")

choice = input("Do you want to play a game of blackjack? Type 'yes or 'no'. ").lower()
first_draw(choice)

# while user_score<21:
#      choice = input("Type 'yes' to get another card, or type 'no' to pass. ").lower()
#      if choice=="yes":
#          user_hand.append(random.choice(cards))
#          user_score += sum(user_hand)
#      elif choice=="no":
#         dealer_score = sum(dealer_hand)
#         while dealer_score<17:
#             dealer_hand.append(random.choice(cards))
#             dealer_score += sum(dealer_hand)
#             print(f"Your final hand: {user_hand}, final score: {user_score}")
            






