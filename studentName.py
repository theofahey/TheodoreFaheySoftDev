## Theodore Fahey
## Softdev
## K03
## 9/22/21
import random
pd1 = ["Aryaman", "Rayat", "Sadid", "Michelle", ]
pd2 = ["Name 1", "Name 2", "Name 3", "Name 4"]
pdnum = input("Input: ")
if pdnum == "1":
    randnum = random.randint(0,len(pd1))
    print(pd1[randnum])
if pdnum == "2":
    print(pd2[random.randint(0,len(pd2))])

