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
county = []
otooley = []
khan = []
correy = []
li = []

#Extract Data from election_data.csv to create three columns: `Voter ID`, `County`, and `Candidate`
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header and loop through rows
    for row in csvreader:
        votes.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
        
    # The total number of votes cast
        voter_total = len(row [1])

    # A complete list of candidates who received votes and the total number of votes each candidate won.
        for can in candidates:
            if can == "khan":
                khan.append(candidates)
                votes_khan = len(khan)
            elif can == "correy":
                correy.append(candidates)
                votes_correy = len(correy)
            elif can == "li":
                li.append(candidates)
                votes_li = len(li)
            else:
                otooley.append(candidates)
                votes_otooley = len(otooley)

    # The percentage of votes each candidate won.
    per_khan = round(((votes_khan / voter_total) * 100), 2)
    per_correy = round(((votes_correy / voter_total) * 100), 2)
    per_li = round(((votes_li / voter_total) * 100), 2)
    per_otooley = round(((votes_otooley / voter_total) * 100), 2)

    # The winner of the election based on popular vote.
    def winner(candidates):
        return max(set(candidates), key = candidates.count)

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
print(f"Khan: %{per_khan} ({votes_khan})")
print(f"Correy: %{per_correy} ({votes_correy})")
print(f"Li: %{per_li} ({votes_li})")
print(f"O'Tooley: %{per_otooley} ({votes_otooley})")
print("----------------------------")
print(f"Winner: ({winner})")
print("----------------------------")

#  Export a text file with the results to Analysis folder.
with open(pathout, "w") as results:
    results.write("Election Results\n")
    results.write("----------------------------\n")
    results.write(f"Total votes:  {votes}\n")
    results.write("----------------------------\n")
    results.write(f"Khan: %{per_khan} ({votes_khan})\n")
    results.write(f"Correy: %{per_correy} ({votes_correy})\n")
    results.write(f"Li: %{per_li} ({votes_li})\n")
    results.write(f"O'Tooley: %{per_otooley} ({votes_otooley})\n")
    results.write("----------------------------\n")
    results.write(f"Winner: ({winner})\n")
    results.write("----------------------------\n")

# Keep trying to run but python file wont start