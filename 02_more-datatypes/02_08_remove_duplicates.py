# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

# 1. Convert to a different data type
list_ = [1, 2, 3, 4, 3, 4, 5]

unique_list = set(list_) # Changes the type to a set and removes duplicates
print(unique_list)

# 2. Use a loop and a second list to solve it more manually
list2 = [1, 2, 3, 4, 3, 4, 5]
unique_list2 = []

for num in list2:
    if num not in unique_list2: # Adds unique numbers to the new list
        unique_list2.append(num)
print(unique_list2)
