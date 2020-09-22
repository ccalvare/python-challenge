#Import Modules
import os
import csv

#Declare Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li _votes = 0 
otooley_votes = 0

#Set Path For File 
csvpath = os.path.join('.','PyPoll', 'Resources','election_data.csv')

#Open the CSV File
with open(csvpath, newline = '') as csvfile:
   #Specify the Delimeter we will use to Sort Through the File and Get our Variables
    csvreader = csv.reader(csvfile, delimiter = ',')

     #Read the Header Row, if there is no Header, Skip
    csv_header = next(csvfile)

    #Create a for loop to read the rows after header
    for row in csvreader:

        #Calculate Total Votes 
        total_votes += 1

        #Calculate the Votes for Each Candidate 
         if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

        #Calculate the Percent of Votes for the Candidates 
        kahn_percent = khan_votes / total_votes
        correy_percent = correy_votes / total_votes
        li_percent = li_votes / total_votes
        otooley_percent = otooley_votes / total_votes

        #Calculate the Winner of the Election using Max
        winner = max(khan_votes,correy_votes,li_votes,otooley_votes)

        #Use If Statement to plug the winner into a new variable to display who won
        if winner == khan_votes:
        winner_name = "Khan"
        elif winner == correy_votes:
        winner_name = "Correy"
        elif winner == li_votes:
        winner_name = "Li"
        else:
        winner_name = "O'Tooley"

#         # Print Analysis
# print(f"Election Results")
# print(f"---------------------------")
# print(f"Total Votes: {total_votes}")
# print(f"---------------------------")
# print(f"Kahn: {kahn_percent:.3%}({khan_votes})")
# print(f"Correy: {correy_percent:.3%}({correy_votes})")
# print(f"Li: {li_percent:.3%}({li_votes})")
# print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
# print(f"---------------------------")
# print(f"Winner: {winner_name}")
# print(f"---------------------------")

# # Specify File To Write To
# output_file = os.path.join('.', 'PyPoll', 'Resources', 'election_data_revised.text')

# # Open File Using "Write" Mode. Specify The Variable To Hold The Contents
# with open(output_file, 'w',) as txtfile:

# # Write New Data
#     txtfile.write(f"Election Results\n")
#     txtfile.write(f"---------------------------\n")
#     txtfile.write(f"Total Votes: {total_votes}\n")
#     txtfile.write(f"---------------------------\n")
#     txtfile.write(f"Kahn: {kahn_percent:.3%}({khan_votes})\n")
#     txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
#     txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
#     txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
#     txtfile.write(f"---------------------------\n")
#     txtfile.write(f"Winner: {winner_name}\n")
#     txtfile.write(f"---------------------------\n")