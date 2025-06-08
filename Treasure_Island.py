

print("Welcome to Treasure Island.")
print("Find the One Piece!")

direction=input("You are at a crossroad, where do you want to go? Type \"left\" or \"right\".\n").lower()
if direction=="right":
    print("Game Over.")
elif direction=="left":
    travel=input("You've come to a deserted island with no trees. Would you wait for the ship or swim fot it?" 
                "Type \"wait\" or \"swim\".\n").lower()
    if travel=="wait":
        print("You died of hunger.")
    elif travel=="swim":
        chest_color=input("No fish at sea. You have safely reached the Treasure Island. What chest do you choose - Red, Blue or Yellow?\n").lower()
        if chest_color=="red":
            print("Dead. No redemption for you.")
        elif chest_color=="blue":
            print("Locked!")
        else:
            print("THE ONE PIECE IS REAL!")
    else:
        print("Wrong input!")
else:
    print("Wrong input")
