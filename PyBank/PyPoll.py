# Import the csv module
import csv

# Open the budget_data.csv file in read mode
with open('budget_data.csv', 'r') as file:
    # Create a csv reader object
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Initialize the variables
    total_months = 0 # The total number of months
    total_profit_loss = 0 # The net total amount of profit/losses
    prev_profit_loss = 0 # The previous month's profit/loss
    changes = [] # A list of changes in profit/losses
    max_increase = 0 # The greatest increase in profits
    max_increase_date = '' # The date of the greatest increase in profits
    max_decrease = 0 # The greatest decrease in profits
    max_decrease_date = '' # The date of the greatest decrease in profits
    # Loop through each row in the file
    for row in reader:
        # Get the date and profit/loss from the row
        date = row[0]
        profit_loss = int(row[1])
        # Increment the total months by 1
        total_months += 1
        # Add the profit/loss to the total profit/loss
        total_profit_loss += profit_loss
        # If this is not the first month, calculate the change in profit/loss
        if total_months > 1:
            change = profit_loss - prev_profit_loss
            # Append the change to the changes list
            changes.append(change)
            # If the change is greater than the max increase, update the max increase and date
            if change > max_increase:
                max_increase = change
                max_increase_date = date
            # If the change is less than the max decrease, update the max decrease and date
            if change < max_decrease:
                max_decrease = change
                max_decrease_date = date
        # Set the previous profit/loss to the current profit/loss
        prev_profit_loss = profit_loss

# Calculate the average of the changes in profit/losses, rounded to two decimal places
average_change = round(sum(changes) / len(changes), 2)

# Print the results to the terminal
print('Financial Analysis')
print('------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_loss}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')
print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')

# Write the results to a text file named output.txt
with open('output.txt', 'w') as file:
    file.write('Financial Analysis\n')
    file.write('------------------\n')
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: ${total_profit_loss}\n')
    file.write(f'Average Change: ${average_change}\n')
    file.write(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})\n')
    file.write(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n')
