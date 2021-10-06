# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

flat_list = []

for sublist in starter_list: # Cycles through each sublist
    for item in sublist: # Cycles through each item
     flat_list.append(item) # Adds each item to a new list
print(flat_list)

# Second Option
starter_list2 = [[1,2, 3,4], [5,6], [7,8,9]]
flat_list2 = [item for sublist in starter_list2 for item in sublist] 
print(flat_list2)

# Third Option for multi-level lists
# Use a function to iterate over the elements, calling the function again if the
# element is a list, once it reaches the first level list items, then append it 
# to a new list
data = [1, [2,3, [4,5]], 6, [[7], [8, 9]]]
flat_list3 = []
# Function
def flatten_list(data):
    for element in data:
        if type(element) == list:
            flatten_list(element)
        else:
            flat_list3.append(element)

flatten_list(data)
print(flat_list3)