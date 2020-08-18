# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
# https://docs.python.org/3/library/csv.html
import csv

import statistics

## This os.path.join function is used to concatenate all of the provided arguments 
## together with the forwardslash/backslash that is appropriate for your operating 
## system. This allows our code to operate regardless of the operating system.


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
        pl= int(row[1])

        months.append(month)
        pls.append(pl)



print("Financial Analysis")
print("-"* 40)

#Print the total number of months included in the dataset 
print(f"Total Months: {len(months)}")


#Print the net total amount of "Profit/Losses" over the entire period
print(f"Total: $ {sum(pls)}")

#Print the mean of P/L over the entire period
print(f"Average Change: $ {round(statistics.mean(pls),2)}")


pmax = max(pls)
pmax_index = pls.index(pmax)
pmax_month = months[pmax_index]

pmin = min(pls)
pmin_index = pls.index(pmin)
pmin_month = months[pmin_index]


print(f"The greatest increase in profits: {pmax_month} (${pmax})")
print(f"The greatest decrease in profits: {pmin_month} (${pmin})")



