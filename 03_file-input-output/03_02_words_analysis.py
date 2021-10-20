# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

from pathlib import Path
file_path = Path("/Users/tabithamccracken/Documents/codingnomads/python-201/03_file-input-output/words.txt")

# Make a list of the words in the txt file
with open (file_path, "r") as file:
    word_list = file.read().split()

# Find and print the length of the list
list_length = len(word_list)
print(f"The length of the list is: {list_length}")

# Find the longest word length and make a list to put it in
longest_words = []
long_word_length = len(max(word_list, key=len))


# Find the shortest word length and make a list to put it in
shortest_words = []
short_word_length = len(min(word_list, key=len))

# Check for a tie in word length, both short and long
for word in word_list:
    if len(word) == long_word_length:
        longest_words.append(word)
    elif len(word) == short_word_length:
        shortest_words.append(word)
print(f"The longest words are: {longest_words}")
print(f"The shortest words are: {shortest_words}")