
import csv
import os

csvpath = os.path.join('pybank', 'Resources','budget_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvreader)
    
    print(f"csv header: {csv_header}")

#define
    months = 0 
    nettotal = 0
    date = []
    avgchange = []
    profit = []

#total months
    for row in csvreader: 
        months = months + 1
        
#net total amount of profit/losses
        nettotal = nettotal + int(row[1])

#The changes in profit/losses
        date.append(row[0])
        profit.append(int(row[1]))
        
    for i in range(len(profit)-1):
        avgchange.append(profit[i+1]-profit[i])

#The greatest increase in profits
        increase = max(avgchange)
        monthlyincrease = avgchange.index(max(avgchange))+1

# The greatest decrease in profits
        decrease = min(avgchange)
        monthlydecrease = avgchange.index(min(avgchange))+1

print(f'Financial Analysis')
print(f'-------------------------------------')
print(f'Total Months:{months}')
print(f'Total: ${nettotal}')
print(f'Average Change: ${round(sum(avgchange)/len(avgchange),2)}')
print(f'Greatest increase in Profits: {date[monthlyincrease]} (${str(increase)})')
print(f'Greatest decrease in Profits: {date[monthlydecrease]} (${str(decrease)})')

output_path = os.path.join('pybank','Analysis','text_file.txt')

with open(output_path, 'w') as csvfile:
    
    csvfile.write(f'Financial Analysis\n')
    csvfile.write(f'-----------------------------------\n')
    csvfile.write(f'Total Months:{months}\n')
    csvfile.write(f'Total: ${nettotal}\n')
    csvfile.write(f'Average Change: ${round(sum(avgchange)/len(avgchange),2)}\n')
    csvfile.write(f'Greatest increase in Profits({date[monthlyincrease]}(${str(increase)})\n')
    csvfile.write(f'Greatest decrease in Profits({date[monthlydecrease]}(${str(decrease)})\n')