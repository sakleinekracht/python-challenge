import os
import csv
from collections import defaultdict

data = csv.reader(open('/Users/sarakleine-kracht/Desktop/python-challenge/PyPoll/Resources/Resources/election_data.csv'))
my_report = open('/Users/sarakleine-kracht/Desktop/python-challenge/PyPoll/Analysis/poll_analysis.text','w')

header = next(data)
votes = 0
candidate_list = ["Charles Casper Stockham", "Diana DeGette","Raymon Anthony Doane"]
total_ccs = 0
total_dd = 0
total_rad = 0
counter = defaultdict(int)

for row in data:
   
   votes += 1 #append; votes = votes +1
   
   counter[row[2]] += 1 #count votes per candidate
   #print(dict(counter))

vote_dict = {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606} #changing counter results into dictionary

my_list = [i for i in vote_dict.values()]
#print(my_list)
   
total_ccs = (my_list[0])

total_dd = (my_list[1])

total_rad = (my_list[1])


output = f'''
Election Results
-------------------------
Total Votes: {votes}
-------------------------
{candidate_list[0]}: {((total_ccs/votes) * 100):,.2f}% ({total_ccs})
{candidate_list[1]}: {((total_dd/votes) * 100):,.2f}% ({total_dd})
{candidate_list[2]}: {((total_rad/votes) * 100):,.2f}% ({total_rad})
-------------------------
Winner: {candidate_list[1]} 
-------------------------
'''

print(output)
my_report.write(output)


