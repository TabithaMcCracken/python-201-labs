# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.

simple_generator = (i**3 for i in range(1,10))
print(simple_generator)
for i in simple_generator:
    print(i)