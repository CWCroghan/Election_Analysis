# Retrieve the following data
# 1. Total number of votes cast
# 2. Complete list of unique candidates who received votes
# 3. The percent of votes for each candidate
# 4. The max percent of votes and related candidate

# Import datetime class from datetime module
import datetime as dt
# Use the now() attribute on the datetime class to get present time.
now = dt.datetime.now()
# Print the present time.#
#print("The current time is ", now)

# Import csv modula
import csv

import os
# Assign variable for file path
file_to_load = os.path.join('Resources','election_results.csv')

# Open election results and read the file

with open(file_to_load) as election_data:
    # Do stuff
    file_reader = csv.reader(election_data)
    header = next(file_reader)
    print(header)
    #for row in file_reader:
    #    print(row)

#file_to_save = os.path.join("analysis","election_analysis.txt")
