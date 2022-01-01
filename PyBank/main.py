import os
import csv


previous = None
total = 0
months = 0
changes = []
greatest = None
least = None

filepath = os.path.join("Resources", "budget_data.csv")

def isgreatest(x, greatest):
    if greatest:
        if int(x[1]) > int(greatest[1]):
            greatest = x
    else:
        greatest = x
    return greatest

def isleast(x, least):
    if least:
        if int(x[1]) < int(least[1]):
            least = x
    else:
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
        if previous != None:
            changes.append(int(row[1]) - previous)
        previous = int(row[1])



print("Financial Analysis\n----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${round(sum(changes)/len(changes),2)}")
print(f"Greatest Increase in Profits: {greatest[0]} (${greatest[1]}")
print(f"Greatest Decrease in Profits: {least[0]} (${least[1]})")