# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

from pathlib import Path

file_in_path = Path("/Users/tabithamccracken/Documents/codingnomads/python-201/03_file-input-output/words.txt")

# Make a list of the words
with open(file_in_path, "r") as file_in:
    word_list = file_in.read().split()
print(f"The first word in the list is: {word_list[0]}")
print(f"The last word in the list is: {word_list[-1]}")

# Reverse the list
word_list.reverse()

print("I have reversed the list.")
print(f"The first word in the list is now: {word_list[0]}")
print(f"The last word in the list is now: {word_list[-1]}")
