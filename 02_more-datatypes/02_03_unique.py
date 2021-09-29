# Write code that creates a list of all unique values in a list.
# For example:
#
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
print(list_)
# unique_list = [55, 'hi', 4, 13]

unique_list = []

for value in list_:
    if list_.count(value) < 2: # Counts the # of times value appears in the list
        unique_list.append(value) # Adds unique values to a new list
print(unique_list)