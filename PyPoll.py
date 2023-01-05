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

#Saving results to text file
with open(file_to_save, "w") as txt_file:
    #print(f"Total votes {total_votes:,}")
    #print(candidate_votes)

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for name in candidate_votes:
        votes = candidate_votes[name]
        vote_percent = float(votes)/float(total_votes) * 100
        #print(f'{name}: received {vote_percent:.1f}% of the vote.')
        candidate_results = (f'{name}: {vote_percent:.1f}% ({votes:,})\n')

        print(candidate_results)
        txt_file.write(candidate_results)

        if winning_count < votes:
            winning_count = votes
            winning_percent = vote_percent
            winner = name
    

# Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percent:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
