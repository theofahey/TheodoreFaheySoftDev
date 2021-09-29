# Michelle Lo, Theodore Fahey, Rayat Roy
# SoftDev
#K<06> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)
# Reads the csv file and then delimits it with a comma. Creates a Dictionary and then added keys for the job titles and
# values for their respective chance. Then we created a random and then parced through the values of the dict. Adding their
#Percentages a total value until it is greater than the random value. Then prints the key of that value.
# <yyyy>-<mm>-<dd>

import csv
import random

with open('occupations.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter= ",")
    jobs = {}
    i = 0;
    for row in spamreader:
        if (i == 0):
            i += 1
        else:
            jobs[row[0]] = float(row[1]);
        
    #random selector
r = random.random() 
s = 0
for key in jobs:
    s+= jobs[key]/100
    if(s > r):
        print(key)
        break

#dictionary
