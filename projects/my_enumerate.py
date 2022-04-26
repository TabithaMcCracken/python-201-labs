# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

# Get name to use as iterable
name = input(str("What is your name?"))

# Function to loop through iterable
def my_enumerate(word):
      index = 0 # Should I define index inside or outside of the function?
      for letter in word:
            print(index, letter)
            index += 1

# Call the function
my_enumerate(name)