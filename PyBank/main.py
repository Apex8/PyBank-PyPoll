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

# Lists and variables to store data
monthly_pnl = []
profits = []
date = []
months = 0
net_pnl = 0
pnl_change = 0
initial_pnl = 0
total = 0 
prev_rev = 0
change = 0
total_change = 0
inc = ["",0]
dec = ["",0]

# Open path
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header and assign variables
    for row in csvreader:
        # print(row)
        date.append(row[0])
        monthly_pnl.append(row[1])

    # Create script to calculate the following:

        #The total number of months included in the dataset
        
        months += 1
        total += int(row[1])

        #Evaluate change
        change = int(row[1]) - prev_rev
        if prev_rev == 0:
            change = 0
        prev_rev = int(row[1])
        total_change += change

        #Evaluate Increase
        if change > int(inc[1]):
            inc[1] = change
            inc[0] = row[0]

        #Evaluate Decrease
        if change < int(dec[1]):
            dec[1] = change
            dec[0] = row[0]


    total_change = total_change / (months - 1)
        



        # The net total amount of "Profit/Losses" over the entire period
        # net_pnl = net_pnl + int(row[1])
        # final_pnl = int(row[1])

        # # The average of the changes in "Profit/Losses" over the entire period
        # monthly_pnl_change = final_pnl - initial_pnl
        # monthly_pnl.append(monthly_pnl_change)
        # pnl_change = pnl_change + monthly_pnl_change
        # average_pnl_change = (pnl_change/months)

        # # The greatest increase in profits (date and amount) over the entire period
        # # The greatest decrease in losses (date and amount) over the entire period

        # greatest_inc = int(monthly_pnl_change)
        # greatest_dec = int(monthly_pnl_change)

        # # inc_pnl = [date[monthly_pnl_change.index(greatest_inc)]]
        # dec_pnl = [date[monthly_pnl_change.index(greatest_dec)]]

# Print the analysis to the terminal
print("\n\nFinancial Analysis")
print("----------------------------")
print(f"Months total in Analysis:  {months}")
print(f"Total:  ${total}")
print(f" Average  Change: ${total_change:.2f}")
print(f"Greatest Increase in Profits: {inc[0]} (${inc[1]})")
print(f"Greatest Decrease in Profits: {dec[0]} (${dec[1]})")
# print(f"Greatest Profit month:  {inc_pnl} (${greatest_inc})")
# print(f"Greatest Loss month:  {dec_pnl} (${greatest_dec})")

 # Export a text file with the results to Analysis folder
# with open(pathout, "w") as results:
#     results.write("Bank Analysis\n")
#     results.write("-----------------------------\n")
#     results.write(f"Months total in Analysis: {months}\n")
#     results.write(f"Profit and Loss total: ${final_pnl}\n")
#     results.write(f"Average Profit/Loss change: ${average_pnl_change}\n")
    # results.write(f"Greatest Profit month: {inc_pnl} (${greatest_inc}\n")
    # results.write(f"Greatest Loss month: {dec_pnl} (${greatest_dec}\n")
