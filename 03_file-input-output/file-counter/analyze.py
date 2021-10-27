# Use the `csv` module to read in and count the different file types.

import csv

with open("python-201/03_file-input-output/file-counter/filecounts.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)
print(counts)
print(type(counts))