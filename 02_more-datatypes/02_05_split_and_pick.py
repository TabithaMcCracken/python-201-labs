# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

input_string = input("Please enter a string of words: \n")

user_list = input_string.split() # Convert string into list
print(f"Here is what you entered: {user_list}")

counter = 0
num = user_list [0] # Sets num to the first word in the list

for word in user_list:
    frequency = user_list.count(word) # Counts the frequency of the word in the list
    if(frequency > counter):
        counter = frequency
        num = word # Changes the num to the more frequent word if greater than previous

print(num)