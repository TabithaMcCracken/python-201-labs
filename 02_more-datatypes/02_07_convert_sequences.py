# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

new_tuple = tuple(string)
print(new_tuple)

new_list = list(new_tuple)
print(new_list)

counter = 0

for char in new_list:
    if char == 'c':
        new_list[counter] = 'k'
    counter += 1
print(new_list)

new_tuple = tuple(new_list) # Convert back to tuple
print(new_tuple)

