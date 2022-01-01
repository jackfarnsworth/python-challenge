import os
import csv

filepath = os.path.join("..", "csv_files", "election_data.csv")

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(header)
