import Constants
curRound = 0
isDefendantRound = False


while curRound > Constants.ROUNDS:
    curRound += 1
    if isDefendantRound:
        isDefendantRound = False
    else:
        isDefendantRound = True