import random
import math

import helpers.populateActiveDraft
from classes.faction import Faction
from classes.politician import Politician
from helpers import reading
from helpers import *

# brings master list of pols into game
polsCSV = reading.retPols()
pols = []
for i in polsCSV:
    # fullName, initialState, value, ideology, team, command, legislative, governing, judicial, military, admin,
    # draftYear, retirementYear, deathYear, partyFlipOne, partyFlipTwo, partyFlipThree
    newPol = Politician(i[0], i[2], i[1], i[4], i[3], i[8], i[9], i[10], i[11], i[12], i[13], i[5], i[6], i[7],
                        i[14], i[15], i[16])
    pols.append(newPol)
# For all those with no retirement date or party flip Dates, set it to 9999 for calculating purposes
for i in pols:
    if i.retirementYear == "":
        i.retirementYear = 9999
    if i.deathYear == "":
        i.deathYear = 9999
    if i.partyFlipOne == "":
        i.partyFlipOne = 9999
    if i.partyFlipTwo == "":
        i.partyFlipTwo = 9999
    if i.partyFlipThree == "":
        i.partyFlipThree = 9999

phase = "start"
year = ""

# Setting draft ideologies by era
B1Ideologies = {1772: ["LW Pop", "Prog", "Lib"], 1788: ["LW Pop", "Prog", "Lib"], 1800: ["LW Pop", "Prog", "Lib"], 1820: ["LW Pop", "Prog", "Lib"],
                1840: ["LW Pop", "Prog", "Lib"], 1856: ["LW Pop", "Prog", "Lib"], 1868: ["LW Pop", "Prog", "Lib"], 1892: ["LW Pop", "Prog"],
                1916: ["LW Pop", "Prog"], 1928: ["LW Pop", "Prog"], 1948: ["LW Pop", "Prog"], 1972: ["LW Pop", "Prog"], 2000: ["LW Pop", "Prog"],
                2012: ["LW Pop", "Prog"]}
B2Ideologies = {1772: ["Lib", "Mod"], 1788: ["Lib", "Mod"], 1800: ["Lib", "Mod"], 1820: ["Lib", "Mod"], 1840: ["Lib", "Mod"],
                1856: ["Lib", "Mod"], 1868: ["Lib", "Mod"], 1892: ["Lib", "Mod"], 1916: ["Lib", "Mod"], 1928: ["Lib", "Mod"],
                1948: ["Lib", "Mod"], 1972: ["Lib", "Mod"], 2000: ["Prog", "Lib"], 2012: ["Prog", "Lib"]}
B3Ideologies = {1772: ["Mod", "Cons"], 1788: ["Mod", "Cons"], 1800: ["Mod", "Cons"], 1820: ["Mod", "Cons"], 1840: ["Mod", "Cons"],
                1856: ["Mod", "Cons"], 1868: ["Mod", "Cons"], 1892: ["Mod", "Cons"], 1916: ["Mod", "Cons"], 1928: ["Mod", "Cons"],
                1948: ["Mod", "Cons"], 1972: ["Mod", "Cons"], 2000: ["Lib", "Mod"], 2012: ["Lib", "Mod"]}
B4Ideologies = {1772: ["Cons", "Trad"], 1788: ["Cons", "Trad"], 1800: ["Cons", "Trad"], 1820: ["Cons", "Trad"], 1840: ["Cons", "Trad"],
                1856: ["Cons", "Trad"], 1868: ["Cons", "Trad"], 1892: ["Cons", "Trad"], 1916: ["Cons", "Trad"], 1928: ["Cons", "Trad"],
                1948: ["Cons", "Trad"], 1972: ["Cons", "Trad"], 2000: ["Mod", "Cons"], 2012: ["Lib", "Mod"]}
B5Ideologies = {1772: ["Trad", "RW Pop"], 1788: ["Trad", "RW Pop"], 1800: ["Trad", "RW Pop"], 1820: ["Trad", "RW Pop"], 1840: ["Trad", "RW Pop"],
                1856: ["Trad", "RW Pop"], 1868: ["Trad", "RW Pop"], 1892: ["Trad", "RW Pop"], 1916: ["Trad", "RW Pop"], 1928: ["Trad", "RW Pop"],
                1948: ["Trad", "RW Pop"], 1972: ["Cons", "Trad", "RW Pop"], 2000: ["Mod", "Cons", "Trad"], 2012: ["Mod", "Cons"]}
R1Ideologies = {1772: ["LW Pop", "Prog", "Lib"], 1788: ["LW Pop", "Prog", "Lib"], 1800: ["LW Pop", "Prog", "Lib"], 1820: ["LW Pop", "Prog", "Lib"],
                1840: ["LW Pop", "Prog"], 1856: ["LW Pop", "Prog"], 1868: ["LW Pop", "Prog"], 1916: ["LW Pop", "Prog"], 1928: ["LW Pop", "Prog", "Lib"],
                1948: ["LW Pop", "Prog", "Lib"], 1972: ["Prog", "Lib", "Mod"], 2000: ["Lib", "Mod"], 2012: ["Lib", "Mod"]}
