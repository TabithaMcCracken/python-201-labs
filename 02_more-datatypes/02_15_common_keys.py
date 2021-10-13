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
dict_4 = dict()

print(f"Here is the first dictionary: {dict_1} ")
print(f"Here is the second dictionary: {dict_2} ")

# Copies first list into a new empty list
for key, value in dict_1.items():
    dict_3[key] = value

# Goes through each key,value pair in the second list
for key, value in dict_2.items():
    if key in dict_3: # Adds the value if the key is already in the list
        dict_3[key] += value
    else: # Adds the key and value to the list if its not there
        dict_3[key] = value
print(f"Here is the first combined dictionary: {dict_3}")

# My first attempt
# Looking for keys that are the same
for key, value in dict_1.items(): # Loops through each key/value in dict_1
    for key_2, value_2 in dict_2.items(): # Loops through each key/value in dict_2
        if key == key_2: # Looks for keys that are the same
            dict_4[key] = value + value_2 # Adds the values together in the new dictionary 

# Looking for keys that are not the same
for key, value in dict_1.items():
    for key_2, value_2 in dict_2.items():
        if key not in dict_4.keys():
            dict_4[key] = value # Adds the key/value to the new dictionary from dict_1
        elif key_2 not in dict_4.keys():
            dict_4[key_2] = value_2 # Adds the key/value to the new dictionary from dict_2
print(f"Here is the second combined dictionary: {dict_4} ")