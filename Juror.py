import Evidence, random, Constants

class Juror:
    def __init__(self):
        self.sideTaken = None
        self.prosecutorPoints = 0
        self.defendantPoints = 0

    def reviewEvidence(self, evidence):
        if random.random() < evidence.probablilty:
            if evidence.side == Constants.PROSECUTOR:
                self.prosecutorPoints += evidence.points
            else:
                self.prosecutorPoints += evidence.points
