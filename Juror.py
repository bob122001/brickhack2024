import Evidence, random, Constants

class Juror:
    def __init__(self):
        self.sideTaken = None
        self.prosecutorPoints = 0
        self.defendantPoints = 0

    def reviewEvidence(self, evidence : Evidence):
        if random.random() < evidence.probablilty:
            if evidence.side == Constants.PROSECUTOR:
                self.prosecutorPoints += evidence.points
                if self.prosecutorPoints >= 100:
                    self.sideTaken = Constants.PROSECUTOR
            else:
                self.defendantPoints += evidence.points
                if self.defendantPoints >= 100:
                    self.sideTaken = Constants.PROSECUTOR
