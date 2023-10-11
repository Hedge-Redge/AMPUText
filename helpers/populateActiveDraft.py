def minimum(a, b):
    if a <= b:
        return a
    else:
        return b
def populateActiveDraft(pols, year):
    retPols = []
    for i in pols:
        if int(i.draftYear) < int(year) < minimum(int(i.deathYear), int(i.retirementYear)):
            retPols.append(i)
    return retPols
