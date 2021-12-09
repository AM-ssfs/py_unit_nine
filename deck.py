from card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def make_deck(self):
        Deck.__init__(self)
        for x in range(2, 15):
            self.cards.append(Card("Hearts", x))
        for x in range(2, 15):
            self.cards.append(Card("Diamonds", x))
        for x in range(2, 15):
            self.cards.append(Card("Clubs", x))
        for x in range(2, 15):
            self.cards.append(Card("Spades", x))
        return self.cards


def main():
    deck = Deck.make_deck(Deck)
    for x in range(52):
        print(str(deck[x].rank) + " of " + deck[x].suit)


if __name__ == '__main__':
    main()
