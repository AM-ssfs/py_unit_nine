class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __str__(self):
        return str(self.rank)+" of "+str(self.suit)

    def __gt__(self, other):
        return self.ranks.index(self.ranks) > other.ranks.index(other.rank)
