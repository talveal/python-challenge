#import modules
import os, csv

csvpath = os.path.join('election_data.csv')

# Open and read CSV file
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
# Read the header row first (skip this step if there is no header)
    next(reader)

# Set variables
    tot_votes = 0
    candidate_votes = {}
    candidates = []

# Loop through each row in the CSV file
    for row in reader:
        # Skip the header row
        if row[0] == 'Ballot ID':
            continue
        # Count the total number of votes
        tot_votes += 1
# Add candidate to list if not already in list
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1

# Calculate the percentage of votes each candidate won
    percentages = {}
    for candidate in candidates:
        percent = round(candidate_votes[candidate] / tot_votes * 100, 3)
        percentages[candidate] = percent
# Find the winner of the election
    winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {tot_votes}")
    print("-------------------------")
#for each candidate, print the candidate's name, percentage of vote, and total number of votes
    for candidate in candidates:
        print(f"{candidate}: {percentages[candidate]}% ({candidate_votes[candidate]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

#Create the text file with the results
    with open("PyPoll_Analysis.txt", 'w') as file_PythonChallenge:
        file_PythonChallenge.write(f"""Election Results
-------------------------------------
Total Votes: {tot_votes} \n""")
        for candidate in candidates:
            file_PythonChallenge.write(f'{candidate}: {percentages[candidate]}% ({candidate_votes[candidate]})\n')
            file_PythonChallenge.write('-----------------------------------\n')
            file_PythonChallenge.write(f'Winner: {winner}\n')
            file_PythonChallenge.write('-----------------------------------\n')