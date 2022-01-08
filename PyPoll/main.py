import os
import csv

#initialization
candidates = {}
filepath = os.path.join("Resources", "election_data.csv")

#Reading csv and making dictionary. Dictionary has values of the form {candidate name : total votes}
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        #if candidate does not have votes we add them to dictionary with initial vote
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

print(candidates)

#Formatting string
totalvotes = sum(candidates.values())
analysis = "Election Results\n-------------------------\n"
analysis += f"Total Votes : {totalvotes}\n-------------------------\n"
#loop through dictionary adding a line for each candidate with form name, percent, total
for name in candidates:
    analysis += f"{name}: {candidates[name]/totalvotes*100:.3f}% ({candidates[name]})\n"
analysis += f"""-------------------------
Winner: {max(candidates, key=candidates.get)}
-------------------------
"""
#write values to screen and text file
open("analysis.txt", "w").write(analysis)
print(analysis)
