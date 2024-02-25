class Evidence:
    def __init__(self, isFake, probability, points, side, evidenceId) -> None:
        self.isFake = isFake
        self.probability = probability
        self.points = points
        self.side = side
        self.evidenceId = evidenceId
    