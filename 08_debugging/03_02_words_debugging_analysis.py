# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

from pathlib import Path
file_path = Path("/Users/tabithamccracken/Documents/codingnomads/python-201-copy/03_file-input-output/words.txt")

with open (file_path, "r") as file:
    words_list = file.read().split()    

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
shortest_length = len(min(words_list, key=len))
shortest_word_list = []
longest_length = len(max(words_list, key=len))
longest_word_list = []

for word in words_list:
    if len(word) == shortest_length:
        shortest_word_list.append(word)
    elif len(word) == longest_length:
        longest_word_list.append(word)

print(f"The shortest words are: {shortest_word_list}\n")
print(f"The longest words are: {longest_word_list}\n")

# 3. The total number of words in the file.
length = len(words_list)
print(f"There are {length} words in the list.")