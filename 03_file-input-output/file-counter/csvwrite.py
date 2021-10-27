# Write the file counts to a `.csv` file.

import csv

# Get the file counts and put them in a list
with open("03_file-input-output/file-counter/filecounts.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)
    print (counts)

# Write the list to a new csv file
with open("03_file-input-output/file-counter/counttotals.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    header = ["Folder", "CSV", "MD", "PNG"]
    data = counts[0]["Folder"], counts[0]["CSV"], counts[0]["MD"], counts[0]["PNG"]
    countwriter.writerow(header)
    countwriter.writerow(data)