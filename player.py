class Player:
    def __init__(self, side) -> None:
        self.money = 3000
        self.credibility = 1
        self.side = side

    def lowerCredibility(self, percentLoweredBy):
        self.credibility -= percentLoweredBy/100

    def lowerMoney(self, amountLoweredBy):
        self.money -= amountLoweredBy