import random

choice = input("Do you want to play a game of blackjack? Type 'yes or 'no'. ").lower()

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_hand = random.sample(cards,k=2)
user_score = sum(user_hand)
print(f"Your cards: {user_hand}, current score = {user_score}")
dealer_hand = random.sample(cards,k=2)
print(f"Computer's first card: {dealer_hand[0]}")

if user_score==21:
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: [{dealer_hand}], final score: {dealer_hand}")
    print("You win with a blackjack!!!")



while user_score<21:
    choice = input("Type 'yes' to get another card, or type 'no' to pass. ").lower()
    if choice=="yes":
        user_hand.append(random.choice(cards))
        user_score += sum(user_hand)
    elif choice=="no":
        dealer_score = sum(dealer_hand)
        while dealer_score<17:
            dealer_hand.append(random.choice(cards))
            dealer_score += sum(dealer_hand)
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            






