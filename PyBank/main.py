#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. 
# The dataset is composed of two columns: Date and Profit/Losses. 

# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

import os
import csv
csvpath = os.path.normpath("/Users/erendiztarakci/UCBWork/UCB-BER-DATA-PT-02-2020-U-C/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")
month_prof_dict = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #loop through rows in Date column
    for row in csvreader:
        #add to dictionary
        month_prof_dict[int(row[1])] =  row[0]
    
#The total number of months included in the dataset
total_months = len(month_prof_dict)

#The net total amount of "Profit/Losses" over the entire period
total_profloss = sum(month_prof_dict.keys())

#The greatest increase in profits (date and amount) over the entire period
max_profit = max(month_prof_dict.keys())
max_profit_date = month_prof_dict[max_profit]

#The greatest decrease in losses (date and amount) over the entire period
max_loss = min(month_prof_dict.keys())
max_loss_date = month_prof_dict[max_loss]

#get average change btwn months
monthly_change = []
prev_i = 0
for i in month_prof_dict.keys():
    if i == month_prof_dict[list(month_prof_dict.keys())[0]]:
        prev_i = i
        continue
    else:
        change = i - prev_i
        monthly_change.append(change)
        prev_i = i

avg_monthly_change = round(sum(monthly_change)/total_months,2)


#make everything a string
total_months_str = str(total_months)
total_profloss_str = str(total_profloss)
max_profit_str = str(max_profit)
max_loss_str = str(max_loss)
avg_monthly_change_str = str(avg_monthly_change)

#Print everything
report_contents = "Financial Analysis \n" + "---------------------------- \n" + "Total Months: " + total_months_str + "\n" + "Total: $" + total_profloss_str + "\n" + "Average Change: $" + avg_monthly_change_str + "\n" + "Greatest Increase in Profits:" + max_profit_date + " ($" + max_profit_str + ")\n" + "Greatest Decrease in Profits:" + max_loss_date + " ($" + max_loss_str + ")\n"
print(report_contents)
 
#Make file
report =open("report.txt","a+")
report.truncate(0)
report.write(report_contents)
report.close()

