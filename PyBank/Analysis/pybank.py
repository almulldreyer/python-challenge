
# Basics
import os 
import csv 

# Connecting CSV 

# csvpath = os.path.join('..','Resources', 'budget_data.csv')

# Open file
with open("../Resources/budget_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)

    # Header Row
    next(csvreader)

    # Lists for Budget Data
    months = []
    profit_loss = []

    # Read CSV file:
    for row in csvreader:

        months.append(row[0])
        profit_loss.append(int(row[1]))

    # Variables for equations for Length of Months & Sum of Profit Loss
    total_months = len(months)
    total_profit_loss = sum(profit_loss)
    average_change = round(total_profit_loss/total_months, 2)
    max_increase = max(profit_loss)
    min_increase = min(profit_loss)
    max_increase_month = months[profit_loss.index(max_increase)]
    min_increase_month = months[profit_loss.index(min_increase)]

    # Find Location of Max increase and min increase 

financial_analysis = f"""
Financial Analysis
----------------------------
Total Months: {str(len(months))}
Total: ${str(total_months)}
Average  Change: ${str(average_change)}
Greatest Increase in Profits: {max_increase_month} (${max_increase})
Greatest Decrease in Profits: {min_increase_month} (${min_increase})
"""

with open("output.txt", "w") as datafile:
    datafile.write(financial_analysis)

print(financial_analysis)
