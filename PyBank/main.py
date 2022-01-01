import os
import csv

filepath = os.path.join("..", "csv_files", "budget_data.csv")

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(header)
