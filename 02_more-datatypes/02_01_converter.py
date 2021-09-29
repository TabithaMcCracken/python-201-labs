# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"
for element in string:
    print(element) # The string prints each character on a new line

tup = (string,) #Once I added the ',' it becomes a tuple, otherwise its a string
print(tup) # The tuple prints with parentheses and a comma
    
for element in tup:
    print(element) # The tuple prints each character on the same line


