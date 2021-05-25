import os
import csv
from io import StringIO

total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0

candidate_count = {}

#import CSV file budget_data
csvpath = os.path.join("Resources","election_data.csv")

buffer = StringIO()

# open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

#Calculate Total Votes
    for row in csvreader:

        total_votes = total_votes + 1

   

#Use dictionary to get candidates, tally results
    
        candidate = row[2].strip()
        found = candidate in candidate_count

        if found == True: 
            candidate_count[candidate] +=1

        else:
            candidate_count[candidate] = 1

   


    most_votes = 0
    winner = ""
    buffer.write("Election Results\n-------------------------\n")
    buffer.write(f"Total Votes: {total_votes}\n")
    for runner, count in candidate_count.items():
        # print(runner)
        # print(count)
        candidate_percent = 100 * count / total_votes
        # print(100* count / total_votes)
        if count > most_votes:
            most_votes = count
            winner = runner
    
        buffer.write(f"RESULTS {runner}, {candidate_percent}%, ({count})\n")
    buffer.write(f"Winner: {winner}")
    buffer.seek(0)
    print(buffer.read())
    buffer.seek(0)
#summary table printout

    with open("output1.txt", "w") as txt_file:
        txt_file.write(buffer.read())
        
        



# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------