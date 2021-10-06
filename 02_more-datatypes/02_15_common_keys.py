# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
dict_3 = dict()

print(f"Here is the first dictionary: {dict_1} ")
print(f"Here is the second dictionary: {dict_2} ")

# Looking for keys that are the same
for i, j in dict_1.items(): # Loops through each key/value in dict_1
    for k, l in dict_2.items(): # Loops through each key/value in dict_2
        if i == k: # Looks for keys that are the same
            dict_3[i] = j + l # Adds the values together in the new dictionary 

# Looking for keys that are not the same
for i, j in dict_1.items():
    for k, l in dict_2.items():
        if i not in dict_3.keys():
            dict_3[i] = j # Adds the key/value to the new dictionary from dict_1
        elif k  not in dict_3.keys():
            dict_3[k] = l # Adds the key/value to the new dictionary from dict_2
print(f"Here is the combined dictionary: {dict_3} ")

# Can this be done a shorter way?