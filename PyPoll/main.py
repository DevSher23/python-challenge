import csv
import os


csvpath = os.path.join('PyPoll','Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvreader)
    
    print(f"csv header: {csv_header}")

    county = []
    candidates = []
    candidates_dict = {}
    votescast = 0
    winnername = ""
    winnervotes = 0

# number of votes cast
    for row in csvreader:
        votescast = votescast + 1

# A complete list of candidates who received votes
        candidatename = row[2]
        if candidatename not in candidates:
            candidates.append(candidatename)
            candidates_dict[candidatename] = 0 

        candidates_dict[candidatename] += 1
        

for candidate in candidates:
    votes = candidates_dict[candidate]


    if votes > winnervotes:
        winnername = candidate
        winnervotes = votes

output = f"""
Election Results
-------------------------
Total Votes: {votescast}
-------------------------
Charles Casper Stockham: {(candidates_dict['Charles Casper Stockham']/votescast)*100:.3f}% ({candidates_dict['Charles Casper Stockham']})
Diana DeGette: {(candidates_dict['Diana DeGette']/votescast)*100:.3f}% ({candidates_dict['Diana DeGette']})
Raymon Anthony Doane: {(candidates_dict['Raymon Anthony Doane']/votescast)*100:.3f}% ({candidates_dict['Raymon Anthony Doane']})
-------------------------
Winner: {winnername}
-------------------------
"""

print(output)

output_path = os.path.join('PyPoll','Analysis','text_file.txt')

with open(output_path, 'w') as csvfile:
    csvfile.write(output)