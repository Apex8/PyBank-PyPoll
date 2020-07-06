# PyBank analysis script
#
#
# Import the os module and the csv module
import os
import csv

# Set path for data
csvpath = os.path.join( "Resources", "budget_data.csv")
pathout = os.path.join( "Analysis", "budget_analysis.txt")

# Lists and variables to store data
date = []
monthly_pnl = []
months = 0
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


# Print the analysis to the terminal
print("\n\nFinancial Analysis")
print("----------------------------")
print(f"Months total in Analysis:  {months}")
print(f"Total:  ${total}")
print(f" Average  Change: ${total_change:.2f}")
print(f"Greatest Increase in Profits: {inc[0]} (${inc[1]})")
print(f"Greatest Decrease in Profits: {dec[0]} (${dec[1]})")


 # Export a text file with the results to Analysis folder
with open(pathout, "w") as results:
     results.write("\n\nFinancial Analysis\n")
     results.write("----------------------------\n")
     results.write(f"Months total in Analysis:  {months}\n")
     results.write(f"Total:  ${total}\n")
     results.write(f" Average  Change: ${total_change:.2f}\n")
     results.write(f"Greatest Increase in Profits: {inc[0]} (${inc[1]})\n")
     results.write(f"Greatest Decrease in Profits: {dec[0]} (${dec[1]})\n")