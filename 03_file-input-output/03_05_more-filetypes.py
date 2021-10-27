# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.



# Get tools
import pathlib
import csv

# Find the path to my desktop and the file type files
desktop = pathlib.Path('/Users/tabithamccracken/Desktop')
count_totals_path = pathlib.Path('/Users/tabithamccracken/Desktop/count_totals')


# Create a dictionary of file types and the quantity of them in my desktop

# Create new dict
file_dict = {} 

# Create a dict of file types
for filepath in desktop.iterdir(): # Loop through each file
    if filepath.suffix not in file_dict: # Adds new file type and value to the dict
        file_dict[filepath.suffix] = 1
        
    elif filepath.suffix in file_dict: # Adds value to the dict if the key already exits
        file_dict[filepath.suffix] += 1
print(file_dict)

# Write the list to a new csv file
fields = [".jpeg", ".jpg", ".pdf", ".txt"]

with open(count_totals_path, "a") as csvfile:
    # Create csv writer object
    csvwriter = csv.writer(csvfile)

    # Write the header
    csvwriter.writerow(fields)

    # Put the file counts in a variable
    data = file_dict[".jpeg"], file_dict[".jpg"], file_dict[".pdf"], file_dict[".txt"]
    
    # Write the file counts data to a row
    csvwriter.writerow(data)