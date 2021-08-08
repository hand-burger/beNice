#If round one then 1, then switch
#Okay this ones pretty complex so it's alright if you don't understand
#So on the first round the choice is always cooperate
#But get this, next time it switches to defect then next time it switches again
def strategy(history, memory):
    choice = memory
    gameLength = history.shape[1]

    if gameLength == 0: #first turn
        choice = 1
    else:
        if choice == 0:
            choice = 1
        else:
            choice = 0

    return choice, choice