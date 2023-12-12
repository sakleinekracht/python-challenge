# python-challenge

import os
import csv

data = csv.reader(open('Resources/budget_data.csv'))
my_report = open('Analysis/budget_analysis.text','w')

months = 0
total = 0
total_ch = 0
prev_rev = 0
inc = ["", 0]
dec = ["", 0]
header = next(data)

for r in data:
   months += 1 #append; months = months +1

   rev = int(r[1])
   total += rev

   ch = rev - prev_rev
   if prev_rev == 0:
      ch = 0 

   total_ch += ch #change

   #greatest increase 
   if ch > inc[1]:
      inc[0] = r[0]
      inc[1] = ch
   
   #greatest decrease
   if ch < dec[1]:
      dec[0] = r[0]
      dec[1] = ch

   prev_rev = rev #reset variable

output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''

print(output)
my_report.write(output)


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
