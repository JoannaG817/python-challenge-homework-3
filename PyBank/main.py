import os
import csv

# path to collect data from the Resources folder
budget_data_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# create lists
total_months = []
total_profit = []
monthly_profit_change = []

# open cvs file 
with open(budget_data_csv, newline="",) as budget:
    # store data under the csvreader variable
    csvreader = csv.reader(budget, delimiter=",")
    # skip the header
    csv_header = next(csvreader)
    for row in csvreader:
        # append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    for i in range(len(total_profit)-1):
         # take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)
# correlate max and min to the proper month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

# print the summary table
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# save results as a text file
file_path = os.path.join("PyBank", "Analysis", "PyBank_Financial_Analysis.txt")
with open(file_path,"w") as text_file:
    text_file.write("Financial Analysis")
    text_file.write("\n")
    text_file.write("----------------------------")
    text_file.write("\n")
    text_file.write(f"Total Months: {len(total_months)}")
    text_file.write("\n")
    text_file.write(f"Total: ${sum(total_profit)}")
    text_file.write("\n")
    text_file.write(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    text_file.write("\n")
    text_file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    text_file.write("\n")
    text_file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


