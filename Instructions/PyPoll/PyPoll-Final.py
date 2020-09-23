#pypoll Analysis Script Written by Carter Alvarez

#Import Modules
import os
import csv

#Declare Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
otooley_votes = 0
li_votes = 0 


#Set Path For File 
csvpath = os.path.join('Resources','election_data.csv')

#Open the CSV File
with open(csvpath, newline = '') as csvfile:
   #Specify the Delimeter we will use to Sort Through the File and Get our Variables
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read the Header Row, if there is no Header, Skip
    csv_header = next(csvfile)

    #Create a for loop to read the rows after header
    for row in csvreader:

        #Set up a Total Votes Counter
        total_votes += 1

        #Calculate the Votes for Each Candidate Through an If Statement 
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

           

    #Calculate the Percent of Votes Each Candidate Recieved  
    kahn_vote_percent = khan_votes / total_votes
    correy_vote_percent = correy_votes / total_votes
    li_vote_percent = li_votes / total_votes
    otooley_vote_percent = otooley_votes / total_votes

    #Calculate the Winner of the Election using "Max"
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

# Print Analysis in Terminal
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {kahn_vote_percent:.2%}({khan_votes})")
print(f"Correy: {correy_vote_percent:.2%}({correy_votes})")
print(f"O'Tooley: {otooley_vote_percent:.2%}({otooley_votes})")
print(f"Li: {li_vote_percent:.2%}({li_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")



#Write our new Analysis Data in a Text File. It will appear in the PyPoll Folder
output = open("analysis-pypoll.txt", "w")
line1 = "Election Results"
line2 = "---------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = "---------------------"
line5 = str(f"Kahn: {kahn_vote_percent:.2%}({khan_votes})")
line6 = str(f"Correy: {correy_vote_percent:.2%}({correy_votes})")
line7 = str(f"O'Tooley: {otooley_vote_percent:.2%}({otooley_votes})")
line8 = str(f"Li: {li_vote_percent:.2%}({li_votes})")
line9 = "---------------------"
line10 = str(f"Winner: {winner_name}")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10))