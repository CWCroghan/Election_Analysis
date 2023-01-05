# Retrieve the following data
# 1. Total number of votes cast
# 2. Complete list of unique candidates who received votes
# 3. The percent of votes for each candidate
# 4. The max percent of votes and related candidate

# Import dependents
import csv
import os
# Assign variables for file path
file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join("analysis","election_analysis.txt")

#Intitializing variables
total_votes = 0
candidate_list = []
candidate_votes = {}

winner = ""
winning_count = 0
winning_percent = 0.0

# Open election results and read the file

with open(file_to_load) as election_data:
    # Do stuff
    file_reader = csv.reader(election_data)
    #print header
    header = next(file_reader)
    print(header)

    #Print data from CSV file
    for row in file_reader:

        total_votes += 1
        
        candidate_name = row[2]
        
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #incrementing up votes for current candidate
        
        candidate_votes[candidate_name] +=1

print(f"Total votes {total_votes:,}")
print(candidate_votes)


for name in candidate_votes:
    votes = candidate_votes[name]
    vote_percent = float(votes)/float(total_votes) * 100
    print(f'{name}: received {vote_percent:.1f}% of the vote.')

    if winning_count < votes:
        winning_count = votes
        winning_percent = vote_percent
        winner = name

print(f"And the winner is {winner} with total {winning_count} for {winning_percent:.1f}% of the votes")



