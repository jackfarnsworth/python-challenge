import os
import csv

#variable initializations; setting to None for values that may be 0
filepath = os.path.join("Resources", "budget_data.csv")
previous = None
total = 0
months = 0
change = 0
sumchanges = 0
greatest = None
least = None

#greatest and least functions, takes and returns a list for easy referencing in fstring
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
        total += int(row[1])
        months += 1
        #on first row, difference does not exist so set previous to that row and continue
        if previous == None:
            previous = int(row[1])
            continue
        change = int(row[1]) - previous
        sumchanges += change
        previous = int(row[1])
        #on second row in csv set greatest/least to that change else run funcs
        greatest = isgreatest([row[0], change], greatest) if greatest else [row[0], change]
        least = isleast([row[0], change], least) if least else [row[0], change]

#string format, average calculation done in place
analysis = f"""Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average Change: ${round(sumchanges/(months - 1),2)}
Greatest Increase in Profits: {greatest[0]} (${greatest[1]})
Greatest Decrease in Profits: {least[0]} (${least[1]})"""

#write values to screen and doc
open("analysis.txt", "w").write(analysis)
print(analysis)
