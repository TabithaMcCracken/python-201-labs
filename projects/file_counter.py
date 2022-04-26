# Add the code for the file counter script that you wrote in the course.

# Get tools
import pathlib

# Find the path to my desktop
desktop = pathlib.Path('/Users/tabithamccracken/Desktop')

# Create new list
file_list = [] 

for filepath in desktop.iterdir(): # Loop through each file
    if filepath.suffix == '.jpg': # Filter files with .jpg
        file_list.append(str(filepath.name)) #Add to file list

print(file_list) # Print the file list