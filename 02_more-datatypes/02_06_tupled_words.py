# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]
input_string = input("Please enter a string of words: ")

user_list = input_string.split()
print(user_list)

empty_tuple = tuple()
new_list = list()

for word in user_list:
    empty_tuple = tuple(word)
    new_list.append(empty_tuple)
    
print(new_list)