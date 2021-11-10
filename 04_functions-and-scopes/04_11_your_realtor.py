# Write a function that prints out nicely formatted information about a
# real estate listing. The information can vary for every listing, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

# Not yet completed

intro_info = ("Welcome to this beautiful, one of a kind, 3 bedroom, 3 bathroom, "
    "single family home in Aurora! Upon entry, you are greeted with an open foyer, "
    "a curved staircase, and sleek wood-like flooring! Stop by for a viewing today!")

# Should the dictionary be down where I call the function, or is this ok?
home_stats = {
    'home_type': "Single Family", 
    'year_built': 1996, 
    'square_footage': 2389, 
    'lot_size': 7405
    }

def print_listing (intro, **kwargs):
    print(intro, "\n")
    print(type(kwargs))
#    for key, value in args.iteritems():
#        print(args[key])

print_listing(intro_info, home_stats)





