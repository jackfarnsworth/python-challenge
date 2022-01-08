import os
import csv


previous = None
total = 0
months = 0
changes = 0
greatest = None
least = None

filepath = os.path.join("Resources", "budget_data.csv")


#functions
def isgreatest(x, greatest):
    if greatest == None:
        greatest = x
    else:
        if int(x[1]) > int(greatest[1]):
            greatest = x
    return greatest

def isleast(x, least):
    if least == None:
        least = x
    else:
        if int(x[1]) < int(least[1]):
            least = x
    return least

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        greatest = isgreatest(row, greatest)
        least = isleast(row, least)
        months += 1
        total += int(row[1])
        if previous == None:
            previous = int(row[1])
            continue
        changes += int(row[1]) - previous
        previous = int(row[1])

#string format
analysis = f"""Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average Change: ${round(changes/(months - 1),2)}
Greatest Increase in Profits: {greatest[0]} (${greatest[1]})
Greatest Decrease in Profits: {least[0]} (${least[1]})"""

open("analysis.txt", "w").write(analysis)
print(analysis)
