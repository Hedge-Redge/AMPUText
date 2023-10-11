import csv
import json

filename = 'helpers/Pols.csv'

def findTitles():
    list = []
    with open(filename) as f:
        reader = csv.reader(f)
        for i in reader:
            if(i[0] == 'Full Name'):
                return i
def readCSV():
    list = []
    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        for i in reader:
            if i != titles:
                list.append(i)
    return list

titles = findTitles()
polList = readCSV()

def retPols():
    return polList