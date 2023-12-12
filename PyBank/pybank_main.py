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
