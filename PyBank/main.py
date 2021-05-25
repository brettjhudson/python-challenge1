import os
import csv

total = 0
months = 0
sum_change = 0
previous = 0
current_row = 0

change_values = []

#import CSV file budget_data
csvpath = os.path.join("Resources","budget_data.csv")



# open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 

    csvheader = next(csvreader)

#loop through rows
    for row in csvreader:

        current_row = float(row[1])

        total = total + current_row
        months = months + 1

    #calculate change
        change = current_row - previous
        previous = current_row

        sum_change = sum_change + change

        change_values.append(change)

        max_value = max(change_values)
        min_value = min(change_values)

        print(f"current: {row[0]} change: {change}")




#Summary Table
    print(f"Total months: {months}")
    print(f"Total: {total}")
    print(max_value)
    print(min_value)


#Print Summary Table to Text
with open("output.txt", "w") as txt_file:
    txt_file.write(f"Financial Analysis\n_________________\n")
    txt_file.write(f"Total months: {months}\n")
    txt_file.write(f"Total: {total}\n")
    txt_file.write(f"Greatest Change in Profits: {max_value}\n")
    txt_file.write(f"Greatest Decrease in Profits: {min_value}\n")