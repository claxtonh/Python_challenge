'''
Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''

import os
import csv


filepath = "budget_data.csv"

with open(filepath) as csvfile:
    fileread = csv.reader(csvfile, delimiter=',')
    csv_header = next(fileread)

    totrows=0
    totprofit=0
    change=0
    priorrow=0
    totchange=0
    currentrow=0
    firstTime=True
    maxchange=0
    minchange=0
    maxdate='str'
    mindate='str'
    
    #find total months
    for row in fileread:
        totrows = totrows+1
        totprofit = totprofit +int(row[1])

        currentrow =int(row[1])
        if firstTime==False:
            change = currentrow-priorrow
            totchange = totchange + change
            if change>maxchange:
                maxchange = change
                maxdate = row[0]
            if change < minchange:
                minchange = change
                mindate = row[0]
        priorrow = currentrow
        firstTime=False

print(f'Total Months: {totrows}')
print(f'Total: ${totprofit}')
print(f'Average Change: ${format(totchange/(totrows-1), ".2f")}')
print(f'Greatest Increase in Profits: {maxdate} {maxchange}')
print(f'Greatest Decrease in Profits: {mindate} {minchange}')

myfile=open("summary.txt", "w+") 
    
myfile.write(f'Total Months: {totrows} \n')
    
myfile.write(f'Total: ${totprofit} \n')
    
myfile.write(f'Average Change: ${format(totchange/(totrows-1), ".2f")} \n')
    
myfile.write(f'Greatest Increase in Profits: {maxdate} {maxchange} \n')
    
myfile.write(f'Greatest Decrease in Profits: {mindate} {minchange} \n')