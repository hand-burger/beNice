#So the strategy here is to defect first turn
#See what the opponent does
#If they are nice (cooperate) I will be nice until the end
#If they are mean (defect) I will be mean until the end
def strategy(history, memory):
    choice = None
    beNice = memory
    gameLength = history.shape[1]

    if gameLength == 0: #first round, so defect
        choice = 0
    elif gameLength > 0: #after first round, so check what the other does and do that until the end
        opponentsAction = history[1, 0]
        if opponentsAction == 1:
            beNice = True
        else:
            beNice = False
    if beNice:
        choice = 1
    else:
        choice = 0

    return choice, beNice