import Constants, Evidence, Juror
class game:
    def __init__(self, story) -> None:
        self.curRound = 0
        self.isDefendantRound = False
        self.story = story
        self.evidence = [[]]
        self.jurorList = []

    def Is_Def_Round(self):
        if self.curRound%2 == 1:
            self.isDefendantRound = True
            return True
        else:
            self.isDefendantRound = False
            return False
    def start_round(self):
        pass
    def chooseEvidence(self, evidence):
        for i in self.jurorList:
            i.reviewEvidence(evidence)
    
    def increment_round(self):
        self.curRound += 1

    def check_winner(self):
        pointsForDefendant = 0
        pointsForProsecuter = 0
        for i in self.jurorList:
            if i.sideTaken == Constants.PROSECUTOR:
                pointsForProsecuter += 1
            elif i.sideTaken == Constants.DEFENDANT:
                pointsForDefendant += 1
            else:
                if i.pointsForProsecuter > pointsForDefendant:
                    pointsForProsecuter += 1
                else:
                    pointsForDefendant += 1
