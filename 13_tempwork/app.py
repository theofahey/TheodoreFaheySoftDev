# Eccentric Pencil: Theodore Fahey, Oscar Wang, Edwin Zheng
# SoftDev
# K13: Template for Success
# 2021-10-08

from flask import Flask, render_template
import random
import csv
app = Flask(__name__) #create instance of class Flask

# opens the csv file and returns a dictionary of its data
#  along with the total aggregate of the data
def openCSV(fname):
    dict = {}
    temp_total = 0
    total = 0
    with open(fname) as f:
        f.readline()
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if 'Total' in row:
                total = float(row[1])
            else:      # the keys are the occupations and the value is a list of the corresponding percentage and link
                dict[row[0]] = [float(row[1]), row[2]]  
                temp_total += float(row[1])
        if total == 0:
            total = temp_total
        return dict, total

# picks an occupation based on the weighted percentages
def picker():
    jobDict, total = openCSV('data/occupations.csv')
    total = total * 10
    values = list(jobDict.values())
    occ = list(jobDict.keys())
    conDict = {}
    sum = 0
    for i in range(len(values)):
        percent = values[i][0]
        percent *= 10
        sum += percent
        values[i] = sum
    for i in range(len(occ)):
        conDict[occ[i]] = values[i]
    n = random.randint(0, total-1)
    for i in conDict:
        if (n < conDict[i]):
            return i

@app.route("/")       # landing page
def display():      #code to display the HTML on the webpage
    # HTML code to redirect to the right place
    output = f'''
    <center><p style="font-size:100px"><a href="http://localhost:5000//occupyflaskst">GO HERE</a></p></center>
    '''
    return output


@app.route("/occupyflaskst")    # main page
def run(): # displays the occupations as links in a table
    data, total = openCSV("data/occupations.csv")
    links = []
    # creates a 2d list called links that stores each occupation and their respective link as given in the csv
    for key in data:
        links.append([key,data[key][1]])
    picked = picker()    # randomly picks an occupation
    randLink = ''
    links.sort()    # sorts links so that the table is in alphabetical order
    for row in links:    # appends the link to the randomly selected occupation
        if row[0] == picked:
            randLink = row[1]
    return render_template("tablified.html", randOcc=picked, RL=randLink, collection=links)

app.debug = True
app.run()