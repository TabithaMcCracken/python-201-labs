# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).


from pathlib import Path

# Create a file path to the txt file
file_path = Path("/Users/tabithamccracken/Documents/codingnomads/python-201/03_file-input-output/words.txt")

# Make a list of the words in the txt file
with open (file_path, "r") as file:
    word_list = file.read().split()

# Print words with more than 20 characters
print("Here are the words that have 20 or more characters: ")
for i in range(len(word_list)):
    if len(word_list[i]) > 20:
        print(word_list[i])

