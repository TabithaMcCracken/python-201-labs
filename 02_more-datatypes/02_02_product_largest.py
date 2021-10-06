# Take in 10 numbers from the user. Place the numbers in a list.
# You can also use the provided random `randlist` list
# to simulate user input.
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist
print(randlist)

highest_num = randlist[0] # Sets first number as the highest number

for num in randlist: # Iterates over all the nums in the list
    if num>highest_num:
        highest_num = num # Replaces the highest num if num is higher

print(highest_num)



# float()