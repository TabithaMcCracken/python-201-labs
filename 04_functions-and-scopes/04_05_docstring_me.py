# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """Converst km to miles

    Args:
        km (float): kilometers

    Returns:
        float: miles
    """       
    miles = km * 0.6
    return miles

miles = km_to_miles(30.6)
print(miles)

print(km_to_miles.__doc__)

help(km_to_miles)