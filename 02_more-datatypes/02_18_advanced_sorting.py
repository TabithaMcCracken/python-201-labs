# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!

# First option using a function
input_dict = {
    "item1": 5, 
    "item2": 6, 
    "item3": 1
}

def take_second(elem):
    return elem[1]

sorted_list = sorted(input_dict.items(), key=take_second)

print("Here is the original list: ", input_dict)
print("Sorted list: ", sorted_list) # Does this come out as a list?

# Another option I found
input_dict2 = {
    "item4": 17, 
    "item5": 31, 
    "item6": 99
}

sort_orders = sorted(input_dict2.items(), key=lambda x:x[1])
for i in sort_orders:
    print(i[0],i[1])

# A third option using a list comprehension
input_dict3 = {
    "item7": 45, 
    "item8": 134, 
    "item9": 1
}

[print(key,value) for (key,value) in sorted(input_dict3.items(), key=lambda x:x[1])]