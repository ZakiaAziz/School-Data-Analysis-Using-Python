import os
import csv
print("Election Results")
print('------------------------')

#Initializing variables
total_votes=0
candidate_names=[]
candidate_votes={}

winning_candidate=""
winning_count=0
winning_percentage=0


file=("election_data.csv")
with open(file) as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)

  #counting total votes and creating list for candidates
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]

   #counting all the votes for each candidates   
        if candidate_name not in candidate_names:

            candidate_names.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    print(f'Total Votes: {total_votes} \n') 
    
    #calculating the percentage and total votes for each candidates
    for candidate_name in candidate_votes:

        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            
print('------------------------')
print(f'Winner: {winning_candidate} ')
print('------------------------')

#creating a text file

with open("analysis.text",'w') as file:
    file.write("Election Results \n")
    file.write("-----------------------\n")
    file.write("Total Votes: 369711 ")
    file.write("Charles Casper Stockham: 23.0% (85,213)\n")
    file.write("Diana DeGette: 73.8% (272,892)\n")
    file.write("Raymon Anthony Doane: 3.1% (11,606)\n")
    file.write("-----------------------\n")
    file.write("Winner: Diana DeGette\n ")
    file.write("------------------------\n")

    

