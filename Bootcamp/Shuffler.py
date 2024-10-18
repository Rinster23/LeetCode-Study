import random


def shuffleN(oldDeck):
    newDeck = list(oldDeck)
    for i in range(len(newDeck)):
        j = random.randint(i, len(newDeck) - 1)  # inclusive
        newDeck[i], newDeck[j] = newDeck[j], newDeck[i]
    return newDeck


def shuffleNLogN(oldDeck):
    return [pair[1] for pair in sorted((random.uniform(0.0, 1.0), value) for value in oldDeck)]


def shuffleNN(oldDeck):
    moved = [False] * len(oldDeck)
    newDeck = [None] * len(oldDeck)
    for iMove in range(len(oldDeck)):
        while True:
            i = random.randint(0, len(oldDeck) - 1)
            if not moved[i]:
                moved[i] = True
                newDeck[iMove] = oldDeck[i]
                break
    return newDeck
