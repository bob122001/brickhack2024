import Constants

class game:
    def __init__(self,) -> None:
        self.curRound = 0
        self.isDefendantRound = False


    def Is_Def_Round(self):
        if self.curRound%2 == 1:
            self.isDefendantRound = True
            return True
        else:
            self.isDefendantRound = True
            return False
    
    def increment_round(self):
        self.curRound += 1