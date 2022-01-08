import os
import csv

#variable initializations; setting to None for values that may be 0
filepath = os.path.join("Resources", "budget_data.csv")
previous = None
total = 0
months = 0
changes = 0
greatest = None
least = None

#greatest and least functions, returns whole row for easy referencing in fstring
def isgreatest(row, greatest):
    if int(row[1]) > int(greatest[1]):
        greatest = row
    return greatest

def isleast(row, least):
    if int(row[1]) < int(least[1]):
        least = row
    return least

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        #on first row in csv set greatest/least to that row
        greatest = isgreatest(row, greatest) if greatest else row
        least = isleast(row, least) if least else row
        months += 1
        total += int(row[1])
        #on first row, difference does not exist so set previous to that row and continue
        if previous == None:
            previous = int(row[1])
            continue
        changes += int(row[1]) - previous
        previous = int(row[1])

#string format, average calculation done in place
analysis = f"""Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average Change: ${round(changes/(months - 1),2)}
Greatest Increase in Profits: {greatest[0]} (${greatest[1]})
Greatest Decrease in Profits: {least[0]} (${least[1]})"""

#write values to screen and doc
open("analysis.txt", "w").write(analysis)
print(analysis)
