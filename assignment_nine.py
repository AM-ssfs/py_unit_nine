from deck import Deck
#from random import randint

deck = Deck()
deck.shuffle()
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
p1 = []
p2 = []

for x in range(26):
    p1.append(deck.deal())

for y in range(26):
    p2.append(deck.deal())

for x in range(len(p2)):
    if p2[x] in p1:
        print("eeeeeeeeeeeeeee")


def turn(p1, p2):
    p1l = len(p1)-1
    p2l = len(p2)-1
    if p1l <= 0:
        return "p1 lose"
    if p2l <= 0:
        return "p2 lose"
    p1c = p1.pop(0)
    p2c = p2.pop(0)
    bounty = []
    print(p1c)
    print(p2c)
    p1v = ranks.index(p1c.rank)
    p2v = ranks.index(p2c.rank)

    while p1v == p2v:

        bounty = [p1c, p2c]
        for x in range(3):
            if len(p1)-1 >= 2:
                bounty.append(p1.pop(0))
        p1c = p1.pop(0)
        for x in range(3):
            if len(p2)-1 >= 2:
                bounty.append(p2.pop(0))
        p2c = p2.pop(0)

        p1v = ranks.index(p1c.rank)
        p2v = ranks.index(p2c.rank)

    if p1v > p2v:
        p1.append(p1c)
        p1.append(p2c)
        if bounty:
            for x in bounty:
                p1.append(bounty.pop(0))
        print("p1 win")
    elif p1v < p2v:
        p2.append(p1c)
        p2.append(p2c)
        if bounty:
            for x in bounty:
                p1.append(bounty.pop(0))
        print("p2 win")

    for x in range(len(p2)):
        if p2[x] in p1:
            print("card duplicated somewhere")


winner = False
while(not winner):
    winner = turn(p1, p2)
print(winner)

