#pybank Analysis Script Written by Carter Alvarez

#Import Modules to be Used
import os 
import csv

#Declare Variables 
months = 0
net_profits = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#Set Path For File 
csvpath = os.path.join('Resources','budget_data.csv')

#Open the CSV File 
with open(csvpath, newline='') as csvfile:

    #Specify the Delimeter we will use to Sort Through the File and Get our Variables
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the Header Row, if there is no Header, Skip
    csv_header = next(csvreader)
    row = next(csvreader)

    #Calculate the Total Number of Months with the Net Proffits and Losses, with their Row Variables 
    previous_row = int(row[1])
    months += 1 
    net_profits += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    #Create a For Loop for Each of the Rows After the Header
    for row in csvreader:
        
        #Set up a Counter for Total Months 
        months += 1
        #Calculate Net Profts and Losses
        net_profits += int(row[1])

        #Calculate the Revenue Change between the months 
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
print(f"Total Months: {months}")
print(f"Total Net Profit: ${net_profits}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")


#Write our new Analysis Data in a Text File, Will be in the PyBank Folder
output = open("analysis-pybank.txt", "w")
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(months)}")
line4 = str(f"Total Net Profit: ${str(net_profits)}")
line5 = str(f"Average Change: ${average_change}")
line6 = str(f"Greatest Increase in Profits: {greatest_increase_month}, (${highest})")
line7 = str(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))