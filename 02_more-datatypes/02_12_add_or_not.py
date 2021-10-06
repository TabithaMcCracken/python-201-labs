# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# input hasn't been added and deduce a point.
# If the user gets loses 5 points, quite the program.
# They wil if they manage to create a set that has more than 10 items.

counter = 5
num_list = set()

while counter > 0:
    print("Please enter a number: ")
    user_input = input()
    print(f"You entered: {user_input}")

    try:
        val = int(user_input) # Checks for an integer
    except ValueError:
        print("This is not an integer.")
    else:
        
        if val in num_list:
            print("This value is already in the list.")
            counter -= 1
        else:
            num_list.add(val) # Adds users input to the set
            print(f"This is the new list: {num_list}")
    
    
    

    