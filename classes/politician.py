class Politician:
    def __init__(self, fullName, initialState, value, ideology, team, command, legislative, governing, judicial, military, admin,
                 draftYear, retirementYear, deathYear, partyFlipOne, partyFlipTwo, partyFlipThree):
        self.fullName = fullName
        self.initialState = initialState
        self.value = float(value)
        self.team = team
        self.ideology = ideology
        self.command = command
        self.legislative = legislative
        self.governing = governing
        self.judicial = judicial
        self.military = military
        self.admin = admin
        self.draftYear = int(draftYear)
        self.retirementYear = retirementYear
        self.deathYear = deathYear
        self.partyFlipOne = partyFlipOne
        self.partyFlipTwo = partyFlipTwo
        self.partyFlipThree = partyFlipThree