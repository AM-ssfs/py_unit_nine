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


def turn(p1, p2):
    p1l = len(p1)-1
    p2l = len(p2)-1
    p1c = p1.pop(0)
    p2c = p2.pop(0)
    print(p1c)
    print(p2c)
    p1v = ranks.index(p1c.rank)
    p2v = ranks.index(p2c.rank)
    if p1v == p2v:
        p1p = [p1c]
        p2p = [p2c]
        if p1l >= 4:
            for x in range(3):
                p1p.append(p1.pop(0))
        else:
            for x in range(p1l-1):
                p1p.append(p1.pop(0))

        pass

    elif p1v > p2v:
        p1.append(p1c)
        p1.append(p2c)
        print("p1 win")
    elif p1v < p2v:
        p2.append(p1c)
        p2.append(p2c)
        print("p2 win")


p1 = player1
p1l = player one deck len
p1c = pyaer 1 card
p1p = prize pile when they are euqal


turn(p1, p2)