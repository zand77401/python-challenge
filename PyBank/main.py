# Module for reading CSV files

import csv

#Module for basic statistics 
import statistics

#Set a path for the CSV file

csvpath = 'Resources/budget_data.csv'



with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #Create lists of months and profit/losses
    months, pls = [], []

    for row in csvreader:
        month = row[0]
        pl = int(row[1])

        months.append(month)
        pls.append(pl)


#Loop through each item in pl list and create a new "Montly Change" list by subtracting month +1 by month starting at row 1 
monthtly_changes = []
index_change = 867884
for i in pls[1:]:
    monthtly_change = i - index_change
    monthtly_changes.append(monthtly_change)
    index_change = i

#Loop through monthly changes to find the max and min profits
#Find the index of max and min profit values and set to variables to find the index
for i in monthtly_changes:
    if i == max(monthtly_changes):
        max_profit = i
        max_profit_index = 1 + (monthtly_changes.index(i))
    elif i == min(monthtly_changes):
        min_profit = i
        min_profit_index = 1 + (monthtly_changes.index(i))

#Set variables using max and min profit index variables into the months list to find the respective month with max and min profits
max_profit_month = months[max_profit_index]
min_profit_month = months[min_profit_index]


print("Financial Analysis")
print("-"* 40)

#Print the total number of months included in the dataset 
print(f"Total Months: {len(months)}")



#Print the net total amount of "Profit/Losses" over the entire period
print(f"Total: ${sum(pls)}")

#Print the mean of P/L over the entire period
print(f"Average Change: ${round(statistics.mean(monthtly_changes),2)}")

#Print the greatest increase and decrease in profits with each respective month and profit/loss value
print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_profit_month} (${min_profit})")

#Export results to txt file by using command in GitBash as follows: python main.py > PyBank_Output.txt