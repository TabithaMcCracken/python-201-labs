# To get that information, write a script that locates your Desktop, fetches all 
# the files that are on there, and counts how many files of each different file type 
# are on your desktop. Use a dictionary to collect this data, and print it to your 
# console at the end in order to get an overview of what is there.

# You can now expand on your file mover script and add logic that moves all file 
# types that have e.g. more than five files on the desktop into their own separate folder. 
# Will it help to keep your desktop cleaner?

# It could be interesting to keep track of what types of files keep agglomerating 
# on your desktop in surprising numbers, also after you've cleaned it yet again. 
# You wrote this script that counts them and shows you the counts as a dictionary, 
# but you'll probably forget these numbers until the next time you run the script.

# Get tools
import pathlib
import pprint
import os

# Find the path to my desktop and the file type files
desktop = pathlib.Path('/Users/tabithamccracken/Desktop')
jpg_folder = pathlib.Path('/Users/tabithamccracken/Desktop/jpg_folder')
png_folder = pathlib.Path('/Users/tabithamccracken/Desktop/png_folder')
jpeg_folder = pathlib.Path('Users/tabithamccracken/Desktop/jpeg_folder')


# Create a dictionary of file types and the quantity of them in my desktop

# Create new dict
file_dict = {} 

# Create a dict of file types
for filepath in desktop.iterdir(): # Loop through each file
    if filepath.suffix not in file_dict: # Adds new file type and value to the dict
        file_dict[filepath.suffix] = 1
        
    elif filepath.suffix in file_dict: # Adds value to the dict if the key already exits
        file_dict[filepath.suffix] += 1
pprint.pprint(file_dict)

# Makes new folders if the file values are greater than 5
for filepath in desktop.iterdir():
    # Filter for .jpg files
    if filepath.suffix == ".jpg" and file_dict[".jpg"] > 5:
        # Create new folder
        jpg_folder.mkdir(exist_ok=True)
        # Create new path for each file
        new_jpg_path = jpg_folder.joinpath(filepath.name)
        # Move the jpg file to the new folder
        filepath.replace(new_jpg_path)
        
    elif filepath.suffix == ".png" and file_dict[".png"] > 5:
        png_folder.mkdir(exist_ok=True)
        new_png_path = png_folder.joinpath(filepath.name)
        filepath.replace(new_png_path)

    elif filepath.suffix == ".jpeg" and file_dict[".jpeg"] > 5:
        jpeg_folder.mkdir(exist_ok=True)
        new_jpeg_path = kpeg_folder.joinpath(filepath.name)
        filepath.replace(new_jpeg_path)

# Is there a way to do this without looping through 2 x's?
# Do I have to create the folders first, or can I create the folder name and path 
# only once it is determined to have 5 files or more?


# Practice 

# Create a list of the file types to be used as the file name
# file_list = []
# for filepath in desktop.iterdir():
#     if filepath.suffix not in file_list:
#         file_list.append(filepath.suffix)   
# print(file_list)


# Remove '.' on file type
# file_list = [i[1:] for i in file_list]
# print(file_list)


# Creating folders with names from a list
# # list = ['car', 'truck', 'bike']
# for items in list:
#     path = os.path.join(desktop, items)
#     os.mkdir(path)
