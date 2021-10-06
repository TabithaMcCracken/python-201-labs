# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

counter = 1
exp_dict = dict()

while counter <= 10:
    exp_dict[counter] = counter*counter
    counter += 1

print(f"Here is the whole dictionary: {exp_dict}")