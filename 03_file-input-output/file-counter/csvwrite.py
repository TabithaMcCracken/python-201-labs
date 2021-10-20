# Write the file counts to a `.csv` file.

import csv

# Get the file counts and put them in a list
with open("filecounts.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

# Write the list to a new csv file
with open("counttotals.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    header = ["Folder", "CSV", "MD", "PNG"]
    data = counts["Folder"], counts["CSV"], counts["MD"], counts["PNG"]
    countwriter.writerow(header)
    countwriter.writerow(data)