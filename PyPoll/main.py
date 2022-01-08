import os
import csv

#initial values
candidates = {}
filepath = os.path.join("Resources", "election_data.csv")

#Reading csv and making dictionary
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

print(candidates)

#Formatting string
totalvotes = sum(candidates.values())
analysis = "Election Results\n-------------------------\n"
analysis += f"Total Votes : {totalvotes}\n-------------------------\n"
for name in candidates:
    analysis += f"{name}: {candidates[name]/totalvotes*100:.3f}% ({candidates[name]})\n"
analysis += f"""-------------------------
Winner: {max(candidates, key=candidates.get)}
-------------------------
"""
open("analysis.txt", "w").write(analysis)
print(analysis)
