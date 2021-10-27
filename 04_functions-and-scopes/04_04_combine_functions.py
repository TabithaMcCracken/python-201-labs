# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

user_tuple = ("Hello", "Waheed")

def write_letter(text):
    greeting = greet(*user_tuple)
    letter = f"{greeting}, {text} See you soon!"
    return letter

complete_letter = write_letter("Thank you for reaching out. I can't wait to see you.")
print(complete_letter)