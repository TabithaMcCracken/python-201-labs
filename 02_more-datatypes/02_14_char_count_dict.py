# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

user_input = input("Please enter a word: ")
user_input = user_input.lower()

final_dict = dict()

for val in user_input: # Loop through every value in the users input
    if val in final_dict: # Adds 1 to the key if it's already in the dictionary
        print(f"This value is in dictionary already")
        final_dict[val] += 1
    else: # Adds the key and value (of 1) if it is not already in the dictionary
        final_dict[val] = 1

print(final_dict)