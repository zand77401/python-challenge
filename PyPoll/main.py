import csv

csvpath = 'Resources/election_data.csv'

#create empty list of all candidates that were voted for
candidates = []

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #Create a list for votes of all candidates
    for row in csvreader:
        candidate = row[2]
        candidates.append(candidate)

#create a variable of total number of votes cast
total_votes = len(candidates)

#Find all unique names of candidates by creating a new list and looping though the candidates list
unique_candidate_list = []
for x in candidates:
    if x not in unique_candidate_list:
        unique_candidate_list.append(x)


#create an empty list for each unique name of candidates
khan, correy, li, otooley = [], [], [], []    


#loop through original candidates list and create a conditional statement to parse the number of votes and append to respective 
# candidate list 
for x in candidates:
    if x == 'Khan':
        khan.append(x)
    elif x == 'Correy':
        correy.append(x)
    elif x == 'Li':
        li.append(x)
    elif x == "O'Tooley":
        otooley.append(x)

#Create variables that will count the number of votes for each candidate
votes_for_khan = len(khan)
votes_for_correy = len(correy)
votes_for_li = len(li)
votes_for_otooley = len(otooley)

#Create variables that will caldulate the percent of votes each candidate won
percent_khan = round((votes_for_khan / total_votes) * 100, 3)
percent_correy = round((votes_for_correy / total_votes) * 100, 3)
percent_li = round((votes_for_li / total_votes) * 100, 3)
percent_otooley = round((votes_for_otooley / total_votes) * 100, 3)

#Create a dictionary with candidate names as the keys and number of votes as the value
candidate_dict= {}
candidate_dict['Khan'] = votes_for_khan
candidate_dict['Correy'] = votes_for_correy
candidate_dict['Li '] = votes_for_li
candidate_dict["O'Tooley"] = votes_for_otooley

#Find the candidate with the most votes from the candidate dictionary
most_votes = max(candidate_dict, key=candidate_dict.get)

#Print results to terminal
print("Election Results")
print("-"*40)
print(f"Total Votes: {total_votes}")
print("-"*40)
print(f"{unique_candidate_list[0]}: {percent_khan}% ({votes_for_khan})")
print(f"{unique_candidate_list[1]}: {percent_correy}% ({votes_for_correy})")
print(f"{unique_candidate_list[2]}: {percent_li}% ({votes_for_li})")
print(f"{unique_candidate_list[3]}: {percent_otooley}% ({votes_for_otooley})")
print("-"*40)
print(f"Winner: {most_votes}")
print("-"*40)

#Exported results to text file in GitBash by typing:  python main.py > PyPoll_Output.txt