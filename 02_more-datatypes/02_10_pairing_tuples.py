# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print("Here is our random list: ")
print(randlist)

# Write your code below here

# Sort the numbers
number_list = sorted(randlist)
print("Here is our list sorted: ")
print(number_list)

# Adds 0 to the end if the length of the list is odd
if len(number_list)%2 != 0:
    number_list.append(0)
print("Here is our adjusted list if the list had an odd number of numbers: ")
print(number_list)

# Store the numbers in tuples of 2 in a new list
counter = 0
final_list = []
list_length = len(number_list)

list_range = range(0, list_length ,2)
for i in list_range:
    list_slice = number_list [i:i+1] + number_list [i+1:i+2]
    print(list_slice)
    final_list.append(list_slice) 

print(final_list)



# I googled some other solutions for this, this one works, so I am trying to figure out 
# exactly how it works :-)
# Using a function
int = 1
def pairs(int, n): # Passes in int and n (number of items in each tuple)
    for i in range(0, len(int), n): # len(int) is going to give us the length of numbers in the list
        # Will iterate through from the first index (0) to the last by 'n' steps)
        yield int[i:i + n] # Returns i to 
        # What is the difference between yield and return? I'm guessing yield doesn't stop the loop?
        # This appends down below when we run the function ?

n = 2 # The number of items we want in each tuple
x = list(pairs(number_list, n)) # Makes a list of the tuples
print("Here is what it looks like with a function: ")
print(x)











# Creating tuples from a list (Adding the letter "D" to each letter)

# lst = ['A', 'B', 'C']
# lst2= [(x, 'D') for x in lst]
# print(lst2)

