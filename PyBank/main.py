# PyBank analysis script
#
#
# Import the os module
import os

# Module for reading CSV files
import csv

# Set path for data
csvpath = os.path.join( "Resources", "budget_data.csv")
pathout = os.path.join( "Analysis", "budget_analysis.txt")

# Lists to store data
monthly_pnl = []
profits = []
date = []

# Create variables where required
months = 0
net_pnl = 0
pnl_change = 0
initial_pnl = 0


# Open path
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header and assign variables
    for row in csvreader:
        print(row)
        date.append(row[0])
        monthly_pnl.append(row[1])

    # Create script to calculate the following:

        #The total number of months included in the dataset
        months =+ 1

        # The net total amount of "Profit/Losses" over the entire period
        net_pnl = net_pnl + int(row[1])
        final_pnl = int(row[1])

        # The average of the changes in "Profit/Losses" over the entire period
        monthly_pnl_change = final_pnl - initial_pnl
        monthly_pnl.append(monthly_pnl_change)
        pnl_change = pnl_change + monthly_pnl_change
        average_pnl_change = (pnl_change/months)

        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in losses (date and amount) over the entire period

        greatest_inc = int(monthly_pnl)
        greatest_dec = int(monthly_pnl)

        inc_pnl = date[monthly_pnl.index(greatest_inc)]
        dec_pnl = date[monthly_pnl.index(greatest_dec)]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Months total in Analysis:  {months}")
print(f"Profit and Loss total:  ${final_pnl}")
print(f"Average Profit/Loss change:  ${average_pnl_change}")
print(f"Greatest Profit month:  {inc_pnl} (${greatest_inc})")
print(f"Greatest Loss month:  {dec_pnl} (${greatest_dec})")

 # Export a text file with the results to Analysis folder
with open(pathout, "w") as results:
    results.write("Analysis\n")
    results.write("-----------------------------\n")
    results.write(f"Months total in Analysis: {months}\n")
    results.write(f"Profit and Loss total: ${final_pnl}\n")
    results.write(f"Average Profit/Loss change: ${average_pnl_change}\n")
    results.write(f"Greatest Profit month: {inc_pnl} (${greatest_inc}\n")
    results.write(f"Greatest Loss month: {dec_pnl} (${greatest_dec}\n")