R2Ideologies = {1772: ["Lib", "Mod"], 1788: ["Lib", "Mod"], 1800: ["Lib", "Mod"], 1820: ["Lib", "Mod"], 1840: ["Lib", "Mod"],
                1856: ["Lib", "Mod"], 1868: ["Prog", "Lib"], 1892: ["Prog", "Lib"], 1916: ["Lib", "Mod"], 1928: ["Lib", "Mod"],
                1948: ["Lib", "Mod"], 1972: ["Lib", "Mod"], 2000: ["Lib", "Mod"], 2012: ["Mod", "Cons"]}
R3Ideologies = {1772: ["Mod", "Cons"], 1788: ["Mod", "Cons"], 1800: ["Mod", "Cons"], 1820: ["Mod", "Cons"], 1840: ["Mod", "Cons"],
                1856: ["Mod", "Cons"], 1868: ["Mod", "Cons"], 1892: ["Mod", "Cons"], 1916: ["Mod", "Cons"], 1928: ["Mod", "Cons"],
                1948: ["Mod", "Cons"], 1972: ["Mod", "Cons"], 2000: ["Mod", "Cons"], 2012: ["Cons", "Trad"]}
R4Ideologies = {1772: ["Mod", "Cons"], 1788: ["Mod", "Cons"], 1800: ["Mod", "Cons"], 1820: ["Mod", "Cons"], 1840: ["Mod", "Cons"],
                1856: ["Mod", "Cons"], 1868: ["Mod", "Cons"], 1892: ["Mod", "Cons"], 1916: ["Mod", "Cons"], 1928: ["Mod", "Cons"],
                1948: ["Cons", "Trad"], 1972: ["Cons", "Trad"], 2000: ["Cons", "Trad"], 2012: ["Cons", "Trad"]}
R5Ideologies = {1772: ["Cons", "Trad", "RW Pop"], 1788: ["Cons", "Trad", "RW Pop"], 1800: ["Cons", "Trad", "RW Pop"], 1820: ["Cons", "Trad", "RW Pop"],
                1840: ["Cons", "Trad", "RW Pop"], 1856: ["Cons", "Trad", "RW Pop"], 1868: ["Cons", "Trad", "RW Pop"], 1892: ["Cons", "Trad", "RW Pop"],
                1916: ["Cons", "Trad", "RW Pop"], 1928: ["Cons", "Trad", "RW Pop"], 1948: ["Cons", "Trad", "RW Pop"], 1972: ["Cons", "Trad", "RW Pop"],
                2000: ["Trad", "RW Pop"], 2012: ["Trad", "RW Pop"]}
print("Welcome to A More Perfect Union!")

# Choose your era
validYear = False
chosenYear = 1772
eraStartDates = [1772, 1788, 1800, 1820, 1840, 1856, 1868, 1892, 1916, 1928, 1948, 1972, 2000, 2012]
while not validYear:
    chosenYear = int(input("Which year would you like to start in? Your options are 1772, 1788, 1800, 1820, 1840, 1856, 1868, 1892, 1916, 1928, 1948, 1972, 2000, 2012\n"))
    if eraStartDates.__contains__(chosenYear):
        validYear = True

# Faction creating
B1 = Faction("B1", "Blue", B1Ideologies[int(chosenYear)])
B2 = Faction("B2", "Blue", B2Ideologies[int(chosenYear)])
B3 = Faction("B3", "Blue", B3Ideologies[int(chosenYear)])
B4 = Faction("B4", "Blue", B4Ideologies[int(chosenYear)])
B5 = Faction("B5", "Blue", B5Ideologies[int(chosenYear)])
R1 = Faction("R1", "Red", R1Ideologies[int(chosenYear)])
R2 = Faction("R2", "Red", R2Ideologies[int(chosenYear)])
R3 = Faction("R3", "Red", R3Ideologies[int(chosenYear)])
R4 = Faction("R4", "Red", R4Ideologies[int(chosenYear)])
R5 = Faction("R5", "Red", R5Ideologies[int(chosenYear)])
factions = [B1, B2, B3, B4, B5, R1, R2, R3, R4, R5]

# Party flipping those who need a party flip
for i in pols:
    if int(i.partyFlipOne) <= int(chosenYear):
        if i.team == "Blue":
            i.team = "Red"
        elif i.team == "Red":
            i.team = "Blue"
for i in pols:
    if int(i.partyFlipTwo) <= chosenYear:
        if i.team == "Blue":
            i.team = "Red"
        elif i.team == "Red":
            i.team = "Blue"
