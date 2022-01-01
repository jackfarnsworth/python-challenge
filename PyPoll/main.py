import os
import csv

candidates = []
totalvotes = 0
filepath = os.path.join("Resources", "election_data.csv")

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        totalvotes += 1
        iscandidate = False
        for candidate in candidates:
            if row[2] == candidate[0]:
                iscandidate = True
                candidate[1] += 1
                break
        if not iscandidate:
            candidates.append([row[2], 1])

analysis = "Election Results\n-------------------------\n"
analysis += f"Total Votes : {totalvotes}\n-------------------------\n"

for candidate in candidates:
    analysis += f"{candidate[0]}: {round(candidate[1]/totalvotes, 3)*100}% ({candidate[1]})\n"

sorted = list(zip(*candidates))
analysis += f"Winner: {sorted[0][sorted[1].index(max(sorted[1]))]}"

print(analysis)
