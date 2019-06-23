# import the os module
import os
import csv

# set path for csv file
poll_csv = os.path.join("election_data.csv")

# read the csv file
with open (poll_csv, 'r') as csvfile:
    # split the data
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # skip the header
    next(csvreader, None)

    # assign  variables and set to 0 
    total_votes = 0

    #set the list to store data
    candidates = []
    unique_candidate_vote =[]
    vote_percent = []


    # loop through data
    for row in csvreader:
        # calculate the total number of votes
        total_votes = total_votes + 1

        # if candidate is not on the list lets add the name to the list along with the vote
        # if candidate on the list then add only vote to the name of the candidate

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            unique_candidate_vote.append(1)

        else:
            index = candidates.index(row[2]) 
            unique_candidate_vote[index] += 1 

    # add results to vote_percent list
    for x in unique_candidate_vote:
         vote_percent.append((int(x)/total_votes)*100)

    # find the winner
    winner = max(unique_candidate_vote)
    index = unique_candidate_vote.index(winner)
    winning_candidate = candidates[index]    


# print the results
print("Election Results")
print("--------------------------")
print("Total Votes:" + str(total_votes))
print("--------------------------")
for i in range (len(candidates)):
    print(candidates[i] + ": " + str(round(vote_percent[i], 1)) + "% " + "(" +str(unique_candidate_vote[i]) +")" )
print("--------------------------")
print("Winner: " + str(winning_candidate))
print("--------------------------") 


#  write text doc with results     
with open('election_data_results.txt', 'w') as text:
    
    text.write("Election Results" + "\n")
    text.write("--------------------------\n")
    text.write("Total Votes:" + str(total_votes) + "\n")
    text.write("--------------------------\n")
    for i in range (len(candidates)):
        text.write(candidates[i] + ": " + str(round(vote_percent[i], 1)) + "% " + "(" +str(unique_candidate_vote[i]) +")" + "\n")
    text.write("--------------------------\n")
    text.write("Winner: " + str(winning_candidate) + "\n")
    text.write("--------------------------\n") 





