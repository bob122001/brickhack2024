import Constants, Evidence, Juror
jurorList = []
class game:
    def __init__(self, story) -> None:
        self.curRound = 0
        self.isDefendantRound = False
        self.story = story
        self.evidence = [[]]

    def Is_Def_Round(self):
        if self.curRound%2 == 1:
            self.isDefendantRound = True
            return True
        else:
            self.isDefendantRound = True
            return False
    def start_round(self):
        pass
    def chooseEvidence(self, evidence):
        for i in jurorList:
            i.reviewEvidence(evidence)
    
    def increment_round(self):
        self.curRound += 1