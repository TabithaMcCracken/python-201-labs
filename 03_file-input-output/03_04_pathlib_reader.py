# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

import csv
from pathlib import Path

file_counts_path = "/Users/tabithamccracken/Documents/codingnomads/python-201/03_file-input-output/file-counter/filecounts.csv"
count_totals_path = "/Users/tabithamccracken/Documents/codingnomads/python-201/03_file-input-output/file-counter/counttotals.csv"

# Get the file counts and put them in a list
with open(file_counts_path, "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

# Write the list to a new csv file
with open(count_totals_path, "a") as csvfile:
    countwriter = csv.writer(csvfile)
    header = ["Folder", "CSV", "MD", "PNG"]
    data = counts[0]["Folder"], counts[0]["CSV"], counts[0]["MD"], counts[0]["PNG"]
    countwriter.writerow(header)
    countwriter.writerow(data)

# Not sure if this is what the instructions are asking for?
