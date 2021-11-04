# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread, *toppings):
    sandwich= ""
    sandwich += str(bread) + "\n"
    for item in toppings:
        sandwich += str(item) + "\n"
    sandwich += str(bread)
    return sandwich

sandwich_printout = make_sandwich("white", "lettuce", "tomato", "mayo")
print(sandwich_printout)