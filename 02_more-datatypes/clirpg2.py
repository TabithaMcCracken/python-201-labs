# Save the user input options you allow e.g. in a set that you can check against when your user makes a choice.
# Create an inventory for your player, where they can add and remove items.
# Players should be able to collect items they find in rooms and add them to their inventory.
# If they lose a fight against the dragon, then they should lose their inventory items.
# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. 
# This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.


player_name = str(input("Please enter your name: \n"))
print(
    f"Welcome, {player_name}! Enjoy the game, we hope you make it out alive! \n")


end_game = False
sword = False
doors_entered = set()
weapons = {"your ninja skills"}

while end_game == False:
    # Present them with a choice between three doors.
    door_choice = str(input(
        "You are in a dark hallway, there are 3 doors in front of you. Would you "
        "like to go through the left door, the center door, the right door? \n"))
    door_choice = door_choice.lower()

    # Tells them which door they chose
    if "left" in door_choice or "right" in door_choice or "center" in door_choice:
        print(f"You have selected the {door_choice} door.")
    
    # Left room 
    if door_choice == "left":  # If they choose the left door, they'll see an empty room.
        # Checks to see if they have entered this room before and alerts the player
        if "left" in doors_entered:
            print("You have entered this room before")

        # Asks if they want to enter the room
        enter_empty = str(
            input("The room appears to be empty. \nWould you like to enter it? \n"))
        enter_empty = enter_empty.lower()
        
        # Determines if they already have a sword and asks if they want if they don't already have it
        if enter_empty == "yes" and "sword" not in weapons:  # enters the room and doesn't have the sword
            doors_entered.add("left") # Adds this room to the list of rooms they have visited
            get_sword = str(input(
                "You have decided to enter the room. As you look around you see a sword. \nWould you like to take it? \n"))
            get_sword = get_sword.lower()

            if get_sword == "yes":  # gets the sword
                weapons.add("sword")
                print("You've got the sword! You head back out of the room.")
            elif get_sword == "no":  # doesn't get the sword
                print("You didn't take the sword.")
            else: 
                print("Next time, please enter 'yes' or 'no'. ")
        elif enter_empty == "yes" and "sword" in weapons:  # enters the room, but already has the sword
            print("You have decided to enter the room. The room is empty.")
            leave_sword = str(input(
                "You already took the sword. Would you like to put it back? \n"))
            leave_sword = leave_sword.lower()
            if leave_sword == "yes":
                weapons.remove("sword")
            elif leave_sword == "no":
                print("You kept your sword! Good choice, you might need it later!")
            else:
                print("Next time, please enter 'yes' or 'no'.")

        else:
            print("You did not enter the room.")

    # Right room
    elif door_choice == "right":
        # Checks to see if they have entered this room before and alerts the player
        if doors_entered == "right":
            print("You have entered this room before.")

        enter_right = str(input(
            "There is a large dragon in the room. Would you like to enter the room? \n"))
        enter_right = enter_right.lower()
        if enter_right == "yes":
            doors_entered.add("right") # Adds this room to the list of rooms they have visited
            fight_dragon = str(input(
                "You have entered the room with the dragon. Would like to fight the dragon? \n"))
            fight_dragon = fight_dragon.lower()
            if fight_dragon == "yes":  # player must fight the dragon to end the game
                end_game = True  # breaks the while loop
                if len(weapons) >=1:  # allows them to win if they have the sword
                    print(
                        f"You had a weapon, fought the dragon, and won! Congratulations {player_name}!")
                else:  # allows them to loose since they don't have the sword
                    print(
                        f"I'm sorry {player_name}! You didn't have enough weapons, so you were eaten by the dragon! You loose!")
            if fight_dragon == "no":  # if the player chooses not to fight the dragon
                print("You have left the room.")
        if enter_right == "no":
            end_game = False

    # Center Room
    elif door_choice == "center":
        # Checks to see if they have entered this room before and alerts the player
        if doors_entered == "center":
            print("You have entered this door before.")

        # Asks if they want to enter the room.
        enter_center = str(input(
            "You have decided to enter the room, but it is actually a court yard. Would you like to enter? \n"))
        enter_center = enter_center.lower()
        # If they choose the center door, its a courtyard with a shield in it.
        if enter_center == "yes" and "shield" not in weapons:
                get_shield = input(
                    "There is a shield leaning up against the fountain. Would you like to take it?\n")
                get_shield = get_shield.lower()
                if get_shield == "yes":
                    weapons.add("shield")
                    print("You now have the shield!")
                elif get_shield == "no":
                    print("You did not take the shield")
        elif enter_center == "yes" and "shield" in weapons:
            print("The courtyard is empty, you already took the shield.")
            leave_shield = str(input(
                "You already have the shield, would you like to leave it next to the fountain? \n"))
            leave_shield = leave_shield.lower()

            if leave_shield == "yes":
                weapons.remove("shield")
            elif leave_shield == "no":
                print("Good choice! You might need it!")
            else:
                print("Next time please enter 'yes' or 'no'")

        else:
            print("You did not enter the courtyard.")
    
    # Not 'center', 'left' or 'right'
    else:
        # if user doesn't put left or right as an answer
        print("Please answer with 'left' or 'right' or 'center':")
