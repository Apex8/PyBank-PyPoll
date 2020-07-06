#PyPoll challenge
#
# Import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join( 'Resources', 'election_data.csv')

# Lists and variables to store data
canidates = []
vote_count = []
votes_cast = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    print(f"{csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

#Extract Data from election_data.csv to create three columns: `Voter ID`, `County`, and `Candidate`
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#Print the analysis to the terminal and export a text file with the results.