for i in pols:
    if int(i.partyFlipThree) <= chosenYear:
        if i.team == "Blue":
            i.team = "Red"
        elif i.team == "Red":
            i.team = "Blue"
# Choosing user faction and setting that faction to player controlled
userFaction = input(
    "Welcome to the A More Perfect Union! Please select your faction:\nB1: " + factions[0].ideologiesToStr() +
    "\nB2: " + factions[1].ideologiesToStr() + "\nB3: " + factions[2].ideologiesToStr() + "\nB4: " + factions[3].ideologiesToStr() +
    "\nB5: " + factions[4].ideologiesToStr() + "\n\nR1: " + factions[5].ideologiesToStr() + "\nR2: " + factions[6].ideologiesToStr() +
    "\nR3: " + factions[7].ideologiesToStr() + "\nR4: " + factions[8].ideologiesToStr() + "\nR5: " + factions[9].ideologiesToStr() + "\n")
while userFaction != "B1" and userFaction != "B2" and userFaction != "B3" and userFaction != "B4" and userFaction != "B5" and userFaction != "R1" and userFaction != "R2" and userFaction != "R3" and userFaction != "R4" and userFaction != "R5" and userFaction != "None":
    userFaction = input("You did not enter a valid faction. Please enter B1, B2, B3, B4, B5, R1, R2, R3, R4, or R5:\n")
for i in factions:
    # This is just so I can get through the draft quickly for bug testing
    if userFaction == "None":
        break
    if i.name == userFaction:
        i.cpuControlled = False
        i.player = "Player"

# Begin draft
print("Welcome to the Active Draft of 1772!\n")
phase = "DraftPopulation"
draftPols = helpers.populateActiveDraft.populateActiveDraft(pols, chosenYear)
phase = "ActiveDraft"

# Determines draft order
draftOrder = factions
random.shuffle(draftOrder)
print("Draft order will be: ")
for i in draftOrder:
    print(i.name)

# Active Draft
while phase == "ActiveDraft":
    for i in draftOrder:
        print("It is " + i.name + "'s turn to draft")
        print("Available Politicians: ")
        print("Politician Name, Politician Ideology, Politician Value, Party")
        for j in draftPols:
            print(j.fullName, j.ideology, j.value, j.team)
        print("\n")

        # Human selecting draft pick and checking that it's valid
        if not i.cpuControlled:
            hasDrafted = False
            validPick = False
            while not validPick:
                draftedPol = input(i.name + ", please select your draft pick! ")
                for j in draftPols:
                    if j.fullName == draftedPol and j.team == i.team and i.ideologies.__contains__(j.ideology):
                        draftPols.remove(j)
                        i.politicians.append(j)
                        print("\n" + i.name + " drafted " + j.fullName + "!\n")
                        validPick = True
        # AI Drafting
        else:
            hasDrafted = False
            for j in draftPols:
                if j.team == i.team and i.ideologies.__contains__(j.ideology):
                    hasDrafted = True
                    draftPols.remove(j)
                    i.politicians.append(j)
                    print("\n" + i.name + " drafted " + j.fullName + "!\n")
                    break
            # Mechanism for people who don't fit their party's ideologies. e.g, Michael Flynn in 2012
            if not hasDrafted:
                for j in draftPols:
                    if j.team == i.team:
                        draftPols.remove(j)
                        i.politicians.append(j)
                        print("\n" + i.name + " drafted " + j.fullName + "!\n")
                        break
        # Checking if team still has pols
        hasRed = False
        hasBlue = False
        for j in draftPols:
            if j.team == "Red":
                hasRed = True
            if j.team == "Blue":
                hasBlue = True
        if not hasRed and not hasBlue:
            print("The draft has concluded!")
            phase = "Rookie Draft"
            break
        if not hasRed:
            for j in draftOrder:
                if j.team == "Red":
                    draftOrder.remove(j)
        if not hasBlue:
            for j in draftOrder:
                if j.team == "Blue":
                    draftOrder.remove(j)
# Reset factions
factions = [B1, B2, B3, B4, B5, R1, R2, R3, R4, R5]
# for i in factions:
#     print(i.name)
#     if not i.cpuControlled:
#         print("Your faction consists of " + i.toStr())

print("B1 consists of " + factions[0].toStr())
print("B2 consists of " + factions[1].toStr())
print("B3 consists of " + factions[2].toStr())
print("B4 consists of " + factions[3].toStr())
print("B5 consists of " + factions[4].toStr())
print("R1 consists of " + factions[5].toStr())
print("R2 consists of " + factions[6].toStr())
print("R3 consists of " + factions[7].toStr())
print("R4 consists of " + factions[8].toStr())
print("R5 consists of " + factions[9].toStr())
# Moving on to rookie draft
