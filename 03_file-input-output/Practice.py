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