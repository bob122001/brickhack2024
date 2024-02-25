import Evidence, random, Constants

class Juror:
    sideTaken = None
    prosecutorPoints = 0
    defendantPoints = 0

    def reviewEvidence(self, evidence):
        if random.random() < evidence.probablilty:
            if evidence.side == Constants.PROSECUTOR:
                self.prosecutorPoints += evidence.points
            else:
                self.prosecutorPoints += evidence.points
