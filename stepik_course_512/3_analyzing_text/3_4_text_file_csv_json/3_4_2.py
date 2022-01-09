import csv
import collections
primary_type = []
with open("Crimes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        primary_type.append(row['Primary Type'])

print(collections.Counter(primary_type))