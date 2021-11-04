# Write a script called typechecker.py where you add your type-hinted greet() function.
# Add some example calls to the greet() function that take other data types than strings as their input.
# Run the file normally and confirm that everything works fine
# Now run the file with mypy and confirm that you get similar error messages as the ones shown above.
# Fix the errors by changing the inputs to your function calls, then confirm that 
# checking your script with mypy now passes all tests.

# def greet(greeting: str, name: str):
#     """Generates a greeting."""
#     sentence = f"{greeting}, {name}! How are you?"
#     return sentence

# full_sentence = greet("Howdy", 78)
# print(full_sentence)

my_list = ["apple", "banana", "orange"]
obj1 = enumerate(my_list)
print(obj1)