import pathlib
import pprint

# Creates a dictionary of the file types and their rate of occurence
# desktop = pathlib.Path("/Users/tabithamccracken/Desktop")
# desktop_file_dict = {}

# for filepath in desktop.iterdir():
#     if filepath.suffix not in desktop_file_dict:
#         desktop_file_dict[filepath.suffix] = 1
    
#     elif filepath.suffix in desktop_file_dict:
#         desktop_file_dict[filepath.suffix] += 1

# pprint.pprint(desktop_file_dict)

# Writes the desktop_file_dict to output.txt file
# file_out = open("/Users/tabithamccracken/Desktop/output.txt","a")
# file_out.write(str(desktop_file_dict))
# file_out.write("\n")
# file_out.close()

# Reads file with 3 step process
# file_in = open("/Users/tabithamccracken/Desktop/output.txt","r")
# contents = file_in.read()
# print(contents)
# file_in.close()
# output = []
# for item in contents:
#     items = item.split(',')
#     output.append([items[0]])
# print(output)

# Read file with context manager
# with open("/Users/tabithamccracken/Desktop/output.txt", "r") as file_in:
#   print(file_in.read())

# import csv

# count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}


# with open("filecounts2.csv", "a") as csvfile:
#     # Adds column names
#     writer = csv.DictWriter(csvfile, fieldnames = ['Col1', 'Col2', 'Col3', 'Col4'])
#     writer.writeheader()

#     # Adds the counts for each file type
#     countwriter = csv.writer(csvfile)
#     data = [count[""], count[".csv"], count[".md"], count[".png"]]
#     countwriter.writerow(data)

# Functions

# def greeting(greeting, name):
#     sentence = f"{greeting}, {name}! How are you?"
#     return sentence

# print(greeting(2,3))

# def greet_many(greeting, *args):
#     greetings = ""
#     for name in args:
#         sentence = f"{greeting}, {name}! How are you?"
#         greetings += sentence + "\n"
#     return greetings

# print(greet_many(greeting = "Hi!", "Kelly", "Jon"))



# # Functionality to capitalize eache word
# def titlecase (text):
#     titlecase = []
#     for word in text.split():
#         cap_word = word.capitalize()
#         titlecase.append(cap_word)
#     return " ".join(titlecase)

# user_input = input("Enter your sentence (Type exit to quit): ")

# # Give output to user
# while user_input.lower() != "exit":
#     crash_blossom = titlecase(user_input)
#     print(titlecase(crash_blossom))
#     user_input = input("Enter your sentence (Type exit to quit): ")

# Enumerate!

locations = ["indonesia", "spain", "thailand", "mexico"]

for index, country in enumerate(locations, start=1):
    print(f"* {index}: {country}")

# Create my own enumerate function
def my_enumerate(a_list):
    result = [] #Creates an empty list to store the index and value as tuples
    counter = 0
    for item in a_list:
        result.append((counter, item))
        counter +=1
    return result

my_list = (my_enumerate(locations))

for index, country in my_list:
    print(f"{index}: {country}")
