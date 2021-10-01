
# import poll
import os
import csv

# directory 
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    # Variables

    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    # Counting votes
    total_votes = (len(votes))

    # Votes for candidates
    for candidate in candidates:
        if candidate == 'Khan':
           khan.append(candidate )
           khan_votes = len(khan)
        elif candidate == "Correy":
           correy.append(candidate)
           correy_votes = len(correy)
        elif candidate == "Li":
           li.append(candidate)
           li_votes = len(li)
        else:
            otooley.append(candidate)
            otooley_votes = len(otooley)

# Percentages
khan_percent = round(((khan_votes / total_votes) * 100), 2)
correy_percent = round(((correy_votes / total_votes) * 100), 2)
li_percent = round(((li_votes / total_votes) * 100), 2)
otooley_percent = round(((otooley_votes / total_votes) * 100), 2)

# Finding winners
if khan_percent > max(correy_percent, li_percent, otooley_percent):
    winner = "Khan"
elif correy_percent > max(khan_percent, li_percent, otooley_percent):
    winner = "Correy"
elif li_percent > max(correy_percent, khan_percent, otooley_percent):
    winner = "Li"
else: 
    winner = "O'Tooley"

election_results = f"""
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
Khan: {khan_percent}% ({khan_votes})
Correy: {correy_percent}% ({correy_votes})
Li: {li_percent}% ({li_votes})
O'Tooley: {otooley_percent}% ({otooley_votes})

----------------------------
Winner = {winner}
----------------------------

"""

with open("results.txt", "w") as datafile:
    datafile.write(election_results)

print(election_results)
