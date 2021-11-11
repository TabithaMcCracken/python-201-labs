# Write a function that prints out nicely formatted information about a
# real estate listing. The information can vary for every listing, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

intro_info = ("Welcome to this beautiful, one of a kind, 3 bedroom, 3 bathroom, "
    "single family home in Aurora! Upon entry, you are greeted with an open foyer, "
    "a curved staircase, and sleek wood-like flooring! Stop by for a viewing today!")

# Should the dictionary be down where I call the function, or is this ok?
home_stats = {
    'Home Type': "Single Family", 
    'Year Built': 1996, 
    'Square Footage': 2389, 
    'Lot Size': 7405
    }

def print_listing (intro, **kwargs):
    print(intro, "\n")
    # print(type(kwargs))
    for key in kwargs:
        print(key, ": ", kwargs[key])

print_listing(intro_info, **home_stats)





