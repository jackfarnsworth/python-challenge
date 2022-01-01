import os
import csv

filepath = os.path.join("Resources", "budget_data.csv")

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = 0
    totalmonths = 0
    previous = 0
    changes = []
    for row in csvreader:
        totalmonths += 1
        changes.append(int(row[1] - previous))
    

    




