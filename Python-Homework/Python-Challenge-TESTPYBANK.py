#Import Modules to be Used
import os 
import csv

#Declare Variables 
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#Set Path For File 
csvpath = os.path.join('.','PyBank','Resources','budget_data.csv')

#Open the CSV File 
with open(csvpath, newline='') as csvfile:

    #Specify the Delimeter we will use to Sort Through the File and Get our Variables
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the Header Row, if there is no Header, Skip
    csv_header = next(csvreader)
    row = next(csvreader)

    #Calculate the Total Number of Months with the Net Proffits and Losses, with their Row Variables 
    previous_row = int(row[1])
    total_months += 1 
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    #Create a For Loop for Each of the Rows After the Header
    for row in csvreader:
        
        #Calculate Total Months 
        total_months += 1
        #Calculate Net Profts and Losses
        net_amount += int(row[1])

        #Calculate Change between the months 
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

        #Calculate the Greatest Increase 
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        #Calculate Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

    #Calculate the Avergage Change and the Date's
    average_change = sum(monthly_change) / len(monthly_change)
    highest = max(monthly_change)
    lowest = min(monthly_change)

#Display the Analysis  
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# # Specify File To Write To
# output_file = os.path.join('.', 'PyBank', 'Resources', 'budget_data_revised.text')

# # Open File Using "Write" Mode. Specify The Variable To Hold The Contents
# with open(output_file, 'w',) as txtfile:

# #Write our new Analysis Data in a Text File 
#     txtfile.write(f"Financial Analysis\n")
#     txtfile.write(f"---------------------------\n")
#     txtfile.write(f"Total Months: {total_months}\n")
#     txtfile.write(f"Total: ${net_amount}\n")
#     txtfile.write(f"Average Change: ${average_change}\n")
#     txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
#     txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")