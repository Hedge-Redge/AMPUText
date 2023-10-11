class Faction:
    def __init__(self, aName, aTeam, ourIdeologies):
        self.name = aName
        self.team = aTeam
        self.ideologies = ourIdeologies
        self.cpuControlled = True
        self.player = "CPU"
        self.politicians = []
    def toStr(self):
        retString = ""
        for i in self.politicians:
            retString += i.fullName + ", "
        return retString
    def ideologiesToStr(self):
        retString = ""
        for i in range(len(self.ideologies)):
            if 0 <= (i + 1) < len(self.ideologies):
                retString += self.ideologies[i] + " - "
            else:
                retString += self.ideologies[i]
        return retString