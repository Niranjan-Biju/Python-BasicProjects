import random

def adjust_ace(hand):
    while 11 in hand and sum(hand)>21:
        hand.remove(11)
        hand.append(1)
    return hand

def first_draw():
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] * 4
        deck = cards.copy()

        user_hand = random.sample(cards,k=2)
        for card in user_hand: deck.remove(card)
        user_hand = adjust_ace(user_hand)
        user_score = sum(user_hand)

        dealer_hand = random.sample(cards,k=2)
        for card in dealer_hand: deck.remove(card)
        dealer_hand = adjust_ace(dealer_hand)
        dealer_score = sum(dealer_hand)

        print(f"Your cards: {user_hand}, current score = {user_score}")
        print(f"Computer's first card: {dealer_hand[0]}")

        if user_score==21:
            final_hand(user_hand,user_score,dealer_hand,dealer_score)
        
        while user_score<21:
            hit_or_stand = input("Type 'yes' to hit, or type 'no' to stand. ").lower()
            if hit_or_stand=="yes":
                new_card = random.choice(deck)
                deck.remove(new_card)
                user_hand.append(new_card)
                user_hand = adjust_ace(user_hand)
                user_score = sum(user_hand)
                print(f"Your cards: {user_hand}, current score = {user_score}")
            elif hit_or_stand=="no":
                if dealer_score<17:
                    dealer_hand = stand(dealer_hand,deck,dealer_score)                        
                    dealer_score = sum(dealer_hand)
            
        final_hand(user_hand,user_score,dealer_hand,dealer_score)
    
def stand(dealerhand,deck,dealerscore): 
    while dealerscore<17:
        card = random.choice(deck)
        deck.remove(card)
        dealerhand.append(card)
        dealerhand=adjust_ace(dealerhand)
        dealerscore=sum(dealerhand)
    return dealerhand

def get_result(userscore, dealerscore):
    if userscore > 21:
        return "You went over. You lose 😭"
    if dealerscore > 21:
        return "Dealer went over. You win 😎"
    if userscore > dealerscore:
        return "You win 😁"
    if userscore < dealerscore:
        return "You lose 😢"
    return "It's a draw 😐"

def final_hand(userhand,userscore,dealerhand,dealerscore):
    print(f"Your final hand: {userhand}, final score: {userscore}")
    print(f"Computer's final hand: {dealerhand}, final score: {dealerscore}")
    print(get_result(userscore, dealerscore))

def main():
    while True:
        play = input("Do you want to play a game of blackjack? Type 'yes' or 'no': ").lower()
        if play == "yes":
            first_draw()
        else:
            print("Thanks for playing! 👋")
            break

main()







