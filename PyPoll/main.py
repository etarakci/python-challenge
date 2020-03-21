#Python-Challenge hw for UCB Data Analytics Bootcamp by Erendiz Tarakci
#last updated 3/21/2020

import os
import csv
csvpath = os.path.normpath("/Users/erendiztarakci/UCBWork/UCB-BER-DATA-PT-02-2020-U-C/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")
#Three comlumns:  Voter ID, County, and Candidate

voter_dict = {}
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    csv_header = next(csvreader)

    #loop through rows and add info to dictionary
    for row in csvreader:
        voter_dict[row[0]] = [row[1],row[2]]

#The total number of votes cast
total_votes = len(voter_dict)

#A complete list of candidates who received votes
#The total number of votes each candidate won
candidates = {}
for voter_id in voter_dict:
    candidate = voter_dict[voter_id][1]
    #check if candidate in dict
    if candidate in candidates:
        candidates[candidate] += 1
    else:
        candidates[candidate] = 1

candidates_list = list(candidates.keys())

#The percentage of votes each candidate won
percent_votes = candidates.copy()
for cand in percent_votes:
    percent_votes[cand] = percent_votes[cand]/total_votes

#The winner of the election based on popular vote. 
cands_list = list(candidates.keys())
votes_list = list(candidates.values())
max_votes = 0
winner = ''
i = 0
while i < len(cands_list):
    if votes_list[i] > max_votes:
        max_votes = votes_list[i]
        winner = cands_list[i]
        i +=1
    else:
        i+=1

#print things and write to file
report = open("PyPoll/report.txt","a+")
report.truncate(0)

total_votes_str = str(total_votes)

print("ELECTION RESULTS \n------------------------")
report.write("ELECTION RESULTS \n------------------------\n")

print("Total Votes: " ,total_votes)
report.write("Total Votes: " + total_votes_str + "\n")

print("------------------------")
report.write("------------------------\n")

for cand in candidates:
    percent = str(round(percent_votes[cand]*100,2))
    num_votes = str(candidates[cand])
    contents = cand + ": " + percent + "% (" + num_votes + ")\n"
    print(contents)
    report.write(contents)
    
print("------------------------")
report.write("------------------------\n")

print("Winner: " , winner)
report.write("Winner: " + winner + "\n")

print("------------------------")
report.write("------------------------\n")

report.close()








