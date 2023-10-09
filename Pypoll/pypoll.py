# Import the csv module
import csv

# Open the election_data.csv file in read mode
with open('election_data.csv', 'r') as file:
    # Create a csv reader object
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Initialize the variables
    total_votes = 0 # The total number of votes cast
    candidates = {} # A dictionary of candidates and their votes
    winner = '' # The winner of the election based on popular vote
    winner_votes = 0 # The total number of votes for the winner
    # Loop through each row in the file
    for row in reader:
        # Get the candidate name from the row
        candidate = row[2]
        # Increment the total votes by 1
        total_votes += 1
        # If the candidate is already in the dictionary, increment their votes by 1
        if candidate in candidates:
            candidates[candidate] += 1
        # Otherwise, add the candidate to the dictionary with 1 vote
        else:
            candidates[candidate] = 1

# Print the results to the terminal
print('Election Results')
print('----------------')
print(f'Total Votes: {total_votes}')
print('----------------')
# Loop through each candidate in the dictionary
for candidate, votes in candidates.items():
    # Calculate the percentage of votes for each candidate, rounded to three decimal places
    percentage = round(votes / total_votes * 100, 3)
    # Print the candidate name, percentage and votes
    print(f'{candidate}: {percentage}% ({votes})')
    # If the candidate has more votes than the current winner, update the winner and winner votes
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
print('----------------')
# Print the winner of the election based on popular vote
print(f'Winner: {winner}')
print('----------------')

# Write the results to a text file named output.txt
with open('output.txt', 'w') as file:
    file.write('Election Results\n')
    file.write('----------------\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write('----------------\n')
    for candidate, votes in candidates.items():
        percentage = round(votes / total_votes * 100, 3)
        file.write(f'{candidate}: {percentage}% ({votes})\n')
    file.write('----------------\n')
    file.write(f'Winner: {winner}\n')
    file.write('----------------\n')
