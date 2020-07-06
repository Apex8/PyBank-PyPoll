#PyPoll challenge
#
#
# Import the os module and module for reading CSV files
import os
import csv

# Set file path
csvpath = os.path.join( 'Resources', 'election_data.csv')
pathout = os.path.join( "Analysis", "election_results.txt")

# Lists and variables to store data
candidates = []
votes = []
percentages = []
vote_count = 0
can_index = 0

#Extract Data from election_data.csv to create three columns: `Voter ID`, `County`, and `Candidate`
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
    # The total number of votes cast
        vote_count = vote_count + 1

    # A complete list of candidates who received votes
        if candidate in candidates:
            can_index = candidates.index(candidate)
            vote_count[can_index] = vote_count[can_index] + 1
        else:
            candidates.append(candidate)
            vote_count.append(1)

    # The percentage of votes each candidate won.
    # The total number of votes each candidate won.
    # The winner of the election based on popular vote.

# Print the analysis to the terminal.
#
#  Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------


print("Election Results")
print("----------------------------")
print(f"Total votes:  {votes}")
print("----------------------------")
print(f"Khan: ")
print(f"")
print(f"")
print(f"")


#  Export a text file with the results to Analysis folder.
with open(pathout, "w") as results:
    results.write("Election Results\n")
    results.write("")