def getCardNum(card):
    return card[2:]

def getCardSuite(card):
    return card[1]

def crossPairListNoIdentity(l):
    for i_, i in enumerate(l):
            for j in (l)[(i_ + 1):]:
                yield (i,j)