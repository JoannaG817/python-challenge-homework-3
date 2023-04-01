import os
import csv

# path to collect data from the Resources folder
election_data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# create lists
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# open cvs file 
with open(election_data_csv, newline="",) as elections:
    # store data under the csvreader variable
    csvreader = csv.reader(elections, delimiter=",")
    # skip the header
    csv_header = next(csvreader)
    for row in csvreader:
        # count the total number of votes
        count = count + 1
        # set the candidate names to candidatelist
        candidatelist.append(row[2])
        # create a set from the candidatelist to get the unique candidate names
    for a in set(candidatelist):
        unique_candidate.append(a)
        # b s the total number of votes per candidate
        b = candidatelist.count(a)
        vote_count.append(b)
        # c is the percent of total votes per candidate
        c = (b/count) * 100
        vote_percent.append(c)

    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

# print the summary table
print("----------------------------")
print("Election Results")
print("----------------------------")
print("Total Votes :" + str(count))
print("----------------------------")
for i in range(len(unique_candidate)):
    print(unique_candidate[i] + ": " + str(vote_percent[i]) + "% (" + str(vote_count[i])+ ")")
print("----------------------------")
print("Winner: " + winner)
print("----------------------------")

# save results as a text file
file_path = os.path.join("PyPoll", "Analysis", "PyPoll_Election_Results.txt")
with open(file_path,"w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("----------------------------\n")
    text_file.write("Total Votes: " + str(count) + "\n")
    text_file.write("----------------------------\n")
    for i in range(len(unique_candidate)):
        text_file.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")\n")
    text_file.write("----------------------------\n")
    text_file.write("Winner: " + winner + "\n")
    text_file.write("----------------------------\n")