def activeDraft():

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