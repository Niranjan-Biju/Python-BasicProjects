def highest_bidder(bid):
    highest_bid=0
    winner=""
    for key in bid:
        if bid[key]>highest_bid:
            highest_bid=bid[key]
            winner=key

    print(f"The winner is {winner} with a bid of ${highest_bid}")      

secret_auction = {}
more_bids="yes"

while more_bids!="no":    
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))

    secret_auction[name]=bid
   
    while True:
        more_bids = input("Are there any more bids?Type 'yes' or 'no':\n").lower()
        if more_bids in ["yes","no"]:
            break
        print("Enter a valid input.\n")
        
    highest_bid=0
    if more_bids=="no":
        highest_bidder(secret_auction)
    else:
        print("\n" *50)
        
