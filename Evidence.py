class Evidence:
    def __init__(self, isFake, probability, points, side, evidenceId, price) -> None:
        self.isFake = isFake
        self.probability = probability
        self.points = points
        self.side = side
        self.evidenceId = evidenceId
        self.price = price

    def display(self):
        pass
